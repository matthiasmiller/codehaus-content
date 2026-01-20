# How to Set CODEHAUS_CONTENT_ROOT_DIR and Run the MCP Server

## Option 1: Using the Shell Script (Easiest)

The `setup_and_run_mcp.sh` script automatically sets the environment variable:

```bash
cd /Users/matthiasmiller/Documents/GitHub/codehaus-content
./setup_and_run_mcp.sh
```

## Option 2: Manual Setup in Terminal

### macOS/Linux (bash/zsh):

```bash
# Set the environment variable
export CODEHAUS_CONTENT_ROOT_DIR="/Users/matthiasmiller/Documents/GitHub/codehaus-content"

# Run the script
python3 claude_mcp_extension/find_project_and_run.py
```

### Or in one line:

```bash
CODEHAUS_CONTENT_ROOT_DIR="/Users/matthiasmiller/Documents/GitHub/codehaus-content" python3 claude_mcp_extension/find_project_and_run.py
```

### Windows (PowerShell):

```powershell
$env:CODEHAUS_CONTENT_ROOT_DIR = "C:\Users\matthiasmiller\Documents\GitHub\codehaus-content"
python claude_mcp_extension\find_project_and_run.py
```

### Windows (Command Prompt):

```cmd
set CODEHAUS_CONTENT_ROOT_DIR=C:\Users\matthiasmiller\Documents\GitHub\codehaus-content
python claude_mcp_extension\find_project_and_run.py
```

## Option 3: Create a Test Script

Create a file called `test_mcp.sh`:

```bash
#!/bin/bash
export CODEHAUS_CONTENT_ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 claude_mcp_extension/find_project_and_run.py
```

Then run:
```bash
chmod +x test_mcp.sh
./test_mcp.sh
```

## What the Script Does

1. Checks that `CODEHAUS_CONTENT_ROOT_DIR` is set
2. Creates a `.venv` virtual environment if it doesn't exist
3. Installs dependencies (`mcp`, `rank-bm25`) from `codehaus_mcp/requirements.txt`
4. Runs the MCP server using the venv Python

## Troubleshooting

If you get permission errors creating the venv, try:
```bash
python3 -m venv .venv
```

Then run the script again - it will use the existing venv.

## For Claude Desktop

When using with Claude Desktop, the `manifest.json` file automatically sets the environment variable. You just need to point Claude Desktop to the `claude_mcp_extension` directory.
