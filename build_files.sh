#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations (if needed)
python manage.py migrate

# Remove the .ipynb_checkpoints directory if it exists (keep this if you need it)
find . -name ".ipynb_checkpoints" -exec rm -rf {} + || true
