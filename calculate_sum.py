import argparse

def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

if __name__ == "__main__":  # This is important!
    parser = argparse.ArgumentParser(description="Calculate the sum of two numbers.")
    parser.add_argument("num1", type=int, help="The first number")
    parser.add_argument("num2", type=int, help="The second number")
    args = parser.parse_args()

    result = calculate_sum(args.num1, args.num2)
    print(f"The sum of {args.num1} and {args.num2} is: {result}") 
