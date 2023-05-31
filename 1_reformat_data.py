#!/usr/bin/env python3

import json
from sys import argv
from parameters import *

def main():
    filename = argv[1]
    file = open(filename)
    hosts = json.load(file)

    host_results = []

    for i in range(len(hosts)):
        host = hosts[i]

        # extract censys data
        ip = host['ip']
        services = host['services']
        open_port_count = len(services)

        s7_service = next((s for s in services if s['port'] == 102 and s['service_name'] == 'S7'), None)

        host_as = host['autonomous_system']
        asn = host_as['asn']
        as_name = host_as['name']

        reverse_dns = host.get('dns', {}).get('reverse_dns', {}).get('names', [None])[0]

        # build result
        host_results.append({
            'ip': ip,
            'reverse_dns': reverse_dns,
            'asn': asn,
            'as_name': as_name,
            'open_port_count': open_port_count,
            's7_censys_service': s7_service
        })
    
    print(json.dumps(host_results, indent=4))

if __name__ == '__main__':
    main()
