# JSON Type Conversion
# TIMESTAMP__2024_08_03__111510
# This example demonstrates the automatic type conversion of JSON data using `json.loads`.

import json

# JSON object to Python dictionary
json_obj = '{"name": "Alice", "age": 30}'
python_dict = json.loads(json_obj)
print("Type of python_dict:", type(python_dict))  # Output: <class 'dict'>

# JSON array to Python list
json_array = '["apple", "banana", "cherry"]'
python_list = json.loads(json_array)
print("Type of python_list:", type(python_list))  # Output: <class 'list'>

# JSON string to Python string
json_str = '"Hello, World!"'
python_str = json.loads(json_str)
print("Type of python_str:", type(python_str))  # Output: <class 'str'>

# JSON number to Python int or float
json_int = "123"
python_int = json.loads(json_int)
print("Type of python_int:", type(python_int))  # Output: <class 'int'>

json_float = "123.45"
python_float = json.loads(json_float)
print("Type of python_float:", type(python_float))  # Output: <class 'float'>

# JSON true to Python True
json_true = "true"
python_true = json.loads(json_true)
print("Type of python_true:", type(python_true))  # Output: <class 'bool'>

# JSON null to Python None
json_null = "null"
python_none = json.loads(json_null)
print("Type of python_none:", type(python_none))  # Output: <class 'NoneType'>
