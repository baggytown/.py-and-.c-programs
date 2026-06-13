#Create a function that counts vowels in a string.
def vowels(text,vowels,count):
    for char in text.lower():
        if char in vowels:
            count += 1
    print(count)
vowels(text=input("Enter a word"),vowels='aeiou',count=0)

