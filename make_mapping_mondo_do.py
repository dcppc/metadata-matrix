#!/usr/bin/env python

import json
import csv

data = {
    'mondo_to_doid': {},
    'doid_to_mondo': {}
}

with open('mondo_doid.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None) # skip the first line, which is just a header
    
    for row in reader:
        mondo_id = row[0]
        do_id = row[2]

        if mondo_id in data['mondo_to_doid']:
            data['mondo_to_doid'][mondo_id].append(do_id)
        else:
            data['mondo_to_doid'][mondo_id] = [do_id]

        if do_id in data['doid_to_mondo']:
            data['doid_to_mondo'][do_id].append(mondo_id)
        else:
            data['doid_to_mondo'][do_id] = [mondo_id]
          
  
json_output = json.dumps(data, indent=2);

print(json_output)
