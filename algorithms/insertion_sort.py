# Pseudo Code
# The pseudocode for insertion sort is given as the procedure INSERTION-SORT,
# takes two parameters: an array A containing the values to
# be sorted and the number n of values of sort. The values occupy positions A[1]
# through A[n] of the array, which we denote by A[1, n]. When the INSERTION-SORT
# procedure is finished, array A[1, n] contains the original values, but in sorted
# order.
# INSERTION-SORT(A, n)
# for i = 2 to n
#   key = A[i]
#   // Insert A[i] into the sorted subarray A[1:i-1].
#   j = i - 1
#   while j > 0 and A[j] > key
#       A[j+1] = A[j]
#       j = j - 1
#   A[j+1] key

def insertion_sort(A: list):
    n = len(A)  # Get the n of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = A[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < A[j]:  # Move elements greater than key one position ahead
            A[j + 1] = A[j]  # Shift elements to the right
            j -= 1

        A[j + 1] = key  # Insert the key in the correct position


# Sorting and array of random numbers with length n using insertion_sort

import random

n = 6
array = [random.randint(-1000, 1000) for i in range(n)]  # Generate a list of n random integers

print(f'''
    Unsorted Array:
        {array}''')
insertion_sort(array)
print(f'''
    Sorted Array:
        {array}'''
      )