import numpy

def arrays(arr):
    np_array = numpy.array(arr, dtype=float)
    reversed_array = np_array[::-1]
    return reversed_array

# Get input and process the array
arr = input("Enter the array elements separated by spaces: ").strip().split()
reversed_arr = arrays(arr)

# Print the results
print("Original Array: ", arr)
print("Reversed Array: ", reversed_arr)
