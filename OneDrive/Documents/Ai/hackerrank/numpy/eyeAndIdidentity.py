#The identity tool returns an identity array. 
# An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0. 
# The default type of elements is float.
# import numpy
# print(numpy.identity(3)) # 3 is for dimension 3x3


#eye
#The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere.
#The diagonal can be main, upper or lower depending on the oprional K. 
# A positive k is for the upper diagonal, a negative k is for the lower, and 0 k (default) is for the main diagonal.
# import numpy
# print(numpy.eye(8,7, k = 1)) # 8x7 dimensional array with first upper diagonal 1.

#Task: print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else.
# In order to get alignment correct, insert numpy.set_printoptions(leagcy='1.13') below the numpy import
#input format: A single line containing the space seperated values of N(rows) and M(columns). Print desired NxM array.

import numpy as np

# Set print options for alignment
np.set_printoptions(legacy='1.13')

# Function to create the desired NxM array with diagonal elements as 1's
def create_diagonal_matrix(N, M):
    # Create an NxM array with 0's
    array = np.zeros((N, M))
    # Set the main diagonal elements to 1
    for i in range(min(N, M)):
        array[i, i] = 1
    return array

# Take input for the dimensions of the array
N, M = map(int, input("Enter the dimensions (N M): ").strip().split())


# Call the function to create the diagonal matrix
result = create_diagonal_matrix(N, M)

# Print the resulting array
print(result)




