import math
leave=0
while leave != 3:
    ty=int(input("IF you want Area then press one Other wise for peimeter press 2"))
    thing=int(input("If you want do use a rectangle then press 1, If you want a Triangle then press 2, if you want a circle press 3, if you want a sqaure then press 4"))
    if ty == 1:
        if thing == 1:
            no=int(input("What is the length"))
            noo=int(input("What is the width"))
            print(no*noo)
        if thing == 2:
            base=int(input("What is the base"))
            height=int(input("What is the height"))
            multi=base*height
            print(multi/2)
        if thing == 3:
            r=int(input("What is the radius"))
            print(math.pi*r*r)
        if thing == 4:
            num=int(input("What is the side length"))
            print(num*num)    
    if ty == 2:
        if thing == 1:
            no=int(input("What is the length"))
            noo=int(input("What is the width"))
            print(no+noo+noo+no)
        elif thing == 2:
            one=int(input("Length of first side"))
            two=int(input("Length of second side"))
            three=int(input("Length of third side"))
            print(one+two+three)
        elif thing == 3:
            ra=int(input("What is the Radius"))
            print(2*math.pi*ra)
        elif thing == 4 :
            numm=int(input("What is the side lenght"))
            print(numm+numm+numm+numm)    
    leave=int(input("If you want to leave then press 3 other wise press any other number"))