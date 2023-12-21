import json
import requests
import pandas as pd

## Read the lines of the file from url
url = 'https://huggingface.co/datasets/MLCommons/peoples_speech/resolve/main/train/clean.json'
response = requests.get(url)
if response.status_code == 200:
    # Convert the byte content of the response to a string for consistent processing
    content = response.content.decode('utf-8')
    # Split the content into lines
    lines = content.split('\n')

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
    merge_data_df.to_json('merge_data_output_remote.json', orient='records')

else:
    print(f"Failed to load JSON data. Status code: {response.status_code}")