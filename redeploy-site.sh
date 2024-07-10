#!/bin/bash

# Kill all existing tmux sessions
tmux kill-server

# Change directory to the project folder
cd /root/mlh-portfolio/
pwd

# Ensure the git repository has the latest changes
git fetch && git reset origin/main --hard

# Enter the python virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Start a new detached Tmux session that starts the Flask server
tmux new-session -d -s portfolio 'flask run --host=0.0.0.0'
