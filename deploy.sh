#!/bin/bash

# Navigate to the application directory
cd /home/site/wwwroot

# Check if the virtual environment exists, create it if it doesn't
if [ ! -d "antenv" ]; then
  python -m venv antenv
fi

# Activate the virtual environment
source antenv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run database migrations
flask db upgrade

# Initialize admin user
python -c "from app import init_admin_user; init_admin_user()"

# Start the application
flask run --host=0.0.0.0 --port=8000
