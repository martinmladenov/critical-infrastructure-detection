#!/usr/bin/env python3

import json
from sys import argv
from parameters import *

# list of indications:
# many_open_ports
# no_s7_censys_label
# mobile_network
# no_plcscan_results
# datacenter_as
# university_as
# honeypot_defaults_conpot
# honeypot_defaults_snap7
# manufacturer_vipa'

classification_unknown = 'classification_potentially_real'
classification_likely_honeypot = 'classification_likely_honeypot'
classification_honeypot = 'classification_honeypot'
classification_likely_real = 'classification_likely_real'

def classify(indications):

    # If we have observed honeypot defaults, it's definitely a honeypot
    if any(x in indications for x in ['honeypot_defaults_conpot', 'honeypot_defaults_snap7']):
        return classification_honeypot

    # If it's at a datacenter or a university, it's likely a honeypot
    if any(x in indications for x in ['datacenter_as', 'university_as']):
        return classification_likely_honeypot

    # If it's at a datacenter or a university, it's likely a honeypot
    if 'many_open_ports' in indications:
        return classification_likely_honeypot

    # If it's on a mobile network, it's likely real
    if 'mobile_network' in indications:
        return classification_likely_real
    
    return classification_unknown

def main():
    filename = argv[1]
    file = open(filename)
    hosts = json.load(file)

    for i in range(len(hosts)):
        host = hosts[i]

        indications = set(host['indications'])

        label = classify(indications)
        host['indications'].append(label)
    
    print(json.dumps(hosts, indent=4))

if __name__ == '__main__':
    main()
