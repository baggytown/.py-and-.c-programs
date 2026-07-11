# Create a List of Even Numbers
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print("Even numbers:", even_numbers)

# Convert Strings to Uppercase
lowercase_strings = ["hello", "world", "python"]
uppercase_strings = [text.upper() for text in lowercase_strings]
print("Uppercase strings:", uppercase_strings)

# Find Length of Each Word
words = ["apple", "banana", "cherry"]
word_lengths = [len(word) for word in words]
print("Word lengths:", word_lengths)

# Display the First Character
items = ["Python", "Java", "C++"]
first_chars = [item[0] for item in items]
print("First characters:", first_chars)

# Creating a List from Another List
original_list = [1, 2, 3, 4, 5]
new_list = [x * 2 for x in original_list]
print("New list (doubled):", new_list)

# Find Common Elements Between Two Lists
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
common_elements = [item for item in list_a if item in list_b]
print("Common elements:", common_elements)

# Create Multiplication Table of 5
multiplication_table = [5 * i for i in range(1, 11)]
print("Multiplication table of 5:", multiplication_table)