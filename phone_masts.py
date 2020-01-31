#!/usr/bin/env python

import csv
import os.path
import argparse

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass
class PhoneMast:
    """
    Dataclass to represent Phone Mast data
    """
    prop_name: str
    prop_addr1: str
    prop_addr2: str
    prop_addr3: str
    prop_addr4: str
    unit_name: str
    tenant: str
    lease_start_date: date
    lease_end_date: date
    lease_years: int
    current_rent: Decimal

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Perhaps not necessary since we're dealing with a specific data set
    parser.add_argument('--csv-fpath',
            help='The path of the data file to load',
            default='./phone_masts.csv')
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
    for mast in masts:
        print(mast)
