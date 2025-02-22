

#Task: You are given two integer arrays, A and B of dimensions N x M. Your task is to perform the following operations:
# 1. Add(A + B)
# 2. Subtract(A - B)
# 3. Multiply(A * B)
# 4. Division(A / B)
# 5. Mod(A % B)
# 6. Power(A ** B)

import numpy as np

# Create arrays with integer type
a = np.array([[1, 2, 3, 4]], int)
b = np.array([[5, 6, 7, 8]], int)

# Perform the operations
add_result = np.add(a, b)
subtract_result = np.subtract(a, b)
multiply_result = np.multiply(a, b)
division_result = np.floor_divide(a, b)  # Use floor division for integer division
mod_result = np.mod(a, b)
power_result = np.power(a, b)

# Print the results
print(add_result)
print(subtract_result)
print(multiply_result)
print(division_result)
print(mod_result)
print(power_result)


