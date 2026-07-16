balance = 500.0

try:
    while True:
        print(f"\nCurrent Balance: ${balance:.2f}")
        choice = input("1. Deposit | 2. Withdraw | 3. Exit: ").strip()

        if choice == "3":
            break

        if choice not in ("1", "2"):
            raise ValueError("Please select a valid option from the menu")

        amount = float(input("Enter amount: "))

        if amount <= 0:
            raise ValueError("Please enter an amount greater than zero")

        if choice == "1":
            balance += amount
            print(f"Success! Deposited: ${amount:.2f}")

        elif choice == "2":
            if amount > balance:
                raise IndexError("Please ensure you have enough funds for this transaction")
            balance -= amount
            print(f"Success! Withdrew: ${amount:.2f}")

except ValueError as error:
    print(f"Input Error: {error}")

except IndexError as error:
    print(f"Balance Error: {error}")

finally:
    print("Thank you for using our banking application")
