#Write a function that accepts a list and returns the largest element.
def list(i,t,r):
    p=[i,t,r]
    print(max(p))
list(i=int(input("Enter a number")),t=int(input("Enter a number")),r=int(input("Enter a number")))
#Create a function to check whether a string is a palindrome.
def pali(t):
    if t == t[::-1]:
        print("It is a palidrone")
    else:
        print("It is not")
pali(t=input("Enter a word"))
#Write a function that calculates the sum of all elements in a list.
def sum(x,y,z):
    l=[x,y,z]
    print(x+y+z)
sum(x=int(input("Enter a number")),y=int(input("Enter a number")),z=int(input("Enter a number")))
#Create a function using *args to find the average of numbers.
def args(*args):
    if not args:
        return 0
    return sum(args)/len(args)
print(args(10,29,17,246))
#Write a lambda function to cube a number.
c = lambda x: x ** 3
print(c)
