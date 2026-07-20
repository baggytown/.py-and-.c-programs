try:
    print(o+2) #type:ignore
except NameError:
    print("Please define a varible")
finally:
    print("Thank you")