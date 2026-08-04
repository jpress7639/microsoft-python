# Revisiting common data structures: Lists, dictionaries, and sets

# Lists - ordered, mutable collections of items
# NOTE: Lists are best used when you need to maintain the order of items,
# such as in a to-do list or a sequence of steps in a process.
my_list = [1, 2, 3, 4]
my_list.append(5)  # Adding an element
my_list.remove(2)  # Removing an element
my_list[0] = 10  # Modifying an element

# Other list operations
my_list.extend([6, 7])  # Adding multiple elements
my_list.pop(1)  # Removing an element by index

# Lists vs Arrays: 
# Lists can hold items of different types, 
# while arrays (from the array module) are more efficient 
# for large collections of numeric data.

# They are mutable - you can change their contents after creation
print("List:", my_list)  # Output: List: [1, 3, 4, 5]

# Dictionaries - unordered, mutable collections of key-value pairs
# NOTE:Dictionaries are best used when you need to associate unique keys with values,
# such as in a phone book or a database of user information.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4  # Adding a key-value pair
del my_dict['b']  # Removing a key-value pair
my_dict['a'] = 10  # Modifying a value

# Other dictionary operations
my_dict.update({'e': 5, 'f': 6})  # Adding multiple key-value pairs
my_dict.pop('c')  # Removing a key-value pair and returning its value

# They are mutable - you can change their contents after creation
print("Dictionary:", my_dict)  # Output: Dictionary: {'a': 10, 'c': 3, 'd': 4}  

# Sets - unordered collections of unique items
# NOTE: Sets are best used when you need to store unique items and perform operations 
# like union, intersection, and difference,
# such as in a collection of tags or a list of unique user IDs.
my_set = {1, 2, 3, 4}
my_set.add(5)  # Adding an element
my_set.remove(2)  # Removing an element

# Other set operations
my_set.update([6, 7])  # Adding multiple elements
my_set.discard(3)  # Removing an element if it exists


# They are mutable - you can change their contents after creation
print("Set:", my_set)  # Output: Set: {1, 3, 4, 5} 

# Exploring Advanced Data Structures: Stacks and Queues

# Stacks - Last In First Out (LIFO) data structure
# Stacks are often implemented using lists in Python, 
# where the append() method is used to push an item onto the stack, 
# and the pop() method is used to remove the top item from the stack.

# NOTE: Stacks are best used when you need to reverse the order of items,
# such as in depth-first search algorithms or undo functionality in applications.
# Real-life examples of stacks include a stack of plates, a stack of books, or a call stack in programming.
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print("Stack before pop:", stack)  # Output: Stack before pop: [1, 2, 3]
stack.pop()  # Pop
print("Stack after pop:", stack)  # Output: Stack after pop: [1, 2]

# Other stack operations
stack.append(4)
print("Stack after pushing 4:", stack)  # Output: Stack after pushing 4: [1, 2, 4]
top_item = stack[-1]  # Peek
print("Top item of the stack:", top_item)  # Output: Top item of the stack: 4

stack.append(5)  # Push
top_item = stack[-1]  # Peek - checks the top item without removing it
print("Top item after pushing 5:", top_item)  # Output: Top item after pushing 5: 5
is_empty = len(stack) == 0  # Checks if the stack is empty
print("Is the stack empty?", is_empty)  # Output: Is the stack empty? False

# Using 'collections.deque' for stack implementation
# The 'collections.deque' class can also be used to implement a stack,
# providing efficient O(1) time complexity for append and pop operations.
from collections import deque
stack_deque = deque()
stack_deque.append(1)  # Push
stack_deque.append(2)
stack_deque.append(3)
print("Stack (deque) before pop:", stack_deque)  # Output: Stack (deque) before pop: deque([1, 2, 3])
stack_deque.pop()  # Pop
print("Stack (deque) after pop:", stack_deque)  # Output: Stack (deque) after pop: deque([1, 2])

# Backtracking algorithms - are used to solve problems by 
# exploring all possible solutions and backtracking when a solution 
# is not feasible. Stacks are often used in backtracking algorithms to keep 
# track of the current state and previous states.

# Example of a backtracking algorithm: solving a maze
# In a maze, you can use a stack to keep track of the path taken.
# Code Example:
def solve_maze(maze, start, end):
    stack = []
    stack.append(start)
    visited = set()
    visited.add(start)

    while stack:
        current_position = stack.pop()
        if current_position == end:
            return True  # Maze solved

        # Get possible moves (up, down, left, right)
        for move in get_possible_moves(maze, current_position):
            if move not in visited:
                visited.add(move)
                stack.append(move)

    return False  # No solution found

def get_possible_moves(maze, position):
    # This function would return a list of valid moves from the current position
    # For simplicity, let's assume it returns an empty list here
    return []


# Queues - First In First Out (FIFO) data structure
# Just like a line in a store, the first person to enter the line is the first one to be served.
# Queues can be implemented using the collections.deque class in Python,
# which provides an efficient way to append and pop items from both ends.

# NOTE: Queues are best used when you need to process items in the order they were added,
# such as in breadth-first search algorithms or task scheduling.
from collections import deque
queue = deque()
queue.append(1)  # Enqueue - adds an element to the back of the queue
queue.append(2)
queue.append(3)
print("Queue before dequeue:", queue)  # Output: Queue before dequeue: deque([1, 2, 3])
queue.popleft()  # Dequeue - removes and returns the front element of the queue
print("Queue after dequeue:", queue)  # Output: Queue after dequeue: deque([2, 3])

# Other queue operations
queue.append(4)
print("Queue after enqueueing 4:", queue)  # Output: Queue after enqueueing 4: deque([2, 3, 4])
front_item = queue[0]  # Peek
print("Front item of the queue:", front_item)  # Output: Front item of the queue: 2

# Linked lists - a linear data structure where 
# each element (node) contains a reference (link) to the next node 
# in the sequence.

# Imagine a chain where each link securely holds a piece of data and points to the next link in the chain.
# NOTE: Linked lists are best used when you need to efficiently 
# insert or remove elements from the middle of the list, 
# such as in a music playlist or a navigation system.

# Each node has two components:
# 1) data: the value stored in the node
# 2) next: a reference to the next node in the list

# Code Example:
class Node: # this is a class that represents a single node in a linked list
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: # this is a class that represents a linked list, which is a collection of nodes
    def __init__(self):
        self.head = None

    def append(self, data): # this method adds a new node with the given data to the end of the linked list
        new_node = Node(data) # create a new node with the given data
        if not self.head: # if the linked list is empty, set the new node as the head of the list
            self.head = new_node
            return
        last_node = self.head # start from the head of the list
        while last_node.next: # traverse the list until the last node is reached
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self): # this method prints the data of each node in the linked list
        current_node = self.head
        while current_node: # traverse the list until the end is reached
            print(current_node.data, end=" -> ")
            current_node = current_node.next # move to the next node
        print("None") # indicates the end of the list

# Inserting and deleting elements in a linked list can be done 
# in O(1) time if you have a reference to the node,
# but finding a specific element requires O(n) time, 
# as you may need to traverse the entire list.

# Example usage of the LinkedList class
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()  # Output: 1 -> 2 -> 3 -> None
# Removing elements from a linked list requires 
# updating the next reference of the previous node to 
# skip over the node to be removed.

linked_list.head.next = linked_list.head.next.next  # Remove the second node (value 2)
linked_list.print_list()  # Output: 1 -> 3 -> None

# Trees: Branching out for efficiency
# Trees are hierarchical data structures that consist of nodes connected by edges.
# Each node contains a value and references to its child nodes.
# The topmost node is called the root, and nodes with no children are called leaves.

# Trees are exceptional at:
# Hierarchical data representation (e.g., file systems, organizational charts)
# Efficient searching and sorting (e.g., binary search trees)

# Code Example:
class TreeNode: # this is a class that represents a single node in a tree
    def __init__(self, data):
        self.data = data
        self.children = []  # list to hold child nodes

    def add_child(self, child_node): # this method adds a child node to the current node
        self.children.append(child_node)

    def print_tree(self, level=0): # this method prints the tree structure starting from the current node
        print(" " * level * 2 + str(self.data)) # print the current node's data with indentation based on its level
        for child in self.children: # recursively print each child node
            child.print_tree(level + 1)

# Each node has at most two children
# Left subtree property: All values in the left subtree are less than the node's value
# Right subtree property: All values in the right subtree are greater than the node's value

# Example usage of the TreeNode class
root = TreeNode(10) # this creates the root node of the tree with a value of 10
child1 = TreeNode(5) # this creates a child node with a value of 5
child2 = TreeNode(15) # this creates another child node with a value of 15
root.add_child(child1) # add_child() as a child of the root node
root.add_child(child2) # add_child() as a child of the root node
child1.add_child(TreeNode(3)) # add_child() as a child of child1 node
child1.add_child(TreeNode(7)) # add_child() as a child of child1 node
root.print_tree() 
# Output: 
# 10
#   5
#     3
#     7
#   15

# Graphs: Connecting the dots
# Graphs are collections of nodes (vertices) connected by edges.
# They can be directed or undirected, weighted or unweighted.
# Graphs are exceptional at:
# Modeling relationships (e.g., social networks, transportation networks)
# Finding shortest paths (e.g., Dijkstra's algorithm, A* search)

# Graphs consist of:
# Nodes (vertices): The entities in the graph
# Edges: The connections between the nodes

# Algorithms: The brains behind the operations
# Algorithms are step-by-step procedures or formulas for solving problems.

# Searching algorithms: Used to find specific elements within data structures (e.g., linear search, binary search)
# Sorting algorithms: Used to arrange elements in a specific order (e.g., bubble sort, quicksort, mergesort)
# Recursion: A technique where a function calls itself to solve smaller instances of the same problem (e.g., factorial calculation, Fibonacci sequence)

# Recursion example: Calculating the factorial of a number
def factorial(n): # defines a recursive function to calculate the factorial of a number n
    if n == 0: # base case: if n is 0, return 1 (since 0! = 1)
        return 1 
    else: # recursive case: return n multiplied by the factorial of (n-1)
        return n * factorial(n-1) 

# it is stopped when n reaches 0, 
# at which point the recursion unwinds and the final result is computed

print(factorial(5))   # Output: 120
# This code demonstrates the concept of recursion, where a function calls itself to solve a problem.
# Recursion is dangerous if not handled properly, 
# as it can lead to infinite loops and stack overflow errors.