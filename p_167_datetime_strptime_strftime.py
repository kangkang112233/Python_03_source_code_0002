# Explanation of strptime and strftime in Python
# TIMESTAMP__2024_08_12__121359

from datetime import datetime


# Function to demonstrate strptime
def parse_date(date_string, date_format):
    return datetime.strptime(date_string, date_format)


# Function to demonstrate strftime
def format_date(date_obj, date_format):
    return date_obj.strftime(date_format)


# Example date string
date_string = "2024-08-12 15:30:00"
date_format = "%Y-%m-%d %H:%M:%S"

# Parsing the date string to datetime object
parsed_date = parse_date(date_string, date_format)
print("Parsed datetime object:")
print(parsed_date)

# Formatting the datetime object to string
formatted_date = format_date(parsed_date, "%d/%m/%Y %I:%M %p")
print("\nFormatted date string:")
print(formatted_date)
