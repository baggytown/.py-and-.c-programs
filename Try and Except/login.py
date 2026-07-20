end=0
try:
    u="hi"
    p="Bye"
    up="i"
    pp="i"
    co=u
    cop=p
    y=0
    while y!=5:
        print("Please enter a string")
        f=input("Forgot Username or password?: Yeas or no")
        u=input("Please enter your Username or Email:")
        p=input("Enter your password:")
        if not isinstance(u, str):
            print("Invalid username")
            y=1
        elif not isinstance(p,str):
            print("Invalid password")
            y=2
        elif u!=up:
            print("Invalid username")
            y=3
        elif p!=pp:
            print("Invalid password")
            y=4
        else:
            y=5
        while end!=2:
            print("Would you like to change your username and password,then type in 1")
            print("If you would like to exit please enter 2")
            i=int(input("What would u like to chose"))
            end=i
            if end == 1:
                c=input("Pls enter your new username")
                cp=input("Pls enter ur new password")
                print("Thank you")
                up=c
                pp=cp
                co=u
                cop=p
            if end == 2:
                break
except ZeroDivisionError:
    print("")
finally:
    print("")

    





