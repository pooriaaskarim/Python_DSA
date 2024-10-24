# # # Tuples Creation
# Creating an empty tuple
empty_tuple = ()

# Tuple with mixed data types
mixed_tuple = (1, "Python", 3.14, True)

# Tuple of numbers
numbers_tuple = (1, 2, 3, 4, 5)

# Tuple of strings
fruits_tuple = ("apple", "banana", "cherry", "date")

# Tuple using the tuple constructor
tuple_constructor = tuple([10, 20, 30, 40])  # Convert a list to a tuple

# Tuple from a string (creates a tuple of characters)
char_tuple = tuple("hello")

print("Empty Tuple:", empty_tuple)
print("Mixed Tuple:", mixed_tuple)
print("Numbers Tuple:", numbers_tuple)
print("Fruits Tuple:", fruits_tuple)
print("Tuple from Constructor:", tuple_constructor)
print("Tuple from String:", char_tuple)

# # # Tuple Operations

numbers_tuple = (10, 20, 30, 40, 50)

# Accessing elements by index
first = numbers_tuple[0]  # First element
last = numbers_tuple[-1]  # Last element

# Slicing a tuple (getting a sub-tuple)
sub_tuple = numbers_tuple[1:4]  # (20, 30, 40)

# Checking if an element is in the tuple
is_present = 30 in numbers_tuple  # True

# Length of the tuple
length = len(numbers_tuple)

print("\nOriginal Tuple:", numbers_tuple)
print("First Element:", first)
print("Last Element:", last)
print("Subtuple (1:4):", sub_tuple)
print("Is 30 present in the tuple?", is_present)
print("Length of the Tuple:", length)

# # # Tuple Immutability

# Tuples are immutable, so you cannot modify or add elements directly.
# However, you can demonstrate immutability by attempting to modify or perform invalid operations:

numbers_tuple = [100, 200, 300, 400]
print("\nOriginal Tuple:", numbers_tuple)

# Attempting to modify an element (will raise a TypeError)
try:
    numbers_tuple[2] = 350  # Trying to change 300 to 350 (INVALID)
except TypeError as e:
    print("Error:", e)

# Attempting to append elements (will raise a TypeError)
try:
    numbers_tuple.append(500)  # Trying to append 500 (INVALID)
except AttributeError as e:
    print("Error:", e)

# However, you can create new tuples based on existing ones
new_tuple = numbers_tuple + 500  # Create a new tuple by concatenation
print("New Tuple after concatenation:", new_tuple)

# Sorting does not work in-place with tuples (because they are immutable),
# but you can return a sorted version of the tuple using the `sorted()` function.
sorted_tuple = tuple(sorted(numbers_tuple))
print("Sorted Tuple (new object):", sorted_tuple)


# Tuples are passed by reference in functions, but you cannot modify the original tuple:
def modify_tuple(tpl):
    # Cannot modify tuple elements, but you can create and return a new tuple
    return (999,) + tpl[1:]


new_numbers_tuple = modify_tuple(numbers_tuple)
print("New Tuple after trying to modify inside function:", new_numbers_tuple)