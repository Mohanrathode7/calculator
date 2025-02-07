# my_app/main.py

def add(a: float, b: float) -> float:
    """
    Returns the sum of a and b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Returns the difference of a and b.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Returns the product of a and b.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Returns the quotient of a divided by b.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    # Example usage from the command line:
    import sys

    if len(sys.argv) < 4:
        print("Usage: python main.py [add|subtract|multiply|divide] num1 num2")
        sys.exit(1)

    operation = sys.argv[1].lower()
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        try:
            result = divide(num1, num2)
        except ZeroDivisionError as e:
            print(e)
            sys.exit(1)
    else:
        print(f"Unknown operation: {operation}")
        sys.exit(1)

    print(f"Result: {result}")