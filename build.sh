#!/usr/bin/env bash
# exit on error
set -o errexit

# Create the 'static' directory if it doesn't exist
mkdir -p static

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

python manage.py makemigrations

# Run migrations
python manage.py migrate

python manage.py runserver 127.0.0.1:8000