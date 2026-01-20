#!/usr/bin/env python3
"""Entry point script for running the MCP stdio server.

This script can be used directly by Claude Desktop or run standalone.
It ensures the correct Python path is set up.
"""

import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now import and run the stdio server
if __name__ == "__main__":
    # Import the stdio_server module
    # We need to execute it as if it were run directly
    import runpy
    stdio_server_path = os.path.join(os.path.dirname(__file__), "stdio_server.py")
    # Run the module as __main__ so its __main__ block executes
    runpy.run_path(stdio_server_path, run_name="__main__")
