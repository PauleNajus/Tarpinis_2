#!/bin/bash

set -e

# Navigate to the application directory
cd /home/site/wwwroot

# Logging to help debug
echo "Checking for virtual environment..."

# Check if the virtual environment exists, create it if it doesn't
if [ ! -d "antenv" ]; then
  echo "Creating virtual environment..."
  python -m venv antenv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source antenv/bin/activate

# Upgrade pip and install dependencies
echo "Upgrading pip and installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
flask db upgrade

# Initialize admin user
echo "Initializing admin user..."
python -c "from app import init_admin_user; init_admin_user()"

# Start the application
echo "Starting the application..."
flask run --host=0.0.0.0 --port=8000
