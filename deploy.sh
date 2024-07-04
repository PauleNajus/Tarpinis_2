#!/bin/bash

# Navigate to the directory where the application is
cd /home/site/wwwroot

# Set up the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run database migrations
flask db upgrade

# Start the Flask app
gunicorn -w 4 -b 0.0.0.0:8000 app:app
