import numpy as np

# Example array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Find the minimum value in the array
min_value = np.min(array)

# Find the maximum value in the array
max_value = np.max(array)

# Print the results
print("Minimum value:", min_value)
print("Maximum value:", max_value)

#Task: you are give 2-D array with dimensions N x M. Your task is to perform the min function over axis 1 and then find the max of that.
#Input Format: The first line of input contains the space separated values of N and M. The next N lines contains M space separated integers.