#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files (for production)
python manage.py collectstatic --noinput

# Start the Django app and bind it to the correct port
python manage.py runserver 0.0.0.0:$PORT
