# ESSENTIAL LIBRARIES FOR DATA ANALYSIS

# NumPy
# An ndarray is a multidimensional container capable of housing numerical data of various types, 
# from integers and floating-point numbers to complex numbers

# Vectorization - allowing you to replace explicit loops with concise array-wide operations. 
# makes your code more readable but also significantly boosts its efficiency, especially when dealing with large datasets.

import numpy as np

prices = np.array([100, 105, 112, 98]) 
percentage_change = (prices[1:] - prices[:-1]) / prices[:-1] * 100

# NumPy handles the entire calculation in a single, optimized operation, 
# significantly outperforming the loop-based approach.

# Need to be cautious of broadcasting rules 
# if you want to perform a simple add - it'll lead to unexpected errors as it'll scalar to each element 

# Broadcasting - that simplifies operations between arrays of different shapes

# Pitfalls of Broadcasting
# Broadcasting works seamlessly when the trailing dimensions of the arrays are either equal or one of them is 1. 
# If these conditions aren't met, you'll encounter a ValueError. 

import numpy as np

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])  # Shape: (2, 3)
arr2 = np.array([10, 20])       # Shape: (2,)

result = arr1 + arr2  # ValueError: operands could not be broadcast together with shapes (2,3) (2,)

# broadcasting fails because the trailing dimensions (3 and 1, implicitly) don't match. 
# To fix this, we can reshape arr2 to have a compatible shape:  

arr2_reshaped = arr2.reshape(2, 1)  # Shape: (2, 1)

# arr2_reshaped to 2 rows, 1 column:
#[[10]
# [20]]
print(arr2_reshaped) 

result = arr1 + arr2_reshaped # Successful

# First row of arr1 gets 10 added to each value
# second row of arr1 gets 20 added to each value
print(result)
# [[11 12 13]
#  [24 25 26]]

# Misaligned Dimensions - the alignment of dimensions is key 
# operates on the trailing dimensions (from the right),
# so ensure the dimensions you intend to broadcast align properly. 

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]]) # Shape: (2, 3)

arr2 = np.array([10, 20]) # Shape: (2,)

result = arr1 + arr2 # ValueError

# To align the dimensions correctly you can introduce a new axis with np.newaxis

arr2_newaxis = arr2[:, np.newaxis] # Shape: (2, 1)

result = arr1 + arr2_newaxis # Shape: (2, 3)

# This works because arr2_newaxis (shape (2, 1)) aligns with arr1 (shape (2, 3)): 
# the 2 matches, and 1 stretches to 3, yielding:

# [[11 12 13]
# [24 25 26]]

# functions reshape() and np.newaxis are your allies in adjusting array shapes to enable broadcasting. 

# Mathematical arsenal: Beware of silent values
# extensive mathematical functions are invaluable, but they can also silently return incorrect results under certain conditions
# consider calculating the sum of a large number of small floating-point values:
# Create an array of one million elements, each containing 0.1
small_values = np.full(1000000, 0.1)

# Summing one million .1 values should yield 100,000
sum_value = np.sum(small_values)

# Results in an incorrect value (99999.9999999998)
print(sum_value)

# If doing this is critical, you can consider using alternative numerical representations or techniques.
# you can investigate specialized Python libraries, using fixed-point arithmetic, or algorithms such as Kahan summations.

# Pandas 
# With its elegant Series and DataFrame structures, 
# pandas is your toolkit for crafting refined datasets ready for analysis.

# it has its own quirks and idiosyncrasies

# Intuitive indexing - can lead to confiusion between explicit indexing (iloc) or label-based indexing (loc)
# Data alignment - assumes that DataFrames share common labels
# if labels are mismatched or missing, calculations may be performed with incorrect values
# Missing data handling - imputing missing values can introduce bias if not done thoughtfully

# Aggregation and transformation: pandas can sometimes modify DataFrames in place, 
# leading to unintended side effects

# Matplotlib
# object-oriented approach offers granular control over every aspect of your visualizations

# Layered approach - Mastering the art of creating a simple plot might take time and practice
# Consider breaking down complex visualizations into multiple subplots 

# Customization galore - "Less is more" - prioritize clarity over complexity 

# Integration - version conflicts between tools can occur - keep libraries up-to-date 
# Be prepared to troubleshoot

