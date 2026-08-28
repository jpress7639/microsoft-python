# Asyncio: The foundation of asynchronous Python

# Asyncio allows you to write concurrent code using the async/await syntax. 
#
# Example:
# import asyncio
#
# async def main():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("World")
#
# asyncio.run(main())

# Concurrency, in this context, doesn't mean your program is literally doing multiple things simultaneously (like true parallelism with multiple CPU cores). 
# Instead, it efficiently manages multiple tasks seemingly at the same time within a single thread. 

# This works well for I/O-bound tasks, such as network requests, file operations, or any situation where your program spends a lot of time waiting for external resources.

# At the heart of Asyncio lies the event loop.
# The event loop keeps track of all the running tasks and decides which one should be active at any given time.

# When a task needs to wait, like when fetching data from a website, the event loop suspends it and gives another task a chance to run.

# Coroutines are the heart of asynchronous programming in Python. 
# They are special functions defined with async def and can be paused and resumed, allowing the event loop to switch between tasks efficiently.

# Example of a coroutine:
# async def fetch_data():
#     print("Start fetching")
#     await asyncio.sleep(2)
#     print("Done fetching")

# To run the coroutine, you would typically use:
# asyncio.run(fetch_data())

# Finally, tasks are used to schedule and manage coroutines. 
# Think of tasks managed by event loops - they are like little units of work that the event loop can switch between, 
# ensuring that your program remains responsive even when dealing with multiple I/O-bound operations.

# Writing asynchronous code
# you'll primarily use the “async” and “await” keywords
# In Python's Asyncio framework, an "awaitable" object is simply something that can be used with the “await” keyword.

# Another type of awaitable is a Task. Think of these as wrapped-up coroutines that are managed by the event loop. 
# You can create a task using asyncio.create_task(coroutine), which schedules the coroutine to run concurrently with other tasks.

# Finally, we have Futures. These are special objects that represent the eventual result of an asynchronous operation. They act as placeholders for a value that will be available in the future. 
# In practice, you often don't need to create Futures directly, as tasks and other high-level asyncio constructs handle them for you.

# By using “await” with these awaitable objects, you allow your coroutines to cooperate efficiently, making your asynchronous code more organized and responsive. 
# This approach helps you write code that can handle many I/O-bound tasks concurrently without blocking the main thread, leading to better performance and responsiveness in your applications.

# Before you practice, remember:

# synchronous programming: tasks run one after another; each must finish before the next starts, which can create bottlenecks when a task waits on I/O.
# asynchronous programming: tasks can run concurrently; a task can pause while waiting (e.g., for network or disk) and let other tasks run, improving responsiveness and throughput, especially for I/O-bound work.
# async def and coroutines: an asynchronous function is defined with async def and returns a coroutine object that can be scheduled by the event loop.
# asyncio.create_task: schedules a coroutine to run concurrently as a Task.
# asyncio.run: runs the main coroutine and manages the event loop for you.

# async def fetch(url):
#     ...
# await: used inside async def to pause the coroutine until an awaitable (another coroutine, Task, etc.) completes, yielding control back to the event loop.

# async def main():
#     data = await fetch(url)
# event loop (and asyncio): the core of asyncio that schedules and runs coroutines and Tasks concurrently.

# import asyncio

# async def main():
#     await fetch("https://example.com")

# asyncio.run(main())
# coroutines, Tasks, and awaitables:

# Coroutines: functions defined with async def that can be paused/resumed.
# Tasks: wrappers that schedule coroutines to run concurrently on the event loop (asyncio.create_task(coro)).
# Awaitables: objects you can await (coroutines, Tasks, some library objects).
# Asynchronous web scraping vs synchronous:

# Synchronous: one HTTP request at a time.
# Asynchronous: many HTTP requests in flight concurrently (e.g., with asyncio + aiohttp) for much faster scraping.
# Basic async web-scraping pattern with aiohttp:

# import asyncio, aiohttp

# async def fetch(session, url):
#     async with session.get(url) as resp:
#         return await resp.text()

# async def main(urls):
#     async with aiohttp.ClientSession() as session:
#         tasks = [asyncio.create_task(fetch(session, u)) for u in urls]
#         results = await asyncio.gather(*tasks)
#     return results

# asyncio.run(main(urls))
# Error handling in async code: use try/except inside async def to catch exceptions without crashing the whole program.

# async def fetch_safe(url):
#     try:
#         return await fetch(url)
#     except Exception as e:
#         # log and continue
#         ...
# exceptions and try-except:

# Exceptions: runtime errors that interrupt normal flow.
# try-except lets you handle them gracefully instead of letting the program crash.
# Documentation essentials:
# docstrings: write clear docstrings for functions/classes/modules so help(obj) is useful.
# API documentation: clearly describe each public function/class: purpose, parameters, return values, exceptions, and examples.
# Common mistakes to watch out for:

# Forgetting async/await:

# Calling an async def function without await just creates a coroutine object and never runs it.
# Using await outside an async def function is a syntax error. Wrap top-level async code in an async def main() and run with asyncio.run(main()).
# Blocking the event loop:

# Using blocking calls (e.g., time.sleep, blocking HTTP libraries, heavy CPU work) inside async def will freeze all other tasks. Use non-blocking/async equivalents (e.g., await asyncio.sleep, aiohttp).
# Misusing Tasks:

# Creating tasks with asyncio.create_task but never awaiting them (or otherwise tracking them) can cause silent failures and lost exceptions. Use await asyncio.gather(*tasks) or explicitly await each task.
# Treating async as parallel CPU execution:

# Async improves concurrency for I/O-bound tasks, not CPU-bound ones. For CPU-heavy work, consider threads/processes instead of expecting asyncio to speed it up.
# Poor error handling in async flows:

# Assuming one try-except around asyncio.gather will always show all errors; by default, gather stops at the first exception unless return_exceptions=True. Be explicit about how you want to collect and handle errors.
# Weak or missing documentation:
# Skipping docstrings or writing vague ones makes your async APIs hard to use and debug. Include what the coroutine does, what it awaits (I/O, network, etc.), and what exceptions it may raise.
