"""Content indexing utilities for codehaus-content.

This module handles building, caching, and managing search indexes for content.
"""

import json
import os
import re
import subprocess
from typing import List, Optional

from . import content_util


def _get_index_dir():
    """Get the index directory path."""
    return content_util.get_cache_dir('codehaus_mcp')


def _get_index_file(content_type: str):
    """Get the index file path for a content type."""
    index_dir = _get_index_dir()
    return os.path.join(index_dir, f'{content_type}_index.json')


def _get_git_revision() -> Optional[str]:
    """Get the current git revision (commit hash).
    
    Returns:
        Commit hash string, or None if git is not available or not in a git repo
    """
    root = content_util.get_project_root()
    try:
        result = subprocess.run(
            ['git', 'rev-parse', 'HEAD'],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, FileNotFoundError):
        pass
    return None


def _has_directory_changed_since_revision(content_type: str, revision: str) -> bool:
    """Check if any files in the content directory have changed since a git revision.
    
    Args:
        content_type: Content type ('docs', 'rtopro-help', 'otter')
        revision: Git commit hash to check against
        
    Returns:
        True if there are changes, False if no changes (or if git check fails, returns True to be safe)
    """
    root = content_util.get_project_root()
    
    # Get the directory path for this content type
    if content_type == 'docs':
        target_dir = content_util._get_docs_dir()
    elif content_type == 'rtopro-help':
        target_dir = content_util._get_rtopro_help_dir()
    elif content_type == 'otter':
        target_dir = content_util._get_otter_dir()
    else:
        return True  # Unknown type, assume changed to be safe
    
    if not os.path.exists(target_dir):
        return False
    
    # Get relative path from project root
    rel_dir = os.path.relpath(target_dir, root)
    
    try:
        # Check if there are any changes to files in this directory since the revision
        # Use --name-only to avoid loading full file contents
        result = subprocess.run(
            ['git', 'diff', '--name-only', revision, 'HEAD', '--', rel_dir],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
            timeout=10
        )
        if result.returncode == 0:
            # If there's any output, files have changed
            return bool(result.stdout.strip())
        # If git command fails, assume changed to be safe
        return True
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, FileNotFoundError):
        # If git is not available or there's an error, assume changed to be safe
        return True


def tokenize(text: str) -> List[str]:
    """Tokenize text for search indexing."""
    if not text:
        return []
    # Convert to lowercase and split on non-word characters
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens


def _extract_doc_title(filename: str, content_type: str) -> str:
    """Extract document title from filename.
    
    Args:
        filename: The filename (without path)
        content_type: Content type ('docs', 'rtopro-help', 'otter')
        
    Returns:
        Document title string
    """
    if content_type == 'otter':
        # Extract title from filename (remove timestamp and ID)
        # Format: 2025-08-07-23-01-27 Lesson 1A [223PAFH4ESDDYSLT].txt
        title_match = re.search(r'\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}\s+(.+?)\s+\[', filename)
        if title_match:
            return title_match.group(1)
        # Fallback: remove extension
        return filename.rsplit('.', 1)[0] if '.' in filename else filename
    else:
        # For docs and rtopro-help: remove extension and replace separators
        base_name = filename.rsplit('.', 1)[0] if '.' in filename else filename
        return base_name.replace('_', ' ').replace('-', ' ')


def _process_file(
    file_path: str,
    filename: str,
    base_dir: str,
    content_type: str,
    documents: list,
    tokenized_documents: list
) -> None:
    """Process a single file and add it to the index.
    
    Args:
        file_path: Full path to the file
        filename: Just the filename (without path)
        base_dir: Base directory for relative path calculation
        content_type: Content type ('docs', 'rtopro-help', 'otter')
        documents: List to append document info to
        tokenized_documents: List to append tokenized content to
    """
    content = content_util.read_file_content(file_path)
    if not content:
        return
    
    # Extract document ID and title based on content type
    if content_type == 'otter':
        rel_path = os.path.relpath(file_path, base_dir)
        doc_id = rel_path.replace('/', '_').replace('\\', '_').replace('.txt', '')
        doc_title = _extract_doc_title(filename, content_type)
        doc_data = {
            'document_id': doc_id,
            'document_title': doc_title,
            'file_path': file_path,
            'content': content,
            'content_type': content_type,
            'relative_path': rel_path
        }
    else:
        # For docs and rtopro-help
        extension = '.md'
        if filename.endswith(extension):
            doc_id = filename[:-len(extension)]
        else:
            doc_id = filename.rsplit('.', 1)[0] if '.' in filename else filename
        doc_title = _extract_doc_title(filename, content_type)
        doc_data = {
            'document_id': doc_id,
            'document_title': doc_title,
            'file_path': file_path,
            'content': content,
            'content_type': content_type
        }
    
    tokens = tokenize(content)
    documents.append(doc_data)
    tokenized_documents.append(tokens)


def _build_index(content_type: str) -> dict:
    """Build search index for a content type."""
    documents = []
    tokenized_documents = []
    
    # Get base directory and file extension based on content type
    if content_type == 'docs':
        base_dir = content_util._get_docs_dir()
        file_extension = '.md'
        walk_subdirs = False
    elif content_type == 'rtopro-help':
        base_dir = content_util._get_rtopro_help_dir()
        file_extension = '.md'
        walk_subdirs = False
    elif content_type == 'otter':
        base_dir = content_util._get_otter_dir()
        file_extension = '.txt'
        walk_subdirs = True
    else:
        return {
            'documents': documents,
            'tokenized_documents': tokenized_documents
        }
    
    if not os.path.exists(base_dir):
        return {
            'documents': documents,
            'tokenized_documents': tokenized_documents
        }
    
    # Process files
    if walk_subdirs:
        # Walk through all subdirectories (for otter)
        for root, dirs, files in os.walk(base_dir):
            for filename in files:
                if filename.endswith(file_extension):
                    file_path = os.path.join(root, filename)
                    _process_file(file_path, filename, base_dir, content_type, documents, tokenized_documents)
    else:
        # Process files directly in base directory (for docs and rtopro-help)
        for filename in os.listdir(base_dir):
            if filename.endswith(file_extension):
                file_path = os.path.join(base_dir, filename)
                _process_file(file_path, filename, base_dir, content_type, documents, tokenized_documents)
    
    return {
        'documents': documents,
        'tokenized_documents': tokenized_documents
    }


def build_or_load_index(content_type: str) -> dict:
    """Build or load search index for a content type.
    
    Uses git revision tracking to determine if the index needs to be rebuilt.
    The index is only rebuilt if files in the content directory have changed
    since the git revision stored in the index.
    """
    index_file = _get_index_file(content_type)
    current_revision = _get_git_revision()
    
    # Check if index exists and we can use git revision tracking
    if os.path.exists(index_file) and current_revision:
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                cached_index = json.load(f)
            
            # Check if we have a stored revision
            stored_revision = cached_index.get('git_revision')
            
            if stored_revision:
                # Check if current revision matches stored revision
                if stored_revision == current_revision:
                    # Same revision - no need to check for changes, index is up to date
                    # Load from cache
                    return {
                        'documents': [
                            {
                                'document_id': doc['document_id'],
                                'document_title': doc['document_title'],
                                'file_path': doc['file_path'],
                                'content_type': doc['content_type'],
                                'content': None  # Will be loaded from file when needed
                            }
                            for doc in cached_index['documents']
                        ],
                        'tokenized_documents': cached_index['tokenized_documents']
                    }
                else:
                    # Different revision, check if directory changed since stored revision
                    if not _has_directory_changed_since_revision(content_type, stored_revision):
                        # Directory hasn't changed, just update the revision in cache
                        cached_index['git_revision'] = current_revision
                        with open(index_file, 'w', encoding='utf-8') as f:
                            json.dump(cached_index, f, indent=2, ensure_ascii=False)
                        # Return cached data
                        return {
                            'documents': [
                                {
                                    'document_id': doc['document_id'],
                                    'document_title': doc['document_title'],
                                    'file_path': doc['file_path'],
                                    'content_type': doc['content_type'],
                                    'content': None
                                }
                                for doc in cached_index['documents']
                            ],
                            'tokenized_documents': cached_index['tokenized_documents']
                        }
                    # Directory has changed, need to rebuild
        except (json.JSONDecodeError, KeyError, IOError):
            # Index file is corrupted or invalid, rebuild
            pass
    elif os.path.exists(index_file) and not current_revision:
        # Index exists but git is not available - can't verify, so rebuild to be safe
        pass
    
    # Build index (either doesn't exist, is out of date, or git unavailable)
    index_data = _build_index(content_type)
    
    # Save index with git revision
    # Only save documents metadata, not full content (to save space)
    index_to_save = {
        'git_revision': current_revision,
        'documents': [
            {
                'document_id': doc['document_id'],
                'document_title': doc['document_title'],
                'file_path': doc['file_path'],
                'content_type': doc['content_type'],
                'word_count': len(doc['content'].split())
            }
            for doc in index_data['documents']
        ],
        'tokenized_documents': index_data['tokenized_documents']
    }
    
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_to_save, f, indent=2, ensure_ascii=False)
    
    return index_data


def rebuild_index(content_type: Optional[str] = None) -> dict:
    """Force rebuild of search index.
    
    Args:
        content_type: Content type to rebuild ('docs', 'rtopro-help', 'otter', or None for all)
        
    Returns:
        dict with counts of documents indexed
    """
    content_types_to_rebuild = [content_type] if content_type else content_util.get_content_types()
    
    results = {}
    
    for ct in content_types_to_rebuild:
        index_file = _get_index_file(ct)
        if os.path.exists(index_file):
            os.remove(index_file)
        
        index_data = build_or_load_index(ct)
        results[ct] = len(index_data['documents'])
    
    return results
