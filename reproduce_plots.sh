#!/bin/bash

set -x;
set -e;

mkdir data;

# *****************
# Run this script to get the paper plots in Fig. 1
# ******************

# 1. Get Tokens
./cryptofees/get_cryptofees_tokens.sh;

# 2. Get Protocol Fees
python3 cryptofees/pull_all_time_fees.py;

# 3. Get Coingecko Market Caps
./curls/get_market_caps.sh

# 3. Produce Plots - AAVE & Uniswap
python3 cryptofees/plot_uniswap.py;
python3 cryptofees/plot_aave.py;

# 4. Procue Plots - YFI
./yearn_revenues/yearn_revenues_curl.sh;
python3 yearn_revenues/plot_yearn_revenues.py;

echo "Done."