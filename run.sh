#!/bin/bash
source env/bin/activate
cd gragieldowa
scrapy crawl sale -t csv -o ../exports/sale.csv
scrapy crawl purchase -t csv -o ../exports/purchase.csv
