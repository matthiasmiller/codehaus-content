#/usr/bin/env bash
SRC_DIR=$(dirname "$0")
VENV_DIR=$SRC_DIR/.venv

[ -d "$VENV_DIR" ] || python3 -m venv "$VENV_DIR"
"$VENV_DIR/bin/pip" install -r "$SRC_DIR/requirements.txt"
cd "$SRC_DIR"

"$VENV_DIR/bin/python3" "$@"
