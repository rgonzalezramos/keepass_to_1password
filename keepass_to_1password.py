#!/usr/bin/env python

import csv
import sys


def convert(f_in, f_out):
    reader = csv.reader(f_in)
    writer = csv.writer(f_out, quotechar='"', quoting=csv.QUOTE_ALL)
    for row in reader:
        writer.writerow([row[1], row[4], row[2], row[3], row[5], '', ''])


if __name__ == '__main__':
    convert(sys.stdin, sys.stdout)
