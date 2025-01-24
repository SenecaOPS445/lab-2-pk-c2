#!/usr/bin/env python3
import sys  # Import the sys module to handle arguments

# Argument check: Ensure exactly 3 arguments (script name, name, and age)
if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} name age')
    sys.exit(0)  # Exit with status 0, but still print the error message

# If the correct number of arguments is provided
name = sys.argv[1]  # First argument is the name
age = sys.argv[2]   # Second argument is the age

# Print the greeting message
print(f'Hi {name}, you are {age} years old.')

