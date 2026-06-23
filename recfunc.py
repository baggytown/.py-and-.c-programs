#Write a recursive function to calculate the factorial of a number.
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
no=5
print(fact(no))
#Write a recursive function to find the nth Fibonacci number
def fib(r):
    if r <= 0:
        return 0
    elif r == 1:
        return 1

    return fib(r - 1) + fib(r - 2)
num=4
print(fib(num))
#Create a recursive function to calculate the sum of digits of a number.
def sum(n):
    if n == 0:
        return 0
    return (n % 10) + sum(n // 10)
print(sum(n=int(input("Enter a number"))))
#Reverse a string
def rev(s):
    if len(s) <= 1:
        return s
    return rev(s[1:]) + s[0]
print(rev("hello")) 
#Create a recursive function to compute the power of a number (a^b).
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
power(a=int(input('Enter a number')),b=int(input('Enter a number')))
#Implement a recursive binary search.
def binary(arr, tar, low, high):
    if low > high:
        return -1
        
    mid = (low + high) // 2
    
    if arr[mid] == tar:
        return mid
        
    elif arr[mid] > tar:
        return binary(arr, tar, low, mid - 1)
        
    else:
        return binary(arr, tar, mid + 1, high)
#Create a recursive function to find the greatest common divisor (GCD).
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(48, 18))


    