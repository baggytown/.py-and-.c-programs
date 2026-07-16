try:
    l=43
    print(l.append(3))
except AttributeError:
    print("Please use proper atributes for certin things")
finally:
    print("Thank you")