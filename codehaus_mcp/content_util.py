"""Content search and retrieval utilities for codehaus-content.

This module provides functions to search and retrieve content from:
- Markdown documentation files (infinite-stairway-designer/docs/ and rtopro-help/)
- Transcript files (otter/)
"""

import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

from rank_bm25 import BM25Okapi


def get_content_types():
    """Get list of available content types."""
    return ['docs', 'rtopro-help', 'otter']


def _get_project_root():
    """Get the project root directory."""
    # This file is in codehaus_mcp/, so go up one level
    this_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(this_dir)
    return root_dir


def _get_docs_dir():
    """Get the docs directory path."""
    root = _get_project_root()
    return os.path.join(root, 'infinite-stairway-designer', 'docs')


def _get_rtopro_help_dir():
    """Get the rtopro-help directory path."""
    root = _get_project_root()
    return os.path.join(root, 'rtopro-help')


def _get_otter_dir():
    """Get the otter directory path."""
    root = _get_project_root()
    return os.path.join(root, 'otter')


def _get_index_dir():
    """Get the index directory path."""
    root = _get_project_root()
    index_dir = os.path.join(root, '.cache', 'codehaus_mcp')
    os.makedirs(index_dir, exist_ok=True)
    return index_dir


def _get_index_file(content_type: str):
    """Get the index file path for a content type."""
    index_dir = _get_index_dir()
    return os.path.join(index_dir, f'{content_type}_index.json')


def _get_git_revision() -> Optional[str]:
    """Get the current git revision (commit hash).
    
    Returns:
        Commit hash string, or None if git is not available or not in a git repo
    """
    root = _get_project_root()
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
    root = _get_project_root()
    
    # Get the directory path for this content type
    if content_type == 'docs':
        target_dir = _get_docs_dir()
    elif content_type == 'rtopro-help':
        target_dir = _get_rtopro_help_dir()
    elif content_type == 'otter':
        target_dir = _get_otter_dir()
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


@dataclass
class DocumentInfo:
    """Information about a document."""
    document_id: str
    document_title: str
    file_path: str
    content_type: str
    word_count: int
    metadata: dict


@dataclass
class SearchResult:
    """Search result for a document."""
    document_id: str
    document_title: str
    file_path: str
    content_type: str
    score: float
    snippet: str


def _tokenize(text: str) -> List[str]:
    """Tokenize text for search indexing."""
    if not text:
        return []
    # Convert to lowercase and split on non-word characters
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens


def _read_file_content(file_path: str) -> str:
    """Read file content with proper error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except (IOError, OSError) as e:
        print(f'Error reading file {file_path}: {e}')
        return ''


def _generate_snippet(content: str, query_tokens: List[str], max_words: int = 150) -> str:
    """Generate a snippet from content, prioritizing query term matches."""
    if not content:
        return ''
    
    words = content.split()
    
    # Try to find first occurrence of any query token
    content_lower = content.lower()
    first_match_pos = None
    
    for token in query_tokens:
        pos = content_lower.find(token)
        if pos != -1:
            # Find word position
            before_match = content_lower[:pos]
            word_pos = len(before_match.split())
            if first_match_pos is None or word_pos < first_match_pos:
                first_match_pos = word_pos
    
    # If we found a match, center snippet around it
    if first_match_pos is not None:
        start = max(0, first_match_pos - max_words // 2)
        end = min(len(words), start + max_words)
        snippet_words = words[start:end]
    else:
        # Just take first N words
        snippet_words = words[:max_words]
    
    snippet = ' '.join(snippet_words)
    
    # Add ellipsis if truncated
    if len(words) > max_words:
        if first_match_pos is not None and first_match_pos > max_words // 2:
            snippet = '... ' + snippet
        if len(snippet_words) == max_words:
            snippet = snippet + ' ...'
    
    return snippet


def _build_index(content_type: str) -> dict:
    """Build search index for a content type."""
    documents = []
    tokenized_documents = []
    
    if content_type == 'docs':
        base_dir = _get_docs_dir()
        if os.path.exists(base_dir):
            for filename in os.listdir(base_dir):
                if filename.endswith('.md'):
                    file_path = os.path.join(base_dir, filename)
                    content = _read_file_content(file_path)
                    if content:
                        doc_id = filename[:-3]  # Remove .md extension
                        doc_title = doc_id.replace('_', ' ').replace('-', ' ')
                        tokens = _tokenize(content)
                        documents.append({
                            'document_id': doc_id,
                            'document_title': doc_title,
                            'file_path': file_path,
                            'content': content,
                            'content_type': content_type
                        })
                        tokenized_documents.append(tokens)
    
    elif content_type == 'rtopro-help':
        base_dir = _get_rtopro_help_dir()
        if os.path.exists(base_dir):
            for filename in os.listdir(base_dir):
                if filename.endswith('.md'):
                    file_path = os.path.join(base_dir, filename)
                    content = _read_file_content(file_path)
                    if content:
                        doc_id = filename[:-3]  # Remove .md extension
                        doc_title = doc_id.replace('_', ' ').replace('-', ' ')
                        tokens = _tokenize(content)
                        documents.append({
                            'document_id': doc_id,
                            'document_title': doc_title,
                            'file_path': file_path,
                            'content': content,
                            'content_type': content_type
                        })
                        tokenized_documents.append(tokens)
    
    elif content_type == 'otter':
        base_dir = _get_otter_dir()
        if os.path.exists(base_dir):
            # Walk through all subdirectories
            for root, dirs, files in os.walk(base_dir):
                for filename in files:
                    if filename.endswith('.txt'):
                        file_path = os.path.join(root, filename)
                        content = _read_file_content(file_path)
                        if content:
                            # Create a document ID from the path
                            rel_path = os.path.relpath(file_path, base_dir)
                            doc_id = rel_path.replace('/', '_').replace('\\', '_').replace('.txt', '')
                            # Extract title from filename (remove timestamp and ID)
                            # Format: 2025-08-07-23-01-27 Lesson 1A [223PAFH4ESDDYSLT].txt
                            title_match = re.search(r'\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}\s+(.+?)\s+\[', filename)
                            if title_match:
                                doc_title = title_match.group(1)
                            else:
                                doc_title = filename[:-4]  # Remove .txt
                            
                            tokens = _tokenize(content)
                            documents.append({
                                'document_id': doc_id,
                                'document_title': doc_title,
                                'file_path': file_path,
                                'content': content,
                                'content_type': content_type,
                                'relative_path': rel_path
                            })
                            tokenized_documents.append(tokens)
    
    return {
        'documents': documents,
        'tokenized_documents': tokenized_documents
    }


def _build_or_load_index(content_type: str) -> dict:
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


def search(
    content_type: Optional[str] = None,
    query: str = "",
    top_k: int = 5
) -> List[SearchResult]:
    """Find documents matching a query, ranked by relevance using BM25.
    
    Args:
        content_type: Content type to search ('docs', 'rtopro-help', 'otter', or None for all)
        query: Search query string
        top_k: Number of top results to return
        
    Returns:
        List of SearchResult objects sorted by relevance score (highest first)
    """
    if not query or not query.strip():
        return []
    
    content_types_to_search = [content_type] if content_type else get_content_types()
    
    all_results = []
    
    for ct in content_types_to_search:
        # Build or load index
        index_data = _build_or_load_index(ct)
        
        if not index_data['documents']:
            continue
        
        # Tokenize query
        query_tokens = _tokenize(query)
        
        if not query_tokens:
            continue
        
        # Score documents using BM25
        bm25 = BM25Okapi(index_data['tokenized_documents'])
        scores = bm25.get_scores(query_tokens)
        
        # Get top_k results for this content type
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        
        for idx in top_indices:
            if scores[idx] <= 0:
                continue
            
            doc_info = index_data['documents'][idx]
            # Read content from file if not in index (for cached indices)
            content = doc_info.get('content')
            if not content:
                content = _read_file_content(doc_info['file_path'])
            
            # Generate snippet
            snippet = _generate_snippet(content, query_tokens, max_words=150)
            
            all_results.append(SearchResult(
                document_id=doc_info['document_id'],
                document_title=doc_info['document_title'],
                file_path=doc_info['file_path'],
                content_type=doc_info['content_type'],
                score=float(scores[idx]),
                snippet=snippet
            ))
    
    # Sort all results by score and return top_k
    all_results.sort(key=lambda x: x.score, reverse=True)
    return all_results[:top_k]


def list_documents(
    content_type: Optional[str] = None,
    filter_name: Optional[str] = None,
    page: int = 1,
    page_size: int = 50
) -> Tuple[List[DocumentInfo], int]:
    """Return a list of all available documents.
    
    Args:
        content_type: Content type to list ('docs', 'rtopro-help', 'otter', or None for all)
        filter_name: Optional filter to match document names (case-insensitive substring)
        page: Page number (1-indexed). Defaults to 1.
        page_size: Number of documents per page. Defaults to 50.
        
    Returns:
        Tuple of (List of DocumentInfo objects, total count)
    """
    content_types_to_list = [content_type] if content_type else get_content_types()
    
    all_documents = []
    
    for ct in content_types_to_list:
        # Build or load index
        index_data = _build_or_load_index(ct)
        
        for doc_data in index_data['documents']:
            doc_title = doc_data['document_title']
            
            # Apply name filter if provided
            if filter_name and filter_name.lower() not in doc_title.lower():
                continue
            
            # Read file to get word count
            content = doc_data.get('content', '')
            if not content:
                content = _read_file_content(doc_data['file_path'])
            
            word_count = len(content.split())
            
            metadata = {
                'relative_path': doc_data.get('relative_path'),
            }
            
            all_documents.append(DocumentInfo(
                document_id=doc_data['document_id'],
                document_title=doc_title,
                file_path=doc_data['file_path'],
                content_type=doc_data['content_type'],
                word_count=word_count,
                metadata=metadata
            ))
    
    # Sort by title
    all_documents.sort(key=lambda x: x.document_title.lower())
    
    total_count = len(all_documents)
    
    # Apply pagination
    if page < 1:
        page = 1
    if page_size < 1:
        page_size = 50
    
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_documents = all_documents[start_idx:end_idx]
    
    return paginated_documents, total_count


def get_document(document_id: str, content_type: Optional[str] = None) -> Optional[DocumentInfo]:
    """Retrieve a specific document by ID.
    
    Args:
        document_id: Document ID to retrieve
        content_type: Content type to search in (optional, will search all if not provided)
        
    Returns:
        DocumentInfo object, or None if document not found
    """
    content_types_to_search = [content_type] if content_type else get_content_types()
    
    for ct in content_types_to_search:
        index_data = _build_or_load_index(ct)
        
        for doc_data in index_data['documents']:
            if doc_data['document_id'] == document_id:
                content = doc_data.get('content', '')
                if not content:
                    content = _read_file_content(doc_data['file_path'])
                
                word_count = len(content.split())
                
                metadata = {
                    'relative_path': doc_data.get('relative_path'),
                }
                
                return DocumentInfo(
                    document_id=doc_data['document_id'],
                    document_title=doc_data['document_title'],
                    file_path=doc_data['file_path'],
                    content_type=doc_data['content_type'],
                    word_count=word_count,
                    metadata=metadata
                )
    
    return None


def rebuild_index(content_type: Optional[str] = None) -> dict:
    """Force rebuild of search index.
    
    Args:
        content_type: Content type to rebuild ('docs', 'rtopro-help', 'otter', or None for all)
        
    Returns:
        dict with counts of documents indexed
    """
    content_types_to_rebuild = [content_type] if content_type else get_content_types()
    
    results = {}
    
    for ct in content_types_to_rebuild:
        index_file = _get_index_file(ct)
        if os.path.exists(index_file):
            os.remove(index_file)
        
        index_data = _build_or_load_index(ct)
        results[ct] = len(index_data['documents'])
    
    return results
