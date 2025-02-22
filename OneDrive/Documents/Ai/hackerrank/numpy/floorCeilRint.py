# you are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.
import numpy as np

# Read input from standard input
A = np.array(list(map(float, input().split())))

# Set print options for better formatting
np.set_printoptions(legacy='1.13')

# Print floor, ceil, and rint of all elements in A
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))