#!/bin/bash

# 1. Activate the Virtual Environment
# This command works for standard Linux/MacOS CI environments.
# (On Windows git-bash, this path might differ, but this is the standard for CI)
source .venv/Scripts/activate

# 2. Run the Test Suite
# We capture the exit code of pytest into a variable named 'exit_code'
pytest
exit_code=$?

# 3. Check Result and Return Correct Exit Code
if [ $exit_code -eq 0 ]; then
    echo "Tests passed successfully."
    exit 0
else
    echo "Tests failed."
    exit 1
fi