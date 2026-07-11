import random

print("===================")
print("  The Door game")
print("===================")
print("Instructions:")
print("There will be 4 options, 1, 2, 3, and 4. If you enter the right one, you win!, if you don't, you lose.")
print("option 1 = door 1")
print("option 2 = door 2")
print("option 3 = door 3")
print("option 4 = door 4")
print("option 5 = exit")

playing = True

while playing:
    r = random.randint(1, 4)
    user_choice = int(input("Enter your choice. Please enter the number shown: "))
    
    if user_choice == 5:
        print("Bye!")
        playing = False
        
    elif user_choice == r:
        print("You Won! Would you like to play again?")
        o = input("Yes or No: ")
        if o.lower() == "no":
            print("Bye!")
            playing = False
        else:
            print("Okay!")

    elif 1 <= user_choice <= 4:
        print("You lost -_- Would you like to play again?")
        t = input("Yes or No: ")
        if t.lower() == "no":
            print("Bye!")
            playing = False
        else:
            print("Okay!")
            
    else:
        print("Invalid input! Please enter a number between 1 and 5.")

