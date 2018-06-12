#!/usr/bin/env python

import json
import csv


data = {
    'mondo_to_doid': {},
}

with open('mondo_doid.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        mondo_id = row[0]
        do_id = row[2]

        if mondo_id in data['mondo_to_doid']:
            data['mondo_to_doid'][mondo_id].append(do_id)
        else:
            data['mondo_to_doid'][mondo_id] = [do_id]
            
json_output = json.dumps(data, indent=2);

print(json_output)

