import subprocess
import sys


# Function to format Python code using Black
def format_code_with_black(
    file_path, check_only=False, line_length=88, exclude_pattern=None
):
    # Ensure Black is installed
    try:
        subprocess.run(
            ["black", "--version"], check=True, capture_output=True, text=True
        )
    except FileNotFoundError:
        print(
            "Black is not installed or not found in PATH. Please install Black using 'pip install black'."
        )
        sys.exit(1)

    # Base command for Black
    command = ["black", file_path, "-l", str(line_length)]

    # Add --check option if only checking the format
    if check_only:
        command.append("--check")

    # Add --exclude option if an exclude pattern is provided
    if exclude_pattern:
        command.extend(["--exclude", exclude_pattern])

    # Run the Black command
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(
            "Ensure that Black is correctly installed and available in the system PATH."
        )
        sys.exit(1)


# Example usage in a library management system context
def setup_and_format_code():
    file_path = "library_management_system.py"

    # Create a sample Python file to format
    with open(file_path, "w") as file:
        file.write("def example_function():\n")
        file.write("    print('Hello, world!')\n")

    # Format the code with Black
    print("Formatting code with Black:")
    format_code_with_black(file_path, line_length=80)

    # Check the code format with Black
    print("\nChecking code format with Black:")
    format_code_with_black(file_path, check_only=True, line_length=80)


# Setup and format the code
setup_and_format_code()

# Output:
# Formatting code with Black:
# reformatted library_management_system.py
# All done! ✨ 🍰 ✨
# 1 file reformatted.

# Checking code format with Black:
# would reformat library_management_system.py
# All done! ✨ 🍰 ✨
# 1 file would be reformatted.
