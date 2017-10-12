#!/usr/bin/env python

import csv
import sys
import urllib
import urllib2

def iplookup(ip_addr):
    url = "http://some_host/ip/query?ip=%s" % ip_addr
    response = urllib2.urlopen(url)
    ret_json = response.read()
    return ret_json

def main():
    if len(sys.argv) != 3:
        sys.exit(1)

    infofield = sys.argv[1]
    ipfield = sys.argv[2]

    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
    w.writeheader()

    for result in r:
        if result[infofield] and result[ipfield]:
            # both fields were provided, just pass it along
            w.writerow(result)

        elif result[ipfield]:
            result[infofield] = iplookup(result[ipfield])
            if result[infofield]:
                w.writerow(result)


