#!/usr/bin/env python3

import json
from sys import argv
import matplotlib.pyplot as plt

# This script can accept input from step 4
def main():
    filename = argv[1]
    file = open(filename)
    hosts = json.load(file)

    bin_labels = ['1-10', '11-100', '>100']
        
    plt.rc('font', size=20)
    
    # all hosts
    plt.xlabel('Number of open ports')
    plt.ylabel('Number of hosts')
    bins = get_bins(hosts)
    print('all', bins)
    plt.bar(bin_labels, bins)
    plt.savefig('open_ports_all.pdf', bbox_inches='tight')
    plt.clf()

    # datacenter and uni
    plt.xlabel('Number of open ports')
    plt.ylabel('Number of hosts')
    required_indications = [
        'datacenter_as',
        'university_as'
    ]
    as_hosts = [h for h in hosts if any(x in required_indications for x in h['indications'])]
    as_bins = get_bins(as_hosts)
    print('AS', as_bins)
    plt.bar(bin_labels, as_bins, color='lightcoral')
    plt.savefig('open_ports_datacenter_uni.pdf', bbox_inches='tight')
    

def get_bins(hosts):
    bin1 = bin2 = bin3 = 0
    
    for host in hosts:
        p = host['open_port_count']
        if p <= 10:
            bin1 += 1
        elif p <= 100:
            bin2 += 1
        else:
            bin3 += 1
    return [bin1, bin2, bin3]
        


if __name__ == '__main__':
    main()
