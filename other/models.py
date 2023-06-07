#!/usr/bin/env python3

import json
from sys import argv

from tabulate import tabulate

# This script can accept input from step 4
def main():
    filename = argv[1]
    file = open(filename)
    hosts = json.load(file)

    models = dict()

    required_indications = [
        'classification_likely_real',
        'classification_potentially_real'
    ]
    
    for host in hosts:
        print(host)
        indications = host['indications']
        if all(x not in required_indications for x in indications) or not host['s7_data']:
            continue
        model = next((e['value'].split('v.')[0].strip() for e in host['s7_data'] if e['key'] == 'Module'), None)
        models[model] = models.get(model, 0) + 1
        
    rows = [[model, models[model]] for model in models.keys()]
    rows = sorted(rows, key=lambda k: k[-1], reverse=True)

    print(tabulate([["Model number", "Count"]] + rows, headers="firstrow"))
    print(tabulate([["Model number", "Count"]] + rows, headers="firstrow", tablefmt='latex'))
    
    


if __name__ == '__main__':
    main()
