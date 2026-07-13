# Algorithm optimization, choosing the right approach

# Optimizing algorithms is like fine-tuning a machine, 
# ensuring it runs at its peak performance

# The importance of choosing the right data structures
# The adage "choosing the right tool for the job" 
# is especially true in the context of algorithm optimization

# Each data structure comes with its strengths and weaknesses, 
# making certain ones more suitable for specific tasks.

# E.g. while lists offer flexibility and ease of use, 
# their linear search performance can become an obstruction when dealing with massive datasets.

# hash tables excel at rapid lookups but might consume more memory

# Inefficient search in a list
my_list = [5, 2, 9, 1, 7]
search_item = 9
found = False
for item in my_list:
    if item == search_item:
        found = True
        break

# Efficient search using a dictionary
my_dict = {5: True, 2: True, 9: True, 1: True, 7: True}
found = my_dict.get(search_item, False)

# The pitfalls of nested loops

# Nested loops, where one loop resides within another, 
# can significantly impact an algorithm's time complexity.

# An approach with nested loops (often referred to as "naive recursion" or a "naive search") 
# would lead to a quadratic time complexity, making it increasingly sluggish as the list size grows

# A more optimized approach would involve techniques such as sorting the list first 
# or utilizing hash sets for efficient comparisons, reducing the time complexity to a more manageable level.

# Inefficient pairwise comparison with nested loops
my_list = [5, 2, 9, 1, 7]
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            print("Duplicate found!")

# Efficient pairwise comparison using a set
my_set = set()
for item in my_list:
    if item in my_set:
        print("Duplicate found!")
    else:
        my_set.add(item)

# This code uses a set to efficiently check for duplicates.
# It iterates through the list, adding each element to the set. 

# Memoization: Remembering for efficiency
# Memoization is a clever optimization technique that involves storing the results 
# of expensive function calls and reusing them when the same inputs occur again.

# This approach can drastically improve the performance of recursive algorithms, 
# which often involve redundant computations

# Essentially, memoization acts as a cache for your function calls.

# Naive recursive Fibonacci calculation
# A naive recursive implementation would lead to repeated calculations of the same Fibonacci numbers
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Memoized Fibonacci calculation
# Memoization temporarily stores results during program execution, 
# avoiding redundant computations within the same run but does not persist between program runs.
memo = {}
def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    memo[n] = result
    return result

# Example usage
print(fibonacci(10))        # Naive approach
print(fibonacci_memo(10))  # Memoized approach

# Counterarguments and considerations
# NOTE: it's essential to strike a balance between performance gains and code 
# Overly optimized code can become convoluted and difficult to maintain, 
# potentially hindering future modifications or debugging efforts

