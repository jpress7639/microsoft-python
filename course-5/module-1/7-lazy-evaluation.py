# Python generators: Lazy evaluation for efficiency

# Generators allow you to iterate over data without loading everything into memory at once.
# They are particularly useful when working with large datasets or streams of data.

# The Mechanics of Generators: 
# Generators are defined using functions and the yield statement.
# When the generator function encounters a yield statement, 
# it produces a value and pauses its execution, maintaining its state for the next iteration.

# Example:

def fibonacci_sequence():
	"""A generator that generates the Fibonacci sequence."""
	a, b = 0, 1
	while True:
		yield a # The yield a statement pauses the function and returns the current value of a.  
		a, b = b, a + b


# Generate the first 10 Fibonacci numbers
fib_gen = fibonacci_sequence()
for i in range(10): 
    print(next(fib_gen))   

# The lazy evaluation model of generators offers several key advantages:

# Memory Efficiency: Generators produce values on-the-fly, 
# which means they do not require the entire dataset to be stored in memory. 
# This is particularly beneficial when dealing with large datasets or streams of data.

# Improved Performance: Generators can improve performance by generating values only when they are needed,
# rather than computing all values upfront. This can lead to faster execution times, especially in scenarios
# where only a subset of the generated values is required.

# Simplified Code: Generators can lead to cleaner and more readable code,
# as they allow for the use of simple loops and yield statements instead of complex data structures or
# manual state management. This can make the code easier to understand and maintain.

# Infinite Sequences: Generators can produce infinite sequences of values without running out of memory,
# as they generate values on-the-fly. This is particularly useful for scenarios where the number
# of values to be generated is not known in advance or is potentially unbounded.

# Generators in Action:

# Data Processing Pipelines: Generators can be used to create pipelines for processing data in a memory-efficient manner.

# Real-time Data Streams: Generators can be used to process real-time data streams, such as sensor data or log files,
# without the need to load the entire stream into memory.

# Web Scraping: Generators can be used to scrape data from websites in a memory-efficient manner,
# allowing for the processing of large amounts of data without overwhelming system resources.

# Combinatorial Problems: Generators can be used to generate combinations or permutations of data on-the-fly,
# which can be particularly useful for solving combinatorial problems without the need to store all possible combinations

# As you become more comfortable with generators, you can explore more advanced techniques:

# Generator Expressions: Similar to list comprehensions, 
# generator expressions allow you to create generators in a concise and readable manner.

# Sending Values to Generators: Generators can receive values sent to them using the send() method,
# allowing for more dynamic and interactive behavior.
# This allows a two-way communication between the generator and the caller, enabling more complex data processing scenarios.

# Chaining Generators: You can chain multiple generators together to create complex data processing pipelines,
# allowing for the composition of multiple generator functions to achieve more sophisticated data transformations.