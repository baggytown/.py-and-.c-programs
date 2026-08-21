def calculate_square_root(number: float) -> float:
    if not isinstance(number, (int, float)):
        raise TypeError("Expected a number")
    if number < 0:
        raise ValueError("Cannot be negative")
    return number ** 0.5

try:
    user_input = -9
    result = calculate_square_root(user_input)
    print(f"Result: {result}")
except (TypeError, ValueError) as error:
    print(f"Handled error: {error}")
