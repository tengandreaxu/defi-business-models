#!/bin/bash

set -x;

source venv/bin/activate;
python3 setup.py sdist;
python3 -m pip install dist/defi-business-models-0.0.0.tar.gz;
python3 -m pip install -r requirements.txt;