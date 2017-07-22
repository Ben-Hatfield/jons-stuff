#!/bin/env python

import requests

MACS_FILE='macs.list'

def oui_lookup(mac_addr):
    result = requests.get('https://www.macvendorlookup.com/oui.php?mac={}'.format(mac_addr))
    if result.text != '':
        return result.json()[0].get('company')
    else:
        return None

def lookup_ouis(macs):
    lookups = []
    for mac in macs:
        lookups.append((mac,oui_lookup(mac)))
    return lookups

with open(MACS_FILE) as f:
    macs = [line.strip() for line in f.readlines()]
print(lookup_ouis(macs))
