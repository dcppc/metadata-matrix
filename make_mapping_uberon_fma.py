#!/usr/bin/env python

import json
import csv

data = {
    'uberon_to_fma': {},
    'fma_to_uberon': {}
}

with open('uberon_fma.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None) # skip the first line, which is just a header

    for row in reader:
        uberon_id = row[0]
        fma_id = row[2]

        if uberon_id in data['uberon_to_fma']:
            data['uberon_to_fma'][uberon_id].append(fma_id)
        else:
            data['uberon_to_fma'][uberon_id] = [fma_id]
        
        if fma_id in data['fma_to_uberon']:
            data['fma_to_uberon'][fma_id].append(uberon_id)
        else:
            data['fma_to_uberon'][fma_id] = [uberon_id]

json_output = json.dumps(data, indent=2);

print(json_output)

