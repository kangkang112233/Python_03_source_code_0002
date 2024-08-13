# Explanation of pdb Module for Debugging in Python
# TIMESTAMP__2024_08_12__155658

import pdb


def faulty_function():
    a = 10
    b = 0
    result = a / b  # This line will cause a ZeroDivisionError
    return result


if __name__ == "__main__":
    pdb.run("faulty_function()")
