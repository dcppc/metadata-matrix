#!/usr/bin/env python

import json
import csv

data = {
    'Humangene_to_MODgene': {},
    'MODgene_to_Humangene': {}
}

with open('alliance-orthology-july-19-2018-stable-1.6.0-v4.tsv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader, None) # skip the first line, which is just a header

    for row in reader:
        if row[0].strip()[0] == '#':  #
           continue
        if "Gene1ID" in row or "Gene2ID" in row:
           continue
        Gene1ID = row[0]
        Gene2ID = row[4]

        if Gene1ID in data['Humangene_to_MODgene']:
            data['Humangene_to_MODgene'][Gene1ID].append(Gene2ID)
        else:
            data['Humangene_to_MODgene'][Gene1ID] = [Gene2ID]
        
        if Gene2ID in data['MODgene_to_Humangene']:
            data['MODgene_to_Humangene'][Gene2ID].append(Gene1ID)
        else:
            data['MODgene_to_Humangene'][Gene2ID] = [Gene1ID]

json_output = json.dumps(data, indent=2);

print(json_output)

