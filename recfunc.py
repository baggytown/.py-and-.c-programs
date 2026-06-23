#Write a recursive function to calculate the factorial of a number.
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
no=5
print(fact(no))
#Write a recursive function to find the nth Fibonacci number
def fib(r):
    if r <= 0:
        return 0
    elif r == 1:
        return 1

    return fib(r - 1) + fib(r - 2)
num=4
print(fib(num))
#Create a recursive function to calculate the sum of digits of a number.
def sum(n):
    if n == 0:
        return 0
    return (n % 10) + sum(n // 10)
print(sum(n=int(input("Enter a number"))))
#Reverse a string
def rev(s):
    if len(s) <= 1:
        return s
    return rev(s[1:]) + s[0]
print(rev("hello")) 
#Create a recursive function to compute the power of a number (a^b).
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
power(a=int(input('Enter a number')),b=int(input('Enter a number')))
#Implement a recursive binary search.
def binary(arr, tar, low, high):
    if low > high:
        return -1
        
    mid = (low + high) // 2
    
    if arr[mid] == tar:
        return mid
        
    elif arr[mid] > tar:
        return binary(arr, tar, low, mid - 1)
        
    else:
        return binary(arr, tar, mid + 1, high)
#Create a recursive function to find the greatest common divisor (GCD).
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(48, 18))
#Write a recursive function to count the number of digits in a number.
def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(12345))
print(count_digits(-7))
print(count_digits(0))
#Create a shopping cart program using functions and dictionaries.
def add_item(cart, item, price, quantity=1):
    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {"price": price, "quantity": quantity}


def remove_item(cart, item):
    if item in cart:
        del cart[item]


def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    total = 0
    for item, info in cart.items():
        subtotal = info["price"] * info["quantity"]
        total += subtotal
        print(
            f"{item}: {info['quantity']} x ${info['price']:.2f} = ${subtotal:.2f}"
        )
    print(f"Total: ${total:.2f}")


my_cart = {}

add_item(my_cart, "Laptop", 999.99)
add_item(my_cart, "Mouse", 25.50, 2)
add_item(my_cart, "Mouse", 25.50, 1)
view_cart(my_cart)

print("\nRemoving Laptop...")
remove_item(my_cart, "Laptop")
view_cart(my_cart)
#Build a menu-driven calculator using functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def calculator():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "5":
            print("Exiting calculator.")
            break

        if choice in ("1", "2", "3", "4"):
            try:
                num1, num2 = get_numbers()

                if choice == "1":
                    print(f"Result: {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("Invalid choice. Please select a valid option.")


calculator()



    