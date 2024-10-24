# # # Lists Creation
# Creating an empty list
empty_list = []

# List with mixed data types
mixed_list = [1, "Python", 3.14, True]

# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry", "date"]

# List using the list constructor
list_constructor = list((10, 20, 30, 40))  # Convert a tuple to a list

# List from a string (creates a list of characters)
char_list = list("hello")

print("Empty List:", empty_list)
print("Mixed List:", mixed_list)
print("Numbers:", numbers)
print("Fruits:", fruits)
print("List from Constructor:", list_constructor)
print("List from String:", char_list)

# # # List Operations

numbers = [10, 20, 30, 40, 50]

# Accessing elements by index
first = numbers[0]  # First element
last = numbers[-1]  # Last element

# Slicing a list (getting a sublist)
sublist = numbers[1:4]  # [20, 30, 40]

# Modifying elements
numbers[1] = 25  # Change 20 to 25

# Adding elements
numbers.append(60)  # Add 60 at the end

# Inserting elements at a specific position
numbers.insert(2, 35)  # Insert 35 at index 2

# Removing elements
numbers.remove(40)  # Removes the first occurrence of 40

# Popping elements (removes and returns the last element)
popped_element = numbers.pop()  # Removes 60

# Checking if an element is in the list
is_present = 30 in numbers  # True

# Length of the list
length = len(numbers)

print("\nOriginal List:", numbers)
print("First Element:", first)
print("Last Element:", last)
print("Sublist (1:4):", sublist)
print("List after modification and additions:", numbers)
print("Popped Element:", popped_element)
print("Is 30 present in the list?", is_present)
print("Length of the List:", length)

# # # List Mutability

# Mutability: lists can be modified in place
numbers = [100, 200, 300, 400]
print("\nOriginal List:", numbers)

# Modifying an element
numbers[2] = 350  # Change 300 to 350
print("After modifying index 2:", numbers)

# Adding elements (mutating the list)
numbers.append(500)
print("After appending 500:", numbers)

# Sorting the list in place (mutates the list)
numbers.sort()
print("After sorting the list:", numbers)

# Mutating through aliasing (demonstrating references to the same object)
alias = numbers
alias[1] = 250  # Modify alias, it affects 'numbers' because they point to the same list
print("After modifying alias:", alias)
print("Numbers after modifying alias (because of mutability):", numbers)

# Demonstrating that lists are passed by reference in functions
def modify_list(lst):
    lst[0] = 999  # Modify the first element

modify_list(numbers)
print("After modifying list inside a function:", numbers)