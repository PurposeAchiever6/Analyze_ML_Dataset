import json

with open('merge_data_output_.json', 'r') as file:
    data = json.load(file)

print(data[0])
print(data[0]['merge_data'])