"""Content search and retrieval logic for codehaus-content.

This module implements the search, listing, and document retrieval logic,
separating it from the low-level utilities and indexing.
"""

from typing import List, Optional, Tuple
from rank_bm25 import BM25Okapi

from . import content_index
from .content_util import (
    get_content_types,
    read_file_content,
    DocumentInfo,
    SearchResult
)


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
                content = read_file_content(doc_info['file_path'])
            
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
                content = read_file_content(doc_data['file_path'])
            
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
                    content = read_file_content(doc_data['file_path'])
                
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
    return content_index.rebuild_index(content_type)
