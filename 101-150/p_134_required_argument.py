# Setting Required Arguments with `required=True`
# TIMESTAMP__2024_08_04__151206
# This example demonstrates how to use `required=True` with argparse in a library management system.

import argparse


def main():
    parser = argparse.ArgumentParser(description="Library Management System")
    parser.add_argument("--book", required=True, help="Name of the book")
    parser.add_argument("--author", required=True, help="Author of the book")
    args = parser.parse_args()

    print(f"Book: {args.book}")
    print(f"Author: {args.author}")


if __name__ == "__main__":
    main()
