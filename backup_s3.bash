#!/bin/bash

source venv/bin/activate
python manage.py backup_data_to_s3
