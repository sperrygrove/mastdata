#!/usr/bin/env python

import csv
import os.path
import argparse

from datetime import datetime, date
from decimal import Decimal

from phonemast import PhoneMast, PhoneMasts

def read_mast_data(fpath):
    """
    Read the data from the provided file at path fpath
    """
    masts = []
    with open(fpath) as csvfile:
        rows = csv.reader(csvfile)
        next(rows) # omit the header
        for row in rows:
            masts.append(
                PhoneMast(prop_name=row[0], prop_addr1=row[1],
                    prop_addr2=row[2], prop_addr3=row[3], prop_addr4=row[4],
                    unit_name=row[5], tenant=row[6],
                    lease_start_date=datetime.strptime(row[7], '%d %b %Y').date(),
                    lease_end_date=datetime.strptime(row[8], '%d %b %Y').date(),
                    lease_years=int(row[9]), current_rent=Decimal(row[10]))
                )
    return masts

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Perhaps not necessary since we're dealing with a specific data set
    parser.add_argument('--csv-fpath',
            help='The path of the data file to load',
            default='./phone_masts.csv')
    parser.add_argument('--five-by-rent-asc', dest='show_by_rent',
            default=False, action='store_true',
            help='Show first 5 masts sorted by "Current Rent"')
    parser.add_argument('--lease-years', dest='lease_years_25',
            default=False, action='store_true',
            help='Show masts with 25 lease years')
    parser.add_argument('--mast-count-by-tenant', dest='count_by_tenant',
            default=False, action='store_true',
            help='Show mast count by tenant')
    parser.add_argument('--lease-date-between', dest='lease_date_between',
            default=False, action='store_true',
            help='List data for rentals with lease start date between '
                 '1st June 1999 and 31st August 2007')

    args = parser.parse_args()
    fpath = os.path.abspath(args.csv_fpath)
    if not os.path.exists(fpath):
        raise SystemExit(f'File not found: {fpath}')

    masts = read_mast_data(fpath)
    phone_masts = PhoneMasts(masts)

    # Allow user input to run all of your script, or specific sections
    if not any((args.show_by_rent,
                args.lease_years_25,
                args.count_by_tenant,
                args.lease_date_between)):
        args.show_by_rent = \
        args.lease_years_25 = \
        args.count_by_tenant = \
        args.lease_date_between = True

    if args.show_by_rent:
        print('1b) Obtain the first 5 items from the resultant list and '
                'output to the console\n')
        print(phone_masts.ordered_by_current_rent())

    if args.lease_years_25:
        # From the list of all mast data, create a new list of mast data with
        #'Lease Years' = 25 years
        masts_with_25_lease_years = phone_masts.with_lease_years(25)
        print('\n2a) Output the list to the console, including all data fields\n')
        print(masts_with_25_lease_years)
        print('\n2b) Output the total rent for all items in this list to the console\n')
        print('Total rent for these phone masts: '
                f'{sum(mast.current_rent for mast in masts_with_25_lease_years)}')

    if args.count_by_tenant:
        print('\n3a) Output the dictionary to the console in a readable form\n')
        print(dict(phone_masts.count_by_tenant()))


    if args.lease_date_between:
        print('\n4) List the data for rentals with “Lease Start Date” between '
                '1st June 1999 and 31st August 2007\n')
        print('\n4a) Output the data to the console with dates formatted as DD/MM/YYYY\n')
        print(phone_masts.lease_start_between(date(1999, 6, 1), date(2007, 8, 31)))
