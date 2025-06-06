#!/bin/bash
# Activate the virtual environment
source ../.venv/bin/activate

# Change to the project root directory
cd ../

# Run the HIDS main script
nohup python3 main.py > hids.log 2>&1 &