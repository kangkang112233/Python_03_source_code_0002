# Explanation of argparse module in Python
# TIMESTAMP__2024_08_11__145322

import argparse


# Function to demonstrate the use of argparse with a required argument
def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--num", type=int, required=True, help="An integer number")

    args = parser.parse_args()
    print(f"The provided number is {args.num}")


if __name__ == "__main__":
    main()
