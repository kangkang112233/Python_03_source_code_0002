# Knowledge point: strftime() method to convert date object to string

from datetime import datetime


# Example for a library management system
# Function to format the current date and time as a string
def get_formatted_datetime():
    # Get the current date and time
    now = datetime.now()

    # Format the date and time as a string
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date


# Function to display formatted date and time
def display_formatted_datetime():
    formatted_date = get_formatted_datetime()
    print("Current date and time:", formatted_date)


# Example usage
if __name__ == "__main__":
    display_formatted_datetime()

# Output:
# Current date and time: YYYY-MM-DD HH:MM:SS
