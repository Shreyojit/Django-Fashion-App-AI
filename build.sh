#!/usr/bin/env bash
# exit on error
set -o errexit

# Create the 'static' directory if it doesn't exist
mkdir -p static

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Make migrations
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Create superuser if needed
if [[ ! $(python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='shreyo').exists())") == "True" ]]; then
  python manage.py createsuperuser --no-input --username "shreyo" --email "shreyo@example.com" --password "fashion2025"
fi


