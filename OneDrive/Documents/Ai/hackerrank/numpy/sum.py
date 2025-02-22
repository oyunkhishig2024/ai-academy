#you given 2-D array with dimensions N x M. Your task is to perform the sum tool over axis 0 and then find the product of that result.
#Input Format the first line contains space separated values of N and M. The next N lines contains M space separated integers.
#Output Format Compute the sum along axis 0. Then, print the product of that sum.
#Sample Input:
#2 2    

# you are given a 2-D array with dimensions N x M. Your task is to perform the sum tool over axis 0 and then find the product of that result.
# Input Format: The first line contains space-separated values of N and M. The next N lines contain M space-separated integers.
# Output Format: Compute the sum along axis 0. Then, print the product of that sum.

import numpy as np

# Read input
N, M = map(int, input().split())
array = np.array([list(map(int, input().split())) for _ in range(N)])

# Compute the sum along axis 0
sum_result = np.sum(array, axis=0)

# Compute the product of the sum
product_result = np.prod(sum_result)

# Print the result
print(product_result)