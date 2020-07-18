#!/bin/bash
set -x
source env/bin/activate
cd gragieldowa
scrapy crawl sale -a stock=$1 -t csv -o ../exports/sale.csv
scrapy crawl purchase -a stock=$1 -t csv -o ../exports/purchase.csv
