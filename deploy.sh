#!/bin/bash

set -e

# Navigate to the application directory
cd /home/site/wwwroot

# Run database migrations
echo "Running database migrations..."
flask db upgrade

# Initialize admin user
echo "Initializing admin user..."
python -c "from app import init_admin_user; init_admin_user()"

# Start the application
echo "Starting the application..."
gunicorn -w 4 -b 0.0.0.0:8000 app:app