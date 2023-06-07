#!/usr/bin/env python3

import json
from sys import argv
import matplotlib.pyplot as plt

# This script can accept input from step 4
def main():
    filename = argv[1]
    file = open(filename)
    hosts = json.load(file)

    all_classifications = [
        'classification_likely_real',
        'classification_potentially_real',
        'classification_likely_honeypot',
        'classification_honeypot',
    ]

    classifications = {c: 0 for c in all_classifications}
    
    for host in hosts:
        clas = next(filter(lambda i: i in all_classifications, host['indications']))
        classifications[clas] += 1

    print([c.replace('classification_', '') for c in all_classifications])
    print([classifications[c] for c in all_classifications])

    plt.rc('font', size=15)
    plt.barh([c.replace('classification_', '') for c in all_classifications],
             [classifications[c] for c in all_classifications],
             color=['royalblue', 'cornflowerblue', 'lightcoral', 'firebrick'])
    plt.xlabel('Number of hosts')
    plt.ylabel('Classification')
    plt.savefig('classifications.pdf', bbox_inches='tight')
    
    


if __name__ == '__main__':
    main()
