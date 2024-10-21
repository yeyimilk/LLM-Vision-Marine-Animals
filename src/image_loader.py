

import json
import os

for f_name in ['test', 'train', 'val']:
    with open(f'../data/{f_name}.json') as f:
        data = json.load(f)
    
    for item in data:
        values = item['file_path'].split('\\')
        print(values)
        item['file_path'] = f"{values[0]}/{values[2]}"

    with open(f'../data/{f_name}.json', 'w') as f:
        json.dump(data, f, indent=4)
    