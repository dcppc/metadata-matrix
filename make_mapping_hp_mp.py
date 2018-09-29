#!/usr/bin/env python

import json
import csv

data = {
    'HP_to_MP': {},
    'MP_to_HP': {}
}

with open('hp-to-mp-bestmatches.tsv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')

    for row in reader:
        HP = row[0]
        MP = row[2]

        if HP in data['HP_to_MP']:
            data['HP_to_MP'][HP].append(MP)
        else:
            data['HP_to_MP'][HP] = [MP]
        
        if MP in data['MP_to_HP']:
            data['MP_to_HP'][MP].append(HP)
        else:
            data['MP_to_HP'][MP] = [HP]

json_output = json.dumps(data, indent=2);

print(json_output)

