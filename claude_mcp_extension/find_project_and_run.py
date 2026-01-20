#!/usr/bin/env python3
"""
Script to find the project root using CODEHAUS_CONTENT_ROOT_DIR and run the MCP server.
This replaces shell scripts to avoid macOS Gatekeeper signature issues.
"""
import os
import sys
import subprocess
from pathlib import Path


def main():
    # Check if CODEHAUS_CONTENT_ROOT_DIR is set
    root_dir = os.environ.get("CODEHAUS_CONTENT_ROOT_DIR")
    if not root_dir:
        print("Error: CODEHAUS_CONTENT_ROOT_DIR environment variable is not set.", file=sys.stderr)
        sys.exit(1)
    
    # Check if the directory exists
    project_root = Path(root_dir)
    if not project_root.is_dir():
        print(f"Error: CODEHAUS_CONTENT_ROOT_DIR directory does not exist: {root_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Set up venv and install requirements
    venv_dir = project_root / ".venv"
    
    # Create venv if it doesn't exist
    if not venv_dir.is_dir():
        print(f"Creating virtual environment at {venv_dir}...", file=sys.stderr)
        subprocess.run(
            [sys.executable, "-m", "venv", str(venv_dir)],
            check=True,
            stderr=sys.stderr
        )
    
    # Install MCP requirements (suppress output to stderr to avoid breaking MCP JSON protocol)
    pip_exe = venv_dir / "bin" / "pip"
    requirements_file = project_root / "codehaus_mcp" / "requirements.txt"
    
    if requirements_file.exists():
        subprocess.run(
            [str(pip_exe), "install", "--quiet", "--disable-pip-version-check", 
                "-r", str(requirements_file)],
            check=False,  # Don't fail if requirements already installed
            stderr=sys.stderr
        )
    else:
        # Fallback: install directly
        subprocess.run(
            [str(pip_exe), "install", "--quiet", "--disable-pip-version-check", 
                "mcp", "rank-bm25"],
            check=False,
            stderr=sys.stderr
        )
    
    # Run the MCP server using the project's venv Python
    python_exe = venv_dir / "bin" / "python3"
    
    # Add the project root to PYTHONPATH so imports work
    pythonpath = os.environ.get("PYTHONPATH", "")
    if pythonpath:
        os.environ["PYTHONPATH"] = f"{project_root}:{pythonpath}"
    else:
        os.environ["PYTHONPATH"] = str(project_root)
    
    # Change to project root directory
    os.chdir(project_root)
    
    # Run the server - stdout must be clean for MCP JSON-RPC protocol
    # Use exec to replace this process
    os.execv(str(python_exe), [str(python_exe), "-m", "codehaus_mcp.stdio_server"])


if __name__ == "__main__":
    main()
