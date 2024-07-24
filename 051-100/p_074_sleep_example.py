# This code example demonstrates the usage of the sleep() function
# in the context of a library management system.

import time


def delay_operation(delay_time):
    """
    Delay an operation for a specified amount of time.

    Args:
    delay_time (float): The amount of time to delay in seconds.

    Returns:
    str: A message indicating the delay has completed.
    """
    print(f"Delaying operation for {delay_time} seconds...")
    time.sleep(delay_time)  # Delay for the specified number of seconds
    return "Operation resumed after delay"


# Test cases
delay_time_1 = 3  # 3 seconds
delay_time_2 = 1.5  # 1.5 seconds
delay_time_3 = 2 * 2  # 4 seconds (using multiplication)

# Delay operations
print(delay_operation(delay_time_1))
print(delay_operation(delay_time_2))
print(delay_operation(delay_time_3))
