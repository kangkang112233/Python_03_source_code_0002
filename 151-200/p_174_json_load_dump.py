# Explanation of load() and dump() Functions in Python's json Module
# TIMESTAMP__2024_08_12__125336

import json


# Function to read JSON data from a file
def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# Function to write JSON data to a file
def write_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# Example usage
file_path = "example.json"
data_to_write = {
    "title": "Python Programming",
    "author": "John Doe",
    "published": 2024,
    "topics": ["json", "file handling", "examples"],
}

# Writing data to JSON file
write_json(data_to_write, file_path)

# Reading data from JSON file
read_data = read_json(file_path)
print("Read data from JSON file:")
print(read_data)
