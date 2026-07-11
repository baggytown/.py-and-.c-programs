no=0
while no <5:
    try:
        print("Calculator")
        print("1) Add")
        print("2) Subtract")
        print("3) Multiply")
        print("4) Divide")
        print("5) Exit")
        no=int(input("Enter Your Choice"))
        if no == 1:
            n=int(input("Enter Your First Number"))
            o=int(input("Enter Your Second Number"))
            print(n+o)
        elif no == 2:
            n=int(input("Enter Your First Number"))
            o=int(input("Enter Your Second Number"))
            print(n-o)
        elif no == 3:
            n=int(input("Enter Your First Number"))
            o=int(input("Enter Your Second Number"))
            print(n*o)
        elif no == 4:
            n=int(input("Enter Your First Number"))
            o=int(input("Enter Your Second Number"))
            print(n/o)
        elif no == 5:
            print("Bye!")
        else:
            print("Please try again")
    except ValueError:
        print("Invalid Character")
    except ZeroDivisionError:
        print("No dividing by zero")
    finally:
        print("Thank you")