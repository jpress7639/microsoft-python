# Asynchronous vs. synchronous code: A comparative analysis

# Synchronous code executes tasks sequentially, 
# blocking the program until each task completes.
# can lead to bottlenecks or delays, especially when dealing with 
# I/O-bound tasks like network requests or file operations.


# Asynchronous code, on the other hand, allows tasks to run concurrently,
# enabling the program to continue executing other tasks while waiting for 
# slower operations (like I/O) to complete.

# Example:

# Synchronous example
import time

def task(name, duration):
    print(f"Starting {name}")
    time.sleep(duration)
    print(f"Finished {name}")

def main_sync():
    task("Task 1", 2)
    task("Task 2", 3)

main_sync()

# Asynchronous example
import asyncio

async def async_task(name, duration):
    print(f"Starting {name}")
    await asyncio.sleep(duration)
    print(f"Finished {name}")

async def main_async():
    await asyncio.gather(
        async_task("Task 1", 2),
        async_task("Task 2", 3)
    )

asyncio.run(main_async())
# In the synchronous example, Task 2 starts only after Task 1 finishes, 
# resulting in a total runtime of 5 seconds.
# In the asynchronous example, both tasks run concurrently, 
# so the total runtime is roughly the duration of the longest task, 3 seconds.

# Advantages of synchronous code:
# Simplicity: easier to understand and reason about, as tasks are executed one after another.
# Predictability: tasks run in a defined order, making it easier to anticipate program behavior.

# Disadvantages of synchronous code:
# Blocking: each task must complete before the next one starts, which can lead to inefficiencies for I/O-bound tasks.
# Limited concurrency: cannot take full advantage of modern multi-core processors for parallelizable tasks.

# Advantages of asynchronous code:
# Concurrency: allows multiple tasks to run simultaneously, improving efficiency for I/O-bound operations.
# Responsiveness: the program can continue executing other tasks while waiting for slower operations to complete.
# Scalability: can handle a larger number of tasks efficiently, as tasks are not blocked by slower operations.

# Disadvantages of asynchronous code:
# Complexity: harder to understand and reason about, as tasks may execute out of order.
# Debugging: can be more challenging due to concurrency and potential race conditions.
# Overhead: managing asynchronous tasks and event loops can introduce additional complexity and resource usage.

# Real-life example: 
# You need to perform web scraping to gather data from a music streaming application.
# Asynchronous approach allows you to send multiple web requests concurrently, 
# significantly reducing the total time required to scrape data from multiple pages.

# Your job is to train a complex machine learning model on a powerful server using multiple CPU cores.
# Synchronous approach is suitable here because the task is CPU-bound and can fully utilize the multiple cores of the server.

# Going asynchronous: Concurrency for responsive applications

# In scenarios where responsiveness is crucial, such as web servers or GUI applications,
# asynchronous programming allows the application to handle multiple tasks concurrently,
# ensuring that the user interface remains responsive and requests are processed efficiently.

# Asynchronous programming involve 3 key components:

# 1. Asynchronous functions
#    These are functions defined using the `async def` syntax.
#    They allow you to perform non-blocking operations using the `await` keyword.

# 2. Await keyword
#    The `await` keyword is used to pause the execution of an asynchronous function
#    until the awaited task is completed. This allows other tasks to run concurrently during the wait time.

# 3. Event loop
#    The event loop is responsible for managing and scheduling asynchronous tasks. 
#    It continuously checks for tasks that are ready to run and executes them, ensuring efficient concurrency.

