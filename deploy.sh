#!/bin/bash

set -e

# Navigate to the application directory
cd /home/site/wwwroot

# Logging to help debug
echo "Running database migrations..."

# Run database migrations
flask db upgrade

echo "Initializing admin user..."

# Initialize admin user
python -c "from app import init_admin_user; init_admin_user()"

echo "Starting the application..."

# Start the application
flask run --host=0.0.0.0 --port=8000