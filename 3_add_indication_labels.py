#!/usr/bin/env python3

import json
from sys import argv
from parameters import *

# indication functions

def many_open_ports(host):
    open_port_count = host['open_port_count']
    if open_port_count > honeypot_open_port_threshold:
        return 'many_open_ports'

def no_s7_censys_label(host):
    s7_censys_service = host['s7_censys_service']
    if not s7_censys_service:
        return 'no_s7_censys_label'

def as_indication(host):
    as_name = host['as_name']
    if as_name in as_indications:
        return as_indications[as_name]
    
def mobile_network(host):
    reverse_dns = host['reverse_dns']
    if reverse_dns and any(reverse_dns.endswith(f'.{domain}') for domain in mobile_domains):
        return 'mobile_network'
    
def no_plcscan_results(host):
    if 's7_data' in host and not host['s7_data']:
        return 'no_plcscan_results'

def honeypot_default(host):
    if not host.get('s7_data', None):
        return
    s7_data = {e['key']: e['value'] for e in host['s7_data']}
    for honeypot_name, defaults in honeypot_defaults.items():
        for d_name, d_value in defaults.items():
            if d_name in s7_data and s7_data[d_name] == d_value:
                return f'honeypot_defaults_{honeypot_name}'

def vipa_indication(host):
    if not host.get('s7_data', None):
        return
    is_vipa = next((e for e in host['s7_data'] if e['key'] == 'Unknown (129)' and 'VIPA' in e['value']), None)
    if is_vipa:
        return 'manufacturer_vipa'
    

indication_functions = [
    many_open_ports,
    no_s7_censys_label,
    as_indication,
    mobile_network,
    no_plcscan_results,
    honeypot_default,
    vipa_indication,
]

# main logic

def main():
    filename = argv[1]
    file = open(filename)
    hosts = json.load(file)

    for i in range(len(hosts)):
        host = hosts[i]

        indications = []
        for f in indication_functions:
            indication = f(host)
            if indication:
                indications.append(indication)

        # build result
        host['indications'] = indications
    
    print(json.dumps(hosts, indent=4))

if __name__ == '__main__':
    main()
