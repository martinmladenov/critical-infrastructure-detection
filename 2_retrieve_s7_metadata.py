#!/usr/bin/env python3

import json
from sys import argv, stderr
from parameters import *
import subprocess
import re
import multiprocessing

def plcscan_results(ip):
    try:
        matches = []
        attempts = 0
        while not matches and attempts < 5:
            attempts += 1
            plcscan_result_raw = subprocess.run([python2_executable, plcscan_location,
                                                '--ports', '102',
                                                '--timeout', '5',
                                                ip], stdout=subprocess.PIPE)
            plcscan_result = plcscan_result_raw.stdout.decode('utf-8')

            # parse plcscan results
            matches = re.findall('^ {2}(.+[^\s])\s*:\s*((?:.+[^\s])?)\s*\(([0-9a-f]*)\)$', plcscan_result, re.MULTILINE)
        return matches
    except:
        return []

def process_host(host):
    ip = host['ip']

    # use plcscan to connect to the device and retrieve information
    matches = plcscan_results(ip)

    # build result
    host['s7_data'] = list(map(lambda kvp: {
            'key': kvp[0],
            'value': kvp[1],
            'value_raw': kvp[2]
        }, matches)) if matches else None

    print(f'Processed {ip}', file=stderr)

    return host

def main():
    filename = argv[1]
    file = open(filename)
    hosts = json.load(file)

    pool = multiprocessing.Pool(processes=32) # connect to 32 hosts at a time
    hosts = pool.map(process_host, hosts)    
    
    print(json.dumps(hosts, indent=4))

if __name__ == '__main__':
    main()
