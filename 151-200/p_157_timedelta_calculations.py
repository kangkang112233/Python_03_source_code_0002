# Explanation of Using timedelta to Calculate Past Dates
# TIMESTAMP__2024_08_11__115833

from datetime import datetime, timedelta


# Function to get the date two weeks ago from today
def get_date_two_weeks_ago():
    today = datetime.now()
    two_weeks_ago = today - timedelta(weeks=2)
    return two_weeks_ago


# Get the date two weeks ago
date_two_weeks_ago = get_date_two_weeks_ago()

# Print the date two weeks ago
print(f"Today's date: {datetime.now().strftime('%Y-%m-%d')}")
print(f"Date two weeks ago: {date_two_weeks_ago.strftime('%Y-%m-%d')}")
