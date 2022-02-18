#!/bin/bash

set -x;

#****************
# Simply creates a Python virtual environment
# and installs essential packages
#****************
python3 -m venv venv;
source venv/bin/activate;
python3 -m pip install --upgrade pip;
python3 -m pip install wheel;