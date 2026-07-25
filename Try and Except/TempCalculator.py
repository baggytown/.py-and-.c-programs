try:
    end=140000
    while end>0:
        temp=int(input("Please enter your temp"))
        r = input("Do you want to leave (Y\\N) (Capitals only): ")
        fc=input("Is it Fahrenheit or Celsius (F\C)")
        if fc == "F" or fc == "f":
            print("The value in celsius is {(temp-32)*5/9}")
        if fc == "C" or fc == "c":
            print("The value in fahrenheit is {(temp*9/5)+32}")
        if r == "Y":
            break
        else:
            continue
except TypeError:

    print("Please enter the right data type")
finally:
    print("Thank you")