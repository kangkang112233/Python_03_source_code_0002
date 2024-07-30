# Knowledge point: fromisoformat to convert ISO8601 string to datetime object

from datetime import datetime


# Example for a library management system
# Function to convert an ISO8601 string to a datetime object
def convert_iso_to_datetime(date_string):
    # Convert the ISO8601 string to a datetime object
    date_time_obj = datetime.fromisoformat(date_string)

    return date_time_obj


# Function to display the converted datetime object
def display_converted_datetime(date_string):
    date_time_obj = convert_iso_to_datetime(date_string)
    print("Converted datetime object:", date_time_obj)


# Example usage
if __name__ == "__main__":
    iso_date_string = "2023-07-25T15:30:00"
    display_converted_datetime(iso_date_string)

# Output:
# Converted datetime object: 2023-07-25 15:30:00
