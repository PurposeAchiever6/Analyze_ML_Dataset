import json
import requests
import pandas as pd

## Read the lines of the file
with open('clean.json', 'r') as file:
    lines = file.readlines()

# Initialize an empty list to store the JSON objects
data_list = []

# Parse each line as a JSON object and append to the list
for line in lines:
    json_line = json.loads(line)['training_data']
    for i in range(len(json_line['name'])):
        merge_data = f"{json_line['name'][i]}/{json_line['duration_ms'][i]}/{json_line['label'][i]}"
        data_list.append(merge_data)

# Combine the list of data frames into a single data frame
merge_data_df = pd.DataFrame(data_list, columns=['merge_data'])

# Save the merge_data property as a JSON file
merge_data_df.to_json('merge_data_output_local.json', orient='records')