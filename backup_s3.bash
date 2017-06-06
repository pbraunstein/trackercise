#!/bin/bash

source $HOME/.bashrc
source $HOME/trackercise/venv/bin/activate
python $HOME/trackercise/manage.py backup_data_to_s3
deactivate
