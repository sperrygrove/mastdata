#!/usr/bin/env python

import csv
import os.path
import argparse

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

    with open(fpath) as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            print(row)
