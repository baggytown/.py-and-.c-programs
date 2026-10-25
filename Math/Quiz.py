import random
import math
try:
    print("Welcome To The Greatest Math Quiz In The World")
    end = int(input("How many questions? "))

    for i in range(end):
        firstnum = random.randint(1, 100)
        secondnum = random.randint(1, 100)
        opera = random.randint(1, 6)

        if opera == 1:
            p = int(input(f"Solve this: {firstnum} + {secondnum} = "))
            m = firstnum + secondnum
            if p == m:
                print("Correct!!!\n")
            else:
                print(f"Incorrect. The correct answer was {m}.\n")
        elif opera == 2:
            p = int(input(f"Solve this: {firstnum} - {secondnum} = "))
            m = firstnum - secondnum
            if p == m:
                print("Correct!!!\n")
            else:
                print(f"Incorrect. The correct answer was {m}.\n")
        elif opera == 3:
            p = int(input(f"Solve this: {firstnum}* {secondnum}= "))
            m = firstnum * secondnum
            if p == m:
                print("Correct!!!\n")
            else:
                print(f"Incorrect. The corect answer is {m}")
        elif opera == 4:
            m = firstnum / secondnum
            if isinstance(m,bool):
                print("Round up") 
                p = int(input(f"Solve this: {firstnum} /{secondnum} = "))      
                m=math.ceil(m)
                if p == m:
                    print("Correct!!!\n")
                else:
                    print(f"Incorrect. The correct answer was {m}.\n")
        elif opera == 5:
            p = int(input(f"Solve this: {firstnum}^ {secondnum} = "))
            m = math.s
            if p == m:
                print("Correct!!!\n")
            else:
                print(f"Incorrect. The correct answer was {m}.\n")
        elif opera == 6:
            la = random.randint(1, 2)
            if la == 1:
                p = int(input(f"Solve this: {firstnum*firstnum} square root = "))
                sq = firstnum * firstnum
                m = math.sqrt(sq)
                if p==m:
                    print("Correct!!!!!\n")
                elif p!=m:
                    print(f"Incorrect. The correct answer was {m}")
            elif la == 2:
                p = int(input(f"Solve this: {secondnum*secondnum} square root = "))
                sq = secondnum*secondnum
                m = math.sqrt(sq)
                if p==m:
                    print("Correct!!!!!\n")
                elif p!=m:
                    print(f"Incorrect. The correct answer was {m}")
            else:
                print("Error")
        else:
            print("Error")
except ValueError:
    print("Please enter a valid number!")
except Exception as e:
    print(f"An error occurred: {e}")