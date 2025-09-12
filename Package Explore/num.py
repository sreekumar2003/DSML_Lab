import numpy as np

data = np.random.randint(1, 100, size=(5, 3))
print("Original Dataset:\n", data)

# Basic stats
print("Sum of all elements:", np.sum(data))
print("Mean of each column:", np.mean(data, axis=0))

# Reshaping the array
reshaped_data = data.reshape(3, 5)
print("\nReshaped Dataset:\n", reshaped_data)


print("\nTransposed Dataset:\n", data.T)

# Element-wise addition of a scalar
data_plus_10 = data + 10
print("\nDataset after adding 10:\n", data_plus_10)

# Matrix multiplication (Dot product)
another_data = np.random.randint(1, 100, size=(3, 5))
dot_product = np.dot(data.T, another_data.T)
print("\nDot Product of Transposed Matrices:\n", dot_product)
