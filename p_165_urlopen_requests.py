# Explanation of urlopen() function for GET and POST requests
# TIMESTAMP__2024_08_11__152934

from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json


# Function to send a GET request
def send_get_request(url):
    response = urlopen(url)
    return response.read().decode("utf-8")


# Function to send a POST request
def send_post_request(url, data):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = urlencode(data).encode("utf-8")
    request = Request(url, data=data, headers=headers)
    response = urlopen(request)
    return response.read().decode("utf-8")


# Example URL for GET request
get_url = "http://httpbin.org/get"
get_response = send_get_request(get_url)
print("GET request response:")
print(get_response)
print(json.dumps(json.loads(get_response), indent=4))

# Example URL for POST request
post_url = "http://httpbin.org/post"
post_data = {"name": "John", "age": 30}
post_response = send_post_request(post_url, post_data)
print("\nPOST request response:")
print(json.dumps(json.loads(post_response), indent=4))
