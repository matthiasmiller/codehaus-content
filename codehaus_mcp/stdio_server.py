"""MCP stdio server for Claude Desktop.

This is a standalone stdio-based MCP server that can be used with Claude Desktop.
It provides search and retrieval tools for codehaus-content repository.

Usage:
    python -m codehaus_mcp.stdio_server
    
Or configure in Claude Desktop's claude_desktop_config.json:
    {
      "mcpServers": {
        "codehaus-content": {
          "command": "python",
          "args": ["-m", "codehaus_mcp.stdio_server"]
        }
      }
    }
"""

import json
import os
import sys
import traceback
from typing import Optional

from mcp.server.fastmcp import FastMCP

from .content_util import (
    get_content_types,
)
from .content_search import (
    list_documents,
    search,
    get_document,
    rebuild_index,
)


# Use FastMCP if available (newer SDK)
mcp = FastMCP("Codehaus Content Server")


# Tool: content_search
@mcp.tool()
def content_search_tool(
    content_type: Optional[str] = None,
    query: str = "",
    top_k: int = 5
) -> dict:
    """Search for documents matching a query using BM25 ranking.
    
    Args:
        content_type: Content type to search ('docs', 'rtopro-help', 'otter', or None for all)
        query: Search query string
        top_k: Number of results to return (default: 5)
    """
    if not query:
        return {"error": "query parameter is required"}
    
    try:
        results = search(content_type=content_type, query=query, top_k=top_k)
        
        result_list = []
        for res in results:
            result_list.append({
                'document_id': res.document_id,
                'document_title': res.document_title,
                'file_path': res.file_path,
                'content_type': res.content_type,
                'score': res.score,
                'snippet': res.snippet,
            })
        
        return result_list
    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }


# Tool: content_get_document
@mcp.tool()
def content_get_document_tool(
    document_id: str = "",
    content_type: Optional[str] = None
) -> str:
    """Retrieve full content of a specific document.
    
    Args:
        document_id: Document ID to retrieve
        content_type: Content type to search in (optional, will search all if not provided)
    """
    if not document_id:
        return "Error: document_id parameter is required"
    
    try:
        doc = get_document(document_id, content_type=content_type)
        
        if not doc:
            return f"Error: Document {document_id} not found"
        
        # Read the full content
        with open(doc.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content_parts = [
            f"# {doc.document_title}",
            f"**Content Type:** {doc.content_type}",
            f"**Document ID:** {doc.document_id}",
            f"**File Path:** {doc.file_path}",
            f"**Word Count:** {doc.word_count}",
            "",
            content,
        ]
        
        return '\n'.join(content_parts)
    except Exception as e:
        return f"Error: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"


# Tool: content_list_documents
@mcp.tool()
def content_list_documents_tool(
    content_type: Optional[str] = None,
    filter: Optional[str] = None,
    page: int = 1,
    page_size: int = 50
) -> dict:
    """List all documents.
    
    Args:
        content_type: Content type to list ('docs', 'rtopro-help', 'otter', or None for all)
        filter: Optional filter to match document names (case-insensitive substring)
        page: Page number (1-indexed). Defaults to 1.
        page_size: Number of documents per page. Defaults to 50.
    """
    try:
        documents, total_count = list_documents(
            content_type=content_type,
            filter_name=filter,
            page=page,
            page_size=page_size
        )
        
        result_list = []
        for doc in documents:
            result_list.append({
                'document_id': doc.document_id,
                'document_title': doc.document_title,
                'file_path': doc.file_path,
                'content_type': doc.content_type,
                'word_count': doc.word_count,
            })
        
        if page_size < 1:
            page_size = 50
        total_pages = (total_count + page_size - 1) // page_size if total_count > 0 else 0
        
        response = {
            'documents': result_list,
            'total': total_count,
            'pagination': {
                'page': page,
                'page_size': page_size,
                'total_pages': total_pages,
                'has_next': page < total_pages if total_pages > 0 else False,
                'has_previous': page > 1,
            }
        }
        
        return response
    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }


# Tool: content_rebuild_index
@mcp.tool()
def content_rebuild_index_tool(content_type: Optional[str] = None) -> dict:
    """Force rebuild of the search index.
    
    This operation can be resource-intensive.
    
    Args:
        content_type: Content type to rebuild ('docs', 'rtopro-help', 'otter', or None for all)
    """
    try:
        results = rebuild_index(content_type=content_type)
        
        return {
            'content_types': list(results.keys()),
            'counts': results,
            'message': f'Search index rebuilt for: {", ".join(results.keys())}',
        }
    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }


# Tool: content_list_types
@mcp.tool()
def content_list_types_tool() -> dict:
    """List all available content types."""
    try:
        types = get_content_types()
        return {
            'content_types': types,
            'message': f'Available content types: {", ".join(types)}',
        }
    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }


if __name__ == "__main__":
    # FastMCP runs automatically
    mcp.run()
