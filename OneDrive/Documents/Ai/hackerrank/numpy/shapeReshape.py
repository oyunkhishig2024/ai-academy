# You are given a space seperated list of nine integers. Your task is to convert this list into 3x3 NumPy array.
#Input Format: A single line of input containing 9 space seperated integers.


import numpy as np

def converted(input_string):
    # Convert input string to a list of integers
    numbers = list(map(int, input_string.split()))
    # Convert list to NumPy array and reshape
    np_array = np.array(numbers).reshape(3, 3)
    return np_array

input_string = input("Enter the array elements separated by spaces: ")
result = converted(input_string)

print("Original Array: ", input_string.split())
print("Reversed and Reshaped Array:")
print(result)



   