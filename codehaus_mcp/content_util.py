"""Content search and retrieval utilities for codehaus-content.

This module provides functions to search and retrieve content from:
- Markdown documentation files (infinite-stairway-designer/docs/ and rtopro-help/)
- Transcript files (otter/)
"""

import os
import re
from dataclasses import dataclass
from typing import List, Optional, Tuple


def get_content_types():
    """Get list of available content types."""
    return ['docs', 'rtopro-help', 'otter', 'client-proposals']


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


def _get_client_proposals_dir():
    """Get the client-proposals directory path."""
    root = get_project_root()
    return os.path.join(root, 'client-proposals')


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
    
    # Brackets have special meaning to designate IDs.
    cleaned = cleaned.replace('[', '(')
    cleaned = cleaned.replace(']', ')')

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


def read_file_content(file_path: str) -> str:
    """Read file content with proper error handling."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
