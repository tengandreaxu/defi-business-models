#!/bin/bash

CWD=`pwd`

curl -X 'GET' \
'https://api.coingecko.com/api/v3/coins/list' \
-H 'accept: application/json' > ${CWD}/data/coingecko/coingecko_coins.json

# AAVE 
curl -X 'GET' \
  'https://api.coingecko.com/api/v3/coins/aave/market_chart?vs_currency=usd&days=1000&interval=daily' \
  -H 'accept: application/json' > ${CWD}/data/coingecko/aave.json

# UNI
curl -X 'GET' \
  'https://api.coingecko.com/api/v3/coins/uniswap/market_chart?vs_currency=usd&days=1000&interval=daily' \
  -H 'accept: application/json' > ${CWD}/data/coingecko/uniswap.json


# YEARN 
curl -X 'GET' \
  'https://api.coingecko.com/api/v3/coins/yearn-finance/market_chart?vs_currency=usd&days=1000&interval=daily' \
  -H 'accept: application/json' > ${CWD}/data/coingecko/yearn.json