# MCP Server for Claude Desktop

This directory contains an MCP (Model Context Protocol) server that provides search and retrieval tools for the codehaus-content repository, including:

- Documentation files (markdown) in `infinite-stairway-designer/docs/` and `rtopro-help/`
- Transcript files (text) in `otter/`

## Overview

The MCP server exposes the following tools:
- **content_search**: Search for documents matching a query using BM25 ranking
- **content_get_document**: Retrieve full content of a specific document
- **content_list_documents**: List all documents with pagination
- **content_list_types**: List all available content types
- **content_rebuild_index**: Force rebuild of the search index

## Installation

1. Set up a virtual environment (if not already done):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install MCP-specific dependencies:
   ```bash
   pip install -r codehaus_mcp/requirements.txt
   ```
   
   Or install directly:
   ```bash
   pip install mcp rank-bm25
   ```

## Configuration

The server can be configured in Claude Desktop's configuration file.

## Setting up Claude Desktop

### Option 1: MCP Bundle (Recommended - Unpacked Extension)

If you're using Claude Desktop's MCP Bundle format (unpacked extension):

1. Point Claude Desktop to the `claude_mcp_extension` directory containing `manifest.json`
2. The `manifest.json` file defines the server configuration
3. The `find_project_and_run.py` script will automatically:
   - Find your project root (set via `CODEHAUS_CONTENT_ROOT_DIR` environment variable)
   - Use your existing `.venv` virtual environment (creates one if needed)
   - Install MCP dependencies (`mcp`, `rank-bm25`) if needed
   - Run the server using the project's venv Python
4. Claude Desktop will read the manifest and configure the server automatically

**Configuration:**
- The default root directory is set in `manifest.json` as `/Users/matthiasmiller/Documents/GitHub/codehaus-content`
- You can change this in Claude Desktop's MCP settings if needed
- The script uses your existing project venv, so make sure you've set up a virtual environment or let it create one automatically

### Option 2: Manual Configuration

1. Locate your Claude Desktop configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. Add the MCP server configuration:

   ```json
   {
     "mcpServers": {
       "codehaus-content": {
         "command": "python",
         "args": [
           "/absolute/path/to/codehaus-content/codehaus_mcp/stdio_server.py"
         ]
       }
     }
   }
   ```

   **Or use the entry point script** (optional wrapper):
   ```json
   {
     "mcpServers": {
       "codehaus-content": {
         "command": "python",
         "args": [
           "/absolute/path/to/codehaus-content/codehaus_mcp/run_stdio_server.py"
         ]
       }
     }
   }
   ```

   **Or use the find-and-run script** (recommended for automatic venv setup):
   ```json
   {
     "mcpServers": {
       "codehaus-content": {
         "command": "python3",
         "args": [
           "/absolute/path/to/codehaus-content/claude_mcp_extension/find_project_and_run.py"
         ],
         "env": {
           "CODEHAUS_CONTENT_ROOT_DIR": "/absolute/path/to/codehaus-content"
         }
       }
     }
   }
   ```

   **Important Notes:**
   - Use the **absolute path** to the script
   - Make sure the `python` command points to the correct Python interpreter (you may need to use the full path, e.g., `/usr/local/bin/python3` or the path to your virtual environment's Python)
   - On macOS/Linux, you may need to make the script executable: `chmod +x codehaus_mcp/stdio_server.py`
   - **You can point directly to `stdio_server.py`** - it handles its own path setup, so `run_stdio_server.py` is optional
   - The `find_project_and_run.py` script automatically sets up venv and installs dependencies

3. Restart Claude Desktop completely (quit and reopen the application)

## Testing

You can test the server manually:

```bash
# Point directly to stdio_server.py
python codehaus_mcp/stdio_server.py
```

Or using the entry point script (optional):

```bash
python codehaus_mcp/run_stdio_server.py
```

## Content Types

The server supports three content types:

1. **docs**: Markdown documentation files in `infinite-stairway-designer/docs/`
2. **rtopro-help**: Markdown help files in `rtopro-help/`
3. **otter**: Transcript files (text) in `otter/` directory structure

## Usage Examples

### Search across all content types
```
content_search(query="accounting loan", top_k=5)
```

### Search in specific content type
```
content_search(content_type="docs", query="accounting", top_k=3)
```

### List documents
```
content_list_documents(content_type="otter", page=1, page_size=20)
```

### Get a specific document
```
content_get_document(document_id="matthias_miller___accounting_loan")
```

### Rebuild search index
```
content_rebuild_index(content_type="docs")
```

## Troubleshooting

### Server doesn't appear in Claude Desktop

1. Check that the path to the script is absolute and correct
2. Verify that Python can be found (use full path to Python if needed)
3. Check Claude Desktop's logs for errors
4. Ensure all dependencies are installed: `pip install -r codehaus_mcp/requirements.txt`

### Import errors

If you see import errors, make sure:
- You're running from the project root or have the project in your Python path
- All dependencies in `requirements.txt` are installed
- The virtual environment is activated if you're using one

### No search results

- Verify that content files exist in the expected directories
- Try rebuilding the index using the `content_rebuild_index` tool
- Check that the file paths are correct

## Index Caching

The server builds and caches search indices in `.cache/codehaus_mcp/` directory. These indices are automatically rebuilt when needed, but you can force a rebuild using the `content_rebuild_index` tool.
