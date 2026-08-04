# Practice 1

# managed_open should:
# Open the file with the given path and mode .
# Ensure the file is closed when the with block exits, even if an exception occurs.
# Return the file object from the with block.

# Use chunk_reader in the evaluator by reading from a temporary file. Do not print anything inside these functions.
# Examples Informal behavior description (not executable tests):
# If a file has 5 lines and chunk_size=2 , chunk_reader should yield three chunks: [line1, line2] , [line3, line4] , [line5] .

def managed_open(path, mode):
    """Open a file and ensure it is closed when leaving the with-block.

    Implement this as a context manager that can be used as:

        with managed_open(path, mode) as f:
            # use f

    It should open the file, yield or return the file object inside the block,
    and guarantee that the file is closed when the block exits, even on error.
    """
    # TODO: implement managed_open as a proper context manager
    f = open(path, mode)
    try:
        with f:
            yield f
    finally:
        f.close()
    # raise NotImplementedError("managed_open is not implemented yet")



def chunk_reader(file_obj, chunk_size):
    """Lazily read lines from file_obj and yield them in lists of up to chunk_size.

    Each yielded value should be a list of lines (strings). The generator should
    stop when there are no more lines to read. Avoid reading all lines into
    memory at once; instead, build each chunk incrementally and yield it.
    """
    # TODO: implement chunk_reader as a generator
    chunk = []
    for line in file_obj:
        chunk.append(line)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
    # raise NotImplementedError("chunk_reader is not implemented yet")

# Practice 2

def process_events(events, max_recent):
    """
    Process a stream of events and keep at most `max_recent` most recent unique events.

    Args:
        events (list of str): Incoming events in order.
        max_recent (int): Maximum number of recent unique events to retain.

    Returns:
        list of str: The events currently in the queue after processing.

    Requirements:
        - Use a list to simulate queue behavior (FIFO).
        - Use a set to track processed events.
        - Do not import external libraries.
    """
    # TODO: Implement queue and set logic as described in the prompt.
    # Hint: For a queue using a list, you can use append() to add
    # and pop(0) to remove the oldest element.
    queue = []
    seen = set()
    for event in events:
        if event not in seen:
            queue.append(event)
            seen.add(event)
            if len(queue) > max_recent:
                oldest_event = queue.pop(0)
                seen.remove(oldest_event)
    return queue

# Practice 3
def get_public_attributes(obj):
    """Return a sorted list of non-callable, non-underscore attribute names of obj.

    Use introspection tools like dir and getattr to discover attributes.
    """
    # TODO: implement this function
    attributes = [attr for attr in dir(obj) if not attr.startswith('_') and not callable(getattr(obj, attr))]
    # this filters out attributes that start with an underscore and those that are callable (methods)
    return sorted(attributes)       


def copy_public_attributes(source, target):
    """Copy public, non-callable attributes from source to target.

    Use get_public_attributes(source) to determine which attributes to copy.
    Overwrite any existing attributes on target with the same names.
    Return target.
    """
    # TODO: implement this function
    for attr in get_public_attributes(source): 
        setattr(target, attr, getattr(source, attr)) 
    # this sets the attribute on target to the value of the attribute on source
    return target

# Practice 4
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        else:
            return self.items.pop()  # No check if stack is empty

stack = Stack()
stack.pop()  # Attempt to pop from empty stack