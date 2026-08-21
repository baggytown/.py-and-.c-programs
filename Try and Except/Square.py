import math

def get_square_root():
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)
        
        if number < 0:
            raise ValueError("Negative numbers are not allowed.")
        
        result = math.sqrt(number)
        print(f"Result: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")

get_square_root()
