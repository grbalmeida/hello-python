import json
from data.customers import customers, customers_json

my_list = [1, 2, 3, 4, 5, 6]
json_data = json.dumps(my_list, indent=2)
print(json_data)
print(type(json_data))

my_dict = json.loads(customers_json)
print(my_dict, type(my_dict))
print(my_dict.get('1'))
print(my_dict.get('1').get('name'))