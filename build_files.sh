# build_files.sh
python3 --version
python3 -m ensurepip --upgrade
pip3 install -r requirements.txt
# python3 manage.py collectstatic --noinput


#!/bin/bash

# Update pip
echo "Updating pip..."
python3 pip install -U pip

# Install dependencies

echo "Installing project dependencies..."
python3 -m pip install -r requirements.txt

# Make migrations
echo "Making migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
#Install whitenoise
echo "Installing white noise..."
python3 manage.py whitenoise
# Collect staticfiles
echo "Collect static..."
python3 manage.py collectstatic --noinput --clear

echo "Build process completed!"```
