try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity < 0:
        print("Numbers must be positive.")
    else:
        subtotal = price * quantity
        tax = subtotal * 0.13
        total = subtotal + tax

        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")

except ValueError:
    print("Error: Please enter numbers only.")
