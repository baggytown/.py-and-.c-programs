d={}
s='Hi'
while s != 4:
    print("==============================")
    print("  Hello, welcome to Walmart")
    print("==============================")
    print(' ')
    print('1)add item')
    print('2)remove item')
    print('3)display cart')
    print('4)end')
    s=int(input("what will you chose: "))

    if s==1:
        p=input('what will you add: ')
        w=int(input('how many: '))
        
        d[p] = d.get(p, 0) + w
    if s==2:
        l=input('What do you want to remove: ')
        if l in d:
            f=int(input('How much: ')) 
            d[l] = d[l] - f
            if d[l] <= 0:
                del d[l]
        else:
            print("Item not found in cart.")
    if s==3:
        print(d)


