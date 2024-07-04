#!/bin/bash

# Navigate to the application directory
cd /home/site/wwwroot

# Activate the virtual environment
source venv/bin/activate

# Run database migrations
flask db upgrade

# Start the application
gunicorn -w 4 -b 0.0.0.0:8000 app:app
