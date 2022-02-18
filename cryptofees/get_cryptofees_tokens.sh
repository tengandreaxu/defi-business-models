#!/bin/bash

set -x;

#********************
# This simple script retrieves the Cryptofees tokens universe
#********************

curl https://cryptofees.info/api/v1/fees -o data/cryptofees_tokens.json;
python3 cryptofees/convert_cryptofees_json_to_csv.py