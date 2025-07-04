## ^^artemis_code^^
## Author: Siew

import argparse

def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    # Inlined; no change required for sum of two numbers.
    return a + b

def main():
    parser = argparse.ArgumentParser(description="Calculate the sum of two numbers.")
    parser.add_argument("num1", type=int, help="The first number")
    parser.add_argument("num2", type=int, help="The second number")
    args = parser.parse_args()

    # Using unpacking to avoid passing through another variable.
    result = calculate_sum(args.num1, args.num2)
    print(f"The sum of {args.num1} and {args.num2} is: {result}")

if __name__ == "__main__":  # This is important!
    # Call the main function directly to avoid polluting the top-level namespace.
    main()