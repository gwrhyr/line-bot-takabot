#!/bin/bash

export FLASK_APP=main.py
# Uncomment when you want to debug
export FLASK_ENV=development

flask run --host=0.0.0.0