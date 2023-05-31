## Information

This is code related to my thesis "Detection of critical infrastructure devices on the public Internet".

The full thesis can be found on the [TU Delft Repository](https://repository.tudelft.nl/).

## Steps

The steps below can be used for reproduction of the research.

### Step 0

Set up the [Censys CLI](https://censys-python.readthedocs.io/en/stable/usage-cli.html) on your machine.

Download data from Censys. For example:

```
censys search 'services.service_name=S7 and location.country_code=NL and services.port=102' --pages -1 -o hosts_0.json
```

### Step 1

Perform initial preprocessing of the Censys data.

```
python3 1_reformat_data.py hosts_0.json > hosts_1.json
```

### Step 2

Connect to the hosts and retrieve metadata from the S7comm service.

This requires [plcscan](https://code.google.com/archive/p/plcscan/) and Python 2 as a dependency of plcscan. Set up the paths to plcscan and Python 2 in `parameters.py`.

**Warning!** This will actively connect to the hosts from your machine.

```
python3 2_retrieve_s7_metadata.py hosts_1.json > hosts_2.json
```

This can take a while.

### Step 3

Process the data to add indication labels.

Optionally, tweak parameters in `parameters.py`.

```
python3 3_add_indication_labels.py hosts_2.json > hosts_3.json
```
