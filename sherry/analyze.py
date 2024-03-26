import json
json_data = '{"name": "John", "age": 25}'
data = json.loads(json_data)
print(data['name'])