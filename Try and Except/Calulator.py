try:
    while grade!=101:
        f=f+1
        print("Set grade to 101 to end")
        grade=int(input("Test score:"))
        if grade >= 0 and grade<=30:
            print("Fail")
            s="Fail"
        if grade >= 30 and grade<=60:
            print("Meh")
            s="Meh"
        if grade >= 60 and grade<=80:
            print("Pass")
            s="Pass"
        if grade >= 80 and grade<=100:
            print("Great")
            s="Excelent grade"
        if grade == 101:
            print("Heres your recipt:")
            break
    for i, grade in enumerate(grade, start=1):
        print(f"Student {f} got {grade}")

except ValueError:
    print("Please enter a number")
finally:
    print("Thank you")
