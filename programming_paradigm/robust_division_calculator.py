def safe_divide(numerator, denominator):
    """Safely divides two numbers, handling division by zero."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    finally:
        print("Over!")

def main():
    while True:
        try:
            num = float(input("Enter a numerator: "))
            denom = float(input("Enter a denominator: "))
            result = safe_divide(num, denom)
            print(f"The result of the division is {result}")
            break
        except ValueError:
            print("Error: Please enter numeric values only.")

main()