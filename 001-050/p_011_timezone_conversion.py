# `ZoneInfoNotFoundError` の処理: 指定されたタイムゾーン `Asia/Tokyo` が見つからない場合、このエラーが発生します。
# これはシステムにタイムゾーンデータがインストールされていないか、タイムゾーン名が間違っていることが原因です。
# この問題を解決するには、正しいタイムゾーン名を確認し、必要に応じてタイムゾーンデータをインストールします。
#
# Handling `ZoneInfoNotFoundError`: This error occurs when the specified timezone `Asia/Tokyo` is not found.
# It may be due to missing timezone data on the system or an incorrect timezone name.
# To resolve this issue, ensure the correct timezone name is used and install timezone data if necessary.

from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def get_time_in_timezone(timezone):
    try:
        # Get the current time in the specified timezone
        current_time = datetime.now(ZoneInfo(timezone))
        return current_time
    except ZoneInfoNotFoundError:
        return f"No time zone found with key {timezone}"


# Get the current time in Tokyo
tokyo_time = get_time_in_timezone("Asia/Tokyo")
print(tokyo_time)

# Get the current time in New York
new_york_time = get_time_in_timezone("America/New_York")
print(new_york_time)

# Example: Book Management System - Convert timestamp to user's timezone

# Sample book transaction timestamp (in UTC)
transaction_time = datetime(2024, 7, 6, 15, 30, tzinfo=ZoneInfo("UTC"))


# Function to convert transaction time to user's timezone
def convert_transaction_time(transaction_time, user_timezone):
    try:
        return transaction_time.astimezone(ZoneInfo(user_timezone))
    except ZoneInfoNotFoundError:
        return f"No time zone found with key {user_timezone}"


# Convert and print transaction time in New York timezone
print(convert_transaction_time(transaction_time, "America/New_York"))
