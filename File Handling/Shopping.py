import os

try:
    option = 0
    while option != 10:
        print("=======================")
        print(" Welcome to the store")
        print("=======================")
        print("1. Add Product ")
        print("2. Display Products ")
        print("3. Search Product ")
        print("4. Update Product Price ")
        print("5. Delete Product ")
        print("6. Count Products ")
        print("7. Most Expensive Product ")
        print("8. Cheapest Product ")
        print("9. Generate Bill ")
        print("10. Exit")
        option = int(input("What will be your choice: "))  
        
        
        if not os.path.exists("Products.txt"):
            with open("Products.txt", "w") as f:
                pass

        if option == 1:
            o = input("What will be your product: ")
            op = input("What is the price (Whole nums pls): ")
            opd = input("What is the decimal: ")
            with open("Products.txt", "a") as f:
                f.write(o + " " + op + "." + opd + "\n") 
            print("Thank you") 
            
        elif option == 2:
            with open("Products.txt", "r") as f:
                content = f.read()
                if content.strip() == "":
                    print("Store is empty.")
                else:
                    print(content)
                    
        elif option == 3:
            i = input("Search: ")
            found = False
            with open("Products.txt", "r") as f:
                for line in f:
                    if i.lower() in line.lower():
                        print("Found:", line.strip())
                        found = True
            if not found:
                print("Product not found.")
                
        elif option == 4:
            product_to_update = input("Enter product name to update price: ")
            new_whole = input("Enter new whole price: ")
            new_decimal = input("Enter new decimal: ")
            new_price = f"{new_whole}.{new_decimal}"
            
            updated = False
            lines = []
            with open("Products.txt", "r") as f:
                lines = f.readlines()
                
            with open("Products.txt", "w") as f:
                for line in lines:
                    parts = line.strip().split()
                    if parts and parts[0].lower() == product_to_update.lower():
                        f.write(f"{parts[0]} {new_price}\n")
                        updated = True
                    else:
                        f.write(line)
            if updated:
                print("Price updated successfully!")
            else:
                print("Product not found.")
                
        elif option == 5:
            product_to_delete = input("Enter product name to delete: ")
            deleted = False
            lines = []
            with open("Products.txt", "r") as f:
                lines = f.readlines()
                
            with open("Products.txt", "w") as f:
                for line in lines:
                    parts = line.strip().split()
                    if parts and parts[0].lower() == product_to_delete.lower():
                        deleted = True
                        continue  
                    f.write(line)
            if deleted:
                print("Product deleted successfully!")
            else:
                print("Product not found.")
                
        elif option == 6:
            count = 0
            with open("Products.txt", "r") as f:
                for line in f:
                    if line.strip():
                        count += 1
            print(f"Total number of products: {count}")
            
        elif option == 7:
            highest_price = -1.0
            most_expensive = ""
            with open("Products.txt", "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        price = float(parts[1])
                        if price > highest_price:
                            highest_price = price
                            most_expensive = parts[0]
            if most_expensive:
                print(f"Most Expensive: {most_expensive} (${highest_price:.2f})")
            else:
                print("No products in store.")
                
        elif option == 8:
            lowest_price = float('inf')
            cheapest = ""
            with open("Products.txt", "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        price = float(parts[1])
                        if price < lowest_price:
                            lowest_price = price
                            cheapest = parts[0]
            if cheapest:
                print(f"Cheapest Product: {cheapest} (${lowest_price:.2f})")
            else:
                print("No products in store.")
                
        elif option == 9:
            bill_items = input("Enter product names to buy (separate with spaces): ").split()
            total_bill = 0.0
            found_any = False
            
            
            store_inventory = {}
            with open("Products.txt", "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        store_inventory[parts[0].lower()] = (parts[0], float(parts[1]))
            
            print("\n--- Receipt ---")
            for item in bill_items:
                if item.lower() in store_inventory:
                    name, price = store_inventory[item.lower()]
                    print(f"{name}: ${price:.2f}")
                    total_bill += price
                    found_any = True
                else:
                    print(f"Skipped '{item}' (Not found in store)")
            
            if found_any:
                print("---------------")
                print(f"Total Bill: ${total_bill:.2f}\n")
            else:
                print("No valid products were selected.\n")
                
        elif option == 10:
            print("Exiting store application. Goodbye!")
            
except IndexError:
    print("System index error occurred.")
except ValueError:
    print("Please enter a valid number or correct data format.")
