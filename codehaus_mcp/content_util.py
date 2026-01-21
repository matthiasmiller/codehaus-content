"""Content search and retrieval utilities for codehaus-content.

This module provides functions to search and retrieve content from:
- Markdown documentation files (infinite-stairway-designer/docs/ and rtopro-help/)
- Transcript files (otter/)
"""

import os
import re
from dataclasses import dataclass
from typing import List, Optional, Tuple

from rank_bm25 import BM25Okapi

from . import content_index


def get_content_types():
    """Get list of available content types."""
    return ['docs', 'rtopro-help', 'otter']


def get_project_root():
    """Get the project root directory.
    
    Returns:
        Path to the project root directory (parent of codehaus_mcp/)
    """
    # This file is in codehaus_mcp/, so go up one level
    this_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(this_dir)
    return root_dir


def _get_docs_dir():
    """Get the docs directory path."""
    root = get_project_root()
    return os.path.join(root, 'infinite-stairway-designer', 'docs')


def _get_rtopro_help_dir():
    """Get the rtopro-help directory path."""
    root = get_project_root()
    return os.path.join(root, 'rtopro-help')


def _get_otter_dir():
    """Get the otter directory path."""
    root = get_project_root()
    return os.path.join(root, 'otter')


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


def clean_filename(name: str) -> str:
    """Clean a name for use in filesystem paths.
    
    Removes or replaces invalid characters, limits length, and handles edge cases.
    
    Args:
        name: Name to clean
        
    Returns:
        Cleaned name safe for filesystem use
    """
    if not name:
        return 'unnamed'
    
    # Replace invalid filesystem characters with underscores
    invalid_chars = '<>:"/\\|?*'
    cleaned = name
    for char in invalid_chars:
        cleaned = cleaned.replace(char, '_')
    
    # Remove leading/trailing dots and spaces (Windows issue)
    cleaned = cleaned.strip('. ')
    
    # Limit length to avoid filesystem issues
    max_length = 200
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length]
    
    # Ensure it's not empty after cleaning
    if not cleaned:
        return 'unnamed'
    
    return cleaned


def get_cache_dir(subdirectory: str = 'codehaus_mcp') -> str:
    """Get a cache directory path.
    
    Args:
        subdirectory: Subdirectory name within .cache (default: 'codehaus_mcp')
        
    Returns:
        Path to the cache directory (created if it doesn't exist)
    """
    root = get_project_root()
    cache_dir = os.path.join(root, '.cache', subdirectory)
    os.makedirs(cache_dir, exist_ok=True)
    return cache_dir


def _read_file_content(file_path: str) -> str:
    """Read file content with proper error handling."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


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
        index_data = content_index.build_or_load_index(ct)
        
        if not index_data['documents']:
            continue
        
        # Tokenize query
        query_tokens = content_index.tokenize(query)
        
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
        index_data = content_index.build_or_load_index(ct)
        
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
        index_data = content_index.build_or_load_index(ct)
        
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
