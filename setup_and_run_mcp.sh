#!/usr/bin/env bash
# Set CODEHAUS_CONTENT_ROOT_DIR to the directory where this script is located (project root)
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
export CODEHAUS_CONTENT_ROOT_DIR="$SRC_DIR"

# Run the Python script that handles venv setup and MCP server startup
python3 "$SRC_DIR/claude_mcp_extension/find_project_and_run.py"
