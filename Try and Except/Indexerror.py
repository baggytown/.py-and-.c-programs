try:
    lists=[0,1,2,3,4,5,6,7,8,9]
    print(lists)
    inp=int(input("Enter the value of a number on the list"))
    print(lists[inp])
except IndexError:
    print("Not a valid number")
finally:
    print("Thank you")