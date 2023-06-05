# step 2
plcscan_location = 'plcscan/plcscan.py'
python2_executable = 'python2'

# step 3
honeypot_open_port_threshold = 10
as_indications = {
    'SHARKTECH': 'datacenter_as',
    'DIGITALOCEAN-ASN': 'datacenter_as',
    'REDHOSTING-AS': 'datacenter_as',
    'AS-CHOOPA': 'datacenter_as',
    'IP-EEND-AS IP-EEND BV': 'university_as', # SURFnet
    # potential industrial ASes:
    # CRITICALCORE
    # ASN-ROUTIT
    # EQUEST-AS
    # NEXTPERTISE Nextpertise - deanone.nl
}
honeypot_defaults = {
    'conpot': { # https://github.com/mushorg/conpot/blob/f0e6925fb9632172922abe41b293d7ee438fa60b/conpot/templates/default/template.xml
        'Plant identification': 'Mouser Factory',
        'Serial number of module': '88111222',
    },
    'snap7': { # https://github.com/SCADACS/snap7/blob/f6ff90317ca5d54250f4dcd29209689a74e26d82/examples/plain-c/server.c
        'Name of the PLC': 'SAAP7-SERVER',
        'Serial number of module': 'S C-C2UR28922012',
        'Serial number of memory card': 'MMC 267FF11F',
    },
}
mobile_domains = [
    'mobile.kpn.net',
    'telenormobil.no',
    'netcom.no',
]
