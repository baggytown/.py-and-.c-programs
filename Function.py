#Create a function that returns the maximum of two numbers.
def mx(t,i):
    if t>i:
        print(f"{t} is greater than {i}")
    elif i>t:
        print(f"{i} is greater than {t}")
    else:
        print("They are equal")
mx(t=int(input("Enter a number")),i=int(input("Enter another number")))

