try:
    no=int(input("Enter a number"))
    no=100/no
    print(no)
except ZeroDivisionError:
    print("You can not divide by zero")
except ValueError:
    print("Please enter a number")
else:
    print("The program ran")
finally:
    print("Thank you")
