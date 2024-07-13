#!/bin/bash

# Change directory to the project folder
cd /root/mlh-portfolio/
pwd

# Ensure the git repository has the latest changes
git fetch && git reset origin/main --hard

# Enter the python virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Restart myportfolio system service
systemctl restart myportfolio
