#!/usr/bin/env python

import csv
import os.path
import argparse

from datetime import datetime
from decimal import Decimal

from phonemast import PhoneMast, PhoneMasts

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Perhaps not necessary since we're dealing with a specific data set
    parser.add_argument('--csv-fpath',
            help='The path of the data file to load',
            default='./phone_masts.csv')
    parser.add_argument('--five-by-rent-asc', dest='show_by_rent',
            default=False, action='store_true',
            help='Show first 5 masts sorted by "Current Rent"')

    args = parser.parse_args()
    fpath = os.path.abspath(args.csv_fpath)
    if not os.path.exists(fpath):
        raise SystemExit(f'File not found: {fpath}')

    masts = []
    with open(fpath) as csvfile:
        rows = csv.reader(csvfile)
        next(rows) # omit the header
        for row in rows:
            masts.append(
                PhoneMast(prop_name=row[0], prop_addr1=row[1],
                    prop_addr2=row[2], prop_addr3=row[3], prop_addr4=row[4],
                    unit_name=row[5], tenant=row[6],
                    lease_start_date=datetime.strptime(row[7], '%d %b %Y'),
                    lease_end_date=datetime.strptime(row[8], '%d %b %Y'),
                    lease_years=int(row[9]), current_rent=Decimal(row[10]))
                )
    phone_masts = PhoneMasts(masts)
    if args.show_by_rent:
        print('1a) Obtain the first 5 items from the resultant list and output to the console\n')
        print(phone_masts.ordered_by_current_rent())
