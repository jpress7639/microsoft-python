# Python powerhouses: Sets, deques, and heaps

# Data structures are the containers to store information in your program.

# Python provides several built-in data structures, 
# each with its own strengths and use cases. 
# In this guide, we will explore three powerful data structures: 
# sets, deques, and heaps.

# Sets - are an unordered collection of unique elements.
# They are useful for membership testing, removing duplicates, 
# and performing mathematical operations like union and intersection.
# Music streaming services are a great example of sets.
# Building a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6) # Output: {1, 2, 3, 4, 5, 6}
my_set.update([7, 8, 9]) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set.discard(3) # Output: {1, 2, 4, 5, 6, 7, 8, 9}

# If you were analyzing user preferences to recommend products,
# you could use a set to store the unique products a user has liked.

# Deques - are a double-ended queue that allows you to add 
# or remove elements from both ends efficiently.
# They are useful for implementing queues, stacks, and other data structures.

# Building a deque
from collections import deque # built-in module for deques - no need to pip install
my_deque = deque([1, 2, 3, 4, 5])

# Adding elements to a deque
my_deque.append(6) # Output: deque([1, 2, 3, 4, 5, 6])
my_deque.appendleft(0) # Output: deque([0, 1, 2, 3, 4, 5, 6])

# Removing elements from a deque
my_deque.pop() # Output: deque([0, 1, 2, 3, 4, 5])
my_deque.popleft() # Output: deque([1, 2, 3, 4, 5]) 
my_deque.remove(3) # Output: deque([1, 2, 4, 5])

# If you were implementing a task scheduler,
# you could use a deque to manage the tasks in a queue,
# allowing you to add new tasks to the front or back of the queue as needed.

# Heaps - are a specialized tree-based data structure that satisfies the heap property.
# In a min-heap, for any given node, the value of that node is less
# than or equal to the values of its children, 

# while in a max-heap,the value of that node is 
# greater than or equal to the values of its children.

# Heaps are useful for implementing priority queues,
# where elements with higher priority are served before elements with lower priority.

# Building a heap
import heapq # built-in module for heaps - no need to pip install
my_heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(my_heap) # Output: [1, 1, 2, 3, 5, 9, 4, 6, 5, 3, 5]

# Adding elements to a heap
heapq.heappush(my_heap, 0) # Output: [0, 1, 1, 3, 5, 9, 2, 6, 5, 3, 5, 4]
# Removing the smallest element from a heap
smallest = heapq.heappop(my_heap) # Output: 0
# my_heap after removing the smallest element: [1, 1, 2, 3, 5, 9, 4, 6, 5, 3, 5]