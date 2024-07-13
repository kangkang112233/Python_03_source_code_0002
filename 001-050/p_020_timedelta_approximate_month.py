# `timedelta` を使用したおおよその月単位の操作: `timedelta` は月を直接サポートしていませんが、
# 日数に変換することでおおよその月単位の操作が可能です。1ヶ月を約30日として、1/4ヶ月を約7.5日と見なして減算できます。
#
# Using `timedelta` for Approximate Month Manipulation: `timedelta` does not directly support months,
# but you can approximate month manipulations by converting to days.
# Considering one month as approximately 30 days, you can subtract 7.5 days for a quarter of a month.

from datetime import datetime, timedelta

# Get the current date and time
specific_date = datetime.now()

# Subtract a quarter of a month (approximately 7.5 days)
new_date = specific_date - timedelta(days=7.5)

# Print the new date
print(f"New date after subtracting a quarter of a month: {new_date}")

# Example: Book Management System - Calculate due date for book returns

# Current date
current_date = datetime.now()


# Function to calculate the new due date
def calculate_due_date(start_date, duration_in_days):
    return start_date + timedelta(days=duration_in_days)


# Calculate due date after a quarter of a month (7.5 days)
due_date = calculate_due_date(current_date, -7.5)

# Print the calculated due date
print(f"Due date for book return: {due_date}")
