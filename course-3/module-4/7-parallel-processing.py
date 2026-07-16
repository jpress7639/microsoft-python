# Parallel processing with Python: Concurrency and multiprocessing

# Concurrency, often implemented using multiple threads (multithreading) in Python, 
# manages multiple tasks within a single process
# NOTE: these threads share the same memory space within the process, which can lead to potential issues with data consistency and requires careful synchronization.
# typically limited in their ability to run truly simultaneously on multi-core processors due to Python's Global Interpreter Lock (GIL)

# Multiprocessing, on the other hand, involves running multiple processes concurrently, 
# each with its own memory space. This approach avoids the data consistency issues associated with threads but comes with higher memory and inter-process communication overhead.

# Concurrency and multiprocessing: The basics

# due to the Global Interpreter Lock (GIL), Python threads take turns utilizing a single CPU core
# While this may appear to limit their effectiveness, 
# threads remain invaluable for tasks involving substantial waiting periods, 
# such as network requests or user input, as they can seamlessly switch between tasks during these idle intervals, 
# maximizing overall efficiency

# Multiprocessing involves running multiple processes, each possessing its own dedicated Python interpreter and memory space.
# This allows true parallel execution on multi-core processors, making it suitable for CPU-bound tasks that require intensive computation.

# Why parallel processing matters for automation

# Think of it as dividing a massive workload into manageable portions, then assigning each portion to a dedicated worker.
# With concurrency or multiprocessing, you can have multiple workers tackle these portions simultaneously, akin to a well-coordinated team effort.

# It unlocks a new level of productivity.

# Scaling automation with concurrency
# You are automating a task that requires retrieving data from multiple web APIs
# Consider using concurrency with threads. It's like opening up multiple checkout lanes.
# While one thread patiently waits for a response from the API, the other threads can proceed with their own requests.

# The result? A considerable boost in speed and efficiency, especially when the primary bottleneck lies in network input/output operations.

# Example Code:
import concurrent.futures
import requests

def fetch_data(api_url):
    """Fetches data from a given API URL."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None

if __name__ == "__main__":
    api_urls = [
        "https://api.example.com/data1",
        "https://api.another-example.com/data2",
        "https://api.yet-another-example.com/data3"
        # Add more API URLs as needed
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit API requests concurrently
        future_to_url = {executor.submit(fetch_data, url): url for url in api_urls}

        # Process results as they become available
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()   
                if data:
                    print(f"Data from {url}: {data}")
            except Exception as exc:
                print(f"Exception while fetching data from {url}: {exc}")


# NOTE: Remember to adjust the number of threads in the ThreadPoolExecutor based on your system's capabilities and the number of API requests 
# Be mindful of API rate limits to avoid overwhelming the APIs

# Scaling automation with multiprocessing
# where your task demands substantial computational power from the CPU

#  With multiprocessing, you essentially open up all the lanes, allowing traffic to flow smoothly and efficiently.

# This approach maximizes the utilization of your hardware's capabilities, 
# ensuring no core remains idle while others are burdened with the entire workload.

# The outcome? A remarkable improvement in performance compared to confining the task to a single CPU core.

# Code Example:
import multiprocessing
from PIL import Image  #type: ignore
# Example of an image processing library

def process_image(image_path):
    """Performs CPU-intensive image processing on a single image."""
    # Load the image
    image = Image.open(image_path)
    # Apply filters, transformations, or any desired processing
    image = image.convert('L') # Example: convert to grayscale
    # Save the processed image
    image.save(f'processed_{image_path}')

if __name__ == '__main__':
    image_paths = ['image1.jpg', 'image2.jpg', ...] # List of image paths
    # Create a pool of processes (adjust the number based on your CPU cores)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the 'process_image' function to each image path in parallel
        pool.map(process_image, image_paths)

# we define a function process_image to handle the CPU-intensive image processing for a single image
# The multiprocessing.Pool creates a pool of worker processes, 
# and the pool.map function distributes the image processing tasks across these processes, 
# allowing them to run in parallel on different CPU cores.

# Navigating the complexities of concurrency and multiprocessing
# NOTE: When working with threads or processes, it's crucial to handle shared data with precision.

# Treat shared data as a valuable resource that multiple threads or processes may want to access simultaneously.
# Without proper synchronization mechanisms, a chaotic "race condition" can occur, where the outcome depends on the unpredictable order in which threads or processes access the data
# This can lead to data corruption or unexpected behavior.

# To prevent such issues - employ techniques like locks, semaphores, or queues, which control access to shared data and ensure integrity.

# Multiprocessing, while powerful, can be problematic.
# Each process in multiprocessing has its own memory space, which can result in higher memory usage compared to using threads.
# Additionally, inter-process communication can be more complex and slower than communication between threads within the same process.
# It's crucial to keep your hardware limitations in mind and design your solution accordingly.

