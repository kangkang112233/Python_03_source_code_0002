# Serialization with json.dumps and default Parameter
# TIMESTAMP__2024_08_04__160701
# This example demonstrates how to use the default parameter in json.dumps in a library management system.

import json
from datetime import datetime


# Custom serialization function for datetime objects
def default_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


# Sample dictionary with a datetime object
data = {
    "title": "Python Programming",
    "author": "John Doe",
    "published": datetime(2021, 5, 17, 10, 45),
}

# Serialize the dictionary to a JSON string
json_data = json.dumps(data, default=default_serializer)
print(json_data)
