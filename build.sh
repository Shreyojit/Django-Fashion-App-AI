#!/usr/bin/env bash
# exit on error
set -o errexit

# Create the 'static' directory if it doesn't exist
mkdir -p static

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
