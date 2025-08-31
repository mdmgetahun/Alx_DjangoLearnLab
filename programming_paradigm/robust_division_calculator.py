def safe_divide(numerator, denominator):
    """Safely divides two numbers, handling division by zero."""
    if denominator == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return numerator / denominator
    

def main():
    while True:
        try:
            num = float(input("Enter a numerator: "))
            denom = float(input("Enter a denominator: "))
            result = safe_divide(num, denom)
            print(f"Result: {result}")
            break
        except ValueError:
            print("Error: Please enter numeric values only.")
        except ZeroDivisionError as e:
            print(e)
        

main()