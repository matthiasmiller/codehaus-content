#!/usr/bin/env python3
"""Update client proposals from the source system.

Downloads proposal data from the source system and stores it in a structured
filesystem format with metadata tracking for rename detection.

This follows the same pattern as update_database_rag in infinite-stairway-designer.

Migrated from /Users/matthiasmiller/Documents/GitHub/infinite-stairway-designer/isd_mcp/chat_util.py
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


def _get_max_content_version_from_metadata(metadata):
    """Get the maximum content version from metadata across all proposals and sections.
    
    Args:
        metadata: Metadata dict with structure:
            {proposals: {ProposalID: {sections: {SectionID: {last_contents_version: ...}}}}}
    
    Returns:
        Maximum content version (int or None if no versions found)
    """
    max_version = None
    
    if 'proposals' not in metadata:
        return None
    
    for proposal_id, prop_meta in metadata['proposals'].items():
        if 'sections' not in prop_meta:
            continue
        for section_id, section_meta in prop_meta['sections'].items():
            version = section_meta.get('last_contents_version')
            if version is not None:
                if max_version is None or version > max_version:
                    max_version = version
    
    return max_version


def update_client_proposals():
    """Download and process client proposals from the source system.
    
    Downloads proposal and section data from the source system and stores it
    in a structured filesystem format with metadata tracking for rename detection.
    
    Data Source:
        Fetches data from report: User/Personal/Matthias.Miller/Blueprint_Designer/Service_Export_Proposals.r20
    
    Input Fields (from JSON response):
        DocumentID: Unique identifier for the proposal
        DocumentName: Display name of the proposal (may change over time)
        SectionID: Unique identifier for the section
        SectionName: Display name of the section (may change over time)
        SectionOrder: Sorting order for sections within a proposal
        ContentsVersion: Version number for content changes
        ContentsChanged: Boolean indicating if content has changed
        ContentsHTMLIfChanged: HTML content (only present if ContentsChanged is True)
    
    Output Structure:
        client-proposals/{CleanProposalTitle} [{ProposalID}]/{CleanSectionTitle} [{SectionID}].md
        
        Where:
        - Each proposal gets its own folder named {CleanProposalTitle} [{ProposalID}]
        - Each section is saved as {CleanSectionTitle} [{SectionID}].md inside the folder
        - Uses the same "basename [ID]" format as otter files
        - Folder and file names are cleaned for filesystem compatibility
    
    Processing Logic:
        - Rename the folder if the DocumentName changes (tracks via metadata)
        - Rename the file if the SectionName changes (tracks via metadata)
        - Save content if ContentsChanged is True OR if file doesn't exist yet
        - Convert HTML to markdown before saving
        - Save metadata for tracking renames and content versions
    """
    if not invwebservices or not ZCH_ARGS:
        print("Error: Client connection not available. Please set up invwebservices and ZCH_ARGS.")
        return
    
    proposals_dir = _get_client_proposals_dir()
    metadata_file = _get_metadata_file_path()
    metadata = _load_metadata(metadata_file)
    
    if 'proposals' not in metadata:
        metadata['proposals'] = {}
    
    # Get max content version from metadata for incremental update
    last_content_version = _get_max_content_version_from_metadata(metadata)
    
    print(f'Fetching client proposals (last version: {last_content_version})...')
    client = invwebservices.Client(**ZCH_ARGS)
    response = client.get(
        'Report',
        'User/Personal/Matthias.Miller/RAG/2026-01-16_First_Version.r20',
        {
            'Prompt.vLastContentVersion': last_content_version
        }
    )
    response_content = response.content
    
    if 'data' not in response_content:
        print('Error: No data in response')
        return
    
    rows = response_content['data']
    
    for row in rows:
        proposal_id = str(row.get('DocumentID', ''))
        proposal_name = row.get('DocumentName', '')
        section_id = str(row.get('SectionID', ''))
        section_name = row.get('SectionName', '')
        section_order = row.get('SectionOrder')
        contents_version = row.get('ContentsVersion')
        contents_changed = row.get('ContentsChanged', False)
        contents_html_if_changed = row.get('ContentsHTMLIfChanged', '')
        
        if not proposal_id or not section_id:
            print(f'Warning: Skipping row with missing ID: Proposal={proposal_id}, Section={section_id}')
            continue
        
        # Clean names for filesystem use
        clean_proposal_name = content_util.clean_filename(proposal_name)
        clean_section_name = content_util.clean_filename(section_name)
        
        # Determine folder name (using "DocumentTitle [DocumentID]" format)
        folder_name = f'{clean_proposal_name} [{proposal_id}]'
        folder_path = os.path.join(proposals_dir, folder_name)
        
        # Determine file name (using "SectionTitle [SectionID].md" format)
        file_name = f'{clean_section_name} [{section_id}].md'
        file_path = os.path.join(folder_path, file_name)
        
        # Get or create proposal metadata
        if proposal_id not in metadata['proposals']:
            metadata['proposals'][proposal_id] = {
                'current_folder_name': None,
                'last_proposal_name': None,
                'sections': {}
            }
        
        prop_meta = metadata['proposals'][proposal_id]
        
        # Check if proposal name changed and rename folder if needed
        if prop_meta['current_folder_name'] and prop_meta['last_proposal_name'] != proposal_name:
            old_folder_path = os.path.join(proposals_dir, prop_meta['current_folder_name'])
            if os.path.exists(old_folder_path) and not os.path.exists(folder_path):
                print(f'Renaming proposal folder: {prop_meta["current_folder_name"]} -> {folder_name}')
                os.rename(old_folder_path, folder_path)
        
        # Update proposal metadata
        prop_meta['current_folder_name'] = folder_name
        prop_meta['last_proposal_name'] = proposal_name
        
        # Ensure folder exists
        os.makedirs(folder_path, exist_ok=True)
        
        # Get or create section metadata
        if 'sections' not in prop_meta:
            prop_meta['sections'] = {}
            
        if section_id not in prop_meta['sections']:
            prop_meta['sections'][section_id] = {
                'current_file_name': None,
                'last_section_name': None,
                'last_contents_version': None,
                'section_order': None
            }
        
        section_meta = prop_meta['sections'][section_id]
        
        # Check if section name changed and rename file if needed
        if section_meta['current_file_name'] and section_meta['last_section_name'] != section_name:
            old_file_path = os.path.join(folder_path, section_meta['current_file_name'])
            if os.path.exists(old_file_path) and not os.path.exists(file_path):
                print(f'Renaming section file: {section_meta["current_file_name"]} -> {file_name}')
                os.rename(old_file_path, file_path)
        
        # Update section metadata
        section_meta['current_file_name'] = file_name
        section_meta['last_section_name'] = section_name
        section_meta['last_contents_version'] = contents_version
        if section_order is not None:
            section_meta['section_order'] = section_order
        
        # Save content if changed or missing
        if contents_changed or not os.path.exists(file_path):
            markdown_content = _html_to_markdown(contents_html_if_changed)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f'Saved section: {folder_name}/{file_name}')
    
    # Save updated metadata
    _save_metadata(metadata_file, metadata)
    print(f'Updated metadata: {metadata_file}')
    print(f'Finished processing proposals in {proposals_dir}')



if __name__ == '__main__':
    update_client_proposals()
