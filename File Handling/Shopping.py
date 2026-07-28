try:
    option=0
    while option!=10:
        print("=======================")
        print(" Welcome to the store")
        print("=======================")
        print("1. Add Product " )
        print("2. Display Products ")
        print("3. Search Product " )
        print("4. Update Product Price " )
        print("5. Delete Product " )
        print("6. Count Products " )
        print("7. Most Expensive Product ")
        print("8. Cheapest Product " )
        print("9. Generate Bill ")
        print("10. Exit")
        option=int(input("What will be your choice: "))
        if option == 1:
            f=open("Products.txt","w")
            o=input("What will be your product: ")
            op=input("What is the price(Whole nums pls): ")
            opd=input("What is the decimal: ")
            f.write(o)
            f.write( op)
            f.write( opd)
            f.close()
            print("Thank you")
        if option ==2:
            print("2")
except IndexError:
    print("Error")

