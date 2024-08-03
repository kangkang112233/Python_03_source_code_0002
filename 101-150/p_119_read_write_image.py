# Reading and Writing Images from the Internet
# TIMESTAMP__2024_08_03__112840
# This example demonstrates how to read an image from a URL and save it locally in a library management system.

import requests
from PIL import Image
from io import BytesIO

# URL of the image to be downloaded
image_url = "https://images.ctfassets.net/rt5zmd3ipxai/25pHfG94sGlRALOqbRvSxl/9f591d8263607fdf923b962cbfcde2a9/NVA-panda.jpg?fit=fill&fm=webp&h=578&w=1070&q=72"

# Fetching the image data from the URL
response = requests.get(image_url)
response.raise_for_status()  # Check if the request was successful

# Creating an Image object from the fetched data using Pillow
image = Image.open(BytesIO(response.content))

# Saving the image locally
image.save("local_image.jpg")

print("Image downloaded and saved as 'local_image.jpg'")
