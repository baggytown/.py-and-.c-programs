#Handle invalid integer input using ValueError.
try:
    no=int(input("Enter a number"))
    no=no*2
    print(no)
except ValueError:
    print("Invalid character")
finally:
    print("Thank you")
