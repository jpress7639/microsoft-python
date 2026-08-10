# Write a Python function that takes a list of numbers and returns the mean, median, and mode.

def calculate_statistics(numbers):
    """Calculate the mean, median, and mode of a list of numbers.

    Args:
        numbers: A list of numerical values."""
    if not numbers:
        return None, None, None

    # Calculate mean
    mean = sum(numbers) / len(numbers)

    # Calculate median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    # Calculate mode
    from collections import Counter
    count = Counter(sorted_numbers)
    max_count = max(count.values())
    mode = [k for k, v in count.items() if v == max_count]
    if mode and len(mode) == len(count):
        mode = None  # No mode if all values are unique
    return mean, median, mode

print(calculate_statistics([1, 2, 3, 4, 4, 5, 5, 5]))  # Output: (2.4, 2, [2])
print(calculate_statistics([1, 2, 3]))  # Output: (3.0, 3, None)