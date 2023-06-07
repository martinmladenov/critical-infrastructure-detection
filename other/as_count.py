#!/usr/bin/env python3

import json
from sys import argv

from tabulate import tabulate

# This script can accept input from step 1+
def main():
    filename = argv[1]
    file = open(filename)
    hosts = json.load(file)

    asc = dict() # AS counts
    asd = dict() # AS names / descriptions
    
    for host in hosts:
        asn = host['asn']
        if not asn in asc:
            asc[asn] = 0
            asd[asn] = host['as_name']
        
        asc[asn] += 1
        
    rows = [[asn, asd[asn], asc[asn]] for asn in asc.keys()]
    rows = sorted(rows, key=lambda k: k[2], reverse=True)

    print(tabulate([["ASN", "AS Name", "Count"]] + rows, headers="firstrow", tablefmt='latex'))
    
    


if __name__ == '__main__':
    main()
