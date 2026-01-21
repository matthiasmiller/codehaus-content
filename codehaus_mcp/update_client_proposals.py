#!/usr/bin/env python3
"""Update client proposals from the source system.

Downloads proposal data from the source system and stores it in a structured
filesystem format with metadata tracking for rename detection.

This follows the same pattern as update_database_rag in infinite-stairway-designer.
"""

import json
import os
from pathlib import Path

import html2text

import content_util

# Try to import the client - adjust path as needed
import invwebservices
from _conf import ZCH_ARGS


def _get_client_proposals_dir():
    """Get the client-proposals directory path."""
    root = content_util.get_project_root()
    proposals_dir = os.path.join(root, 'client-proposals')
    os.makedirs(proposals_dir, exist_ok=True)
    return proposals_dir


def _get_metadata_file_path():
    """Get the metadata file path."""
    cache_dir = content_util.get_cache_dir('client-proposals')
    return os.path.join(cache_dir, 'proposals_metadata.json')


def _html_to_markdown(html_content):
    """Convert HTML content to markdown.
    
    Args:
        html_content: HTML string to convert
        
    Returns:
        Markdown string
    """
    if not html_content:
        return ''
    
    # Configure html2text converter
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Don't wrap lines
    h.unicode_snob = True  # Use unicode characters
    
    # Convert HTML to markdown
    markdown = h.handle(html_content)
    
    return markdown


def _load_metadata(metadata_file):
    """Load metadata from JSON file.
    
    Returns empty dict if file doesn't exist or is invalid.
    """
    if not os.path.exists(metadata_file):
        return {}
    
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print(f'Warning: Could not load metadata from {metadata_file}, using empty metadata')
        return {}


def _save_metadata(metadata_file, metadata):
    """Save metadata to JSON file."""
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)


def update_client_proposals():
    """Download and process client proposals from the source system.
    
    Downloads proposal data from the source system and stores it
    in a structured filesystem format with metadata tracking for rename detection.
    
    Data Source:
        Fetches data from report: User/Personal/Matthias.Miller/Blueprint_Designer/Service_Export_Proposals.r20
    
    Input Fields (from JSON response):
        id: Unique identifier for the proposal
        name: Display name of the proposal (may change over time)
        html: HTML content of the proposal
    
    Output Structure:
        client-proposals/{ProposalID}-{CleanProposalTitle}/{CleanProposalName} [{ProposalID}].md
        
        Where:
        - Each proposal gets its own folder named {ProposalID}-{CleanProposalTitle}
        - The proposal content is saved as {CleanProposalName} [{ProposalID}].md inside the folder
        - Uses the same "basename [ID]" format as otter files
        - Folder and file names are cleaned for filesystem compatibility
    
    Processing Logic:
        - Rename the folder if the proposal name changes (tracks via metadata)
        - Convert HTML to markdown before saving
        - Save metadata for tracking renames
    """
    if not invwebservices or not ZCH_ARGS:
        print("Error: Client connection not available. Please set up invwebservices and ZCH_ARGS.")
        return
    
    proposals_dir = _get_client_proposals_dir()
    metadata_file = _get_metadata_file_path()
    metadata = _load_metadata(metadata_file)
    
    if 'proposals' not in metadata:
        metadata['proposals'] = {}
    
    print('Fetching client proposals...')
    client = invwebservices.Client(**ZCH_ARGS)
    response = client.get(
        'Report',
        'User/Personal/Matthias.Miller/Blueprint_Designer/Service_Export_Proposals.r20'
    )
    response_content = response.content
    
    if 'data' not in response_content:
        print('Error: No data in response')
        return
    
    proposals = response_content['data']
    
    for proposal in proposals:
        proposal_id = str(proposal.get('id', ''))
        proposal_name = proposal.get('name', '')
        proposal_html = proposal.get('html', '')
        
        if not proposal_id:
            print(f'Warning: Skipping proposal with no ID: {proposal_name}')
            continue
        
        # Clean the name for filesystem use
        clean_name = content_util.clean_filename(proposal_name)
        
        # Determine folder name (using "DocumentTitle [DocumentID]" format)
        folder_name = f'{clean_name} [{proposal_id}]'
        folder_path = os.path.join(proposals_dir, folder_name)
        
        # Determine file name (using "DocumentTitle [DocumentID].md" format)
        file_name = f'{clean_name} [{proposal_id}].md'
        file_path = os.path.join(folder_path, file_name)
        
        # Get or create proposal metadata
        if proposal_id not in metadata['proposals']:
            metadata['proposals'][proposal_id] = {
                'current_folder_name': None,
                'current_file_name': None,
                'last_proposal_name': None
            }
        
        proposal_meta = metadata['proposals'][proposal_id]
        
        # Check if proposal name changed and rename folder if needed
        if proposal_meta['current_folder_name'] and proposal_meta['last_proposal_name'] != proposal_name:
            old_folder_path = os.path.join(proposals_dir, proposal_meta['current_folder_name'])
            if os.path.exists(old_folder_path) and not os.path.exists(folder_path):
                print(f'Renaming proposal folder: {proposal_meta["current_folder_name"]} -> {folder_name}')
                os.rename(old_folder_path, folder_path)
        
        # Check if file name changed and rename file if needed
        if proposal_meta['current_file_name'] and proposal_meta['current_file_name'] != file_name:
            old_file_path = os.path.join(folder_path, proposal_meta['current_file_name'])
            if os.path.exists(old_file_path) and not os.path.exists(file_path):
                print(f'Renaming proposal file: {proposal_meta["current_file_name"]} -> {file_name}')
                os.rename(old_file_path, file_path)
        
        # Update proposal metadata
        proposal_meta['current_folder_name'] = folder_name
        proposal_meta['current_file_name'] = file_name
        proposal_meta['last_proposal_name'] = proposal_name
        
        # Create proposal folder
        os.makedirs(folder_path, exist_ok=True)
        
        # Convert HTML to markdown and save
        markdown_content = _html_to_markdown(proposal_html)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f'Saved proposal: {folder_name}/{file_name}')
    
    # Save updated metadata
    _save_metadata(metadata_file, metadata)
    print(f'Updated metadata: {metadata_file}')
    print(f'Updated {len(proposals)} proposals in {proposals_dir}')


if __name__ == '__main__':
    update_client_proposals()
