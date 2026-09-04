try:
    print(o+2) #type:ignore
except NameError:
    print("Please define a variable")
finally:
    print("Thank you")