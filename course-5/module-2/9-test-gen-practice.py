# Practice 1:

def summarize_latencies(latencies):
    """Summarize a list of request latencies in milliseconds.

    Args:
        latencies (list of int): Non-negative request latencies in ms.

    Returns:
        dict: A dictionary with keys "avg" (float), "p95" (int), and "max" (int).

    Behavior:
        - If latencies is empty, return {"avg": 0.0, "p95": 0, "max": 0}.
        - Otherwise, compute:
            * avg: arithmetic mean of latencies
            * p95: 95th percentile, defined as the element at index ceil(0.95 * n) - 1
                   in the sorted list, where n is len(latencies)
            * max: maximum value in latencies
    """
    # TODO: Implement this function following the specification above.
    # You may import standard library modules inside the function if needed.
    new_latencies = sorted(latencies)
    n = len(new_latencies)
    if n == 0:
        return {"avg": 0.0, "p95": 0, "max": 0}
    avg = sum(new_latencies) / n
    p95_index = int((0.95 * n) - 1)
    p95 = new_latencies[p95_index]
    max_latency = max(new_latencies)
    return {"avg": avg, "p95": p95, "max": max_latency}


# Practice 2:

def build_docstring(func_name, description, params, returns):
    """Build a standardized docstring string for a function.

    Parameters
    ----------
    func_name : str
        Name of the function.
    description : str
        Short description of the function behavior.
    params : list of tuple
        Each tuple is (name, type, description) for a parameter.
    returns : tuple
        A tuple (type, description) for the return value.

    Returns
    -------
    str
        A multi-line docstring following the required template.
    """
    # TODO: Implement according to the specification in the prompt.
    # Remember to:
    # - Use "Function: <func_name>" as the first line.
    # - Include a Summary line, Parameters section, Returns section.
    # - Add the final human oversight note line exactly as specified.
    # - Join all lines with "\n" and avoid leading/trailing blank lines.
    docstring_lines = []
    docstring_lines.append(f"Function: {func_name}")
    docstring_lines.append("")
    docstring_lines.append(f"Summary: {description}")
    docstring_lines.append("")
    docstring_lines.append("Parameters")
    docstring_lines.append("----------")
    for name, type_, desc in params:
        docstring_lines.append(f"{name} : {type_}")
        docstring_lines.append(f"    {desc}")
    docstring_lines.append("")
    docstring_lines.append("Returns")
    docstring_lines.append("-------")
    return_type, return_desc = returns
    docstring_lines.append(f"{return_type}")
    docstring_lines.append(f"    {return_desc}")
    docstring_lines.append("")
    docstring_lines.append("Note: Always review the generated docstring for accuracy and completeness.")
    return "\n".join(docstring_lines)

# Practice 3:

"""COPilot: Your Task You are using generative AI to help you write unit tests for a Python function. Sometimes the AI proposes redundant tests (same inputs, same expected behavior) or misses important edge cases.

Implement two functions:

is_redundant(test_a, test_b)

Each test is represented as a dictionary with keys:

'name' : a string test name.

'input' : a tuple of positional arguments for the function under test.

'expected' : the expected return value.

Return True if test_a and test_b are redundant from a behavioral perspective, meaning:

They have exactly the same 'input' tuple, and

They have exactly the same 'expected' value. Otherwise, return False .

find_missing_edge_cases(generated_tests, required_cases)

generated_tests is a list of test dictionaries in the same format as above.

required_cases is a list of dictionaries with keys:

'input' : a tuple of positional arguments.

'expected' : the expected return value.

Return a list of all dictionaries from required_cases that are not covered by any test in generated_tests . A required case is considered covered if there exists at least one generated test that is not redundant with it but is behaviorally equivalent, i.e., has the same 'input' and 'expected' .

Your functions will help you validate and refine AI-generated test suites by detecting duplicates and identifying missing edge cases.

Examples Informal example 1 (redundant tests): * test_a = {"name": "t1", "input": (1, 2), "expected": 3} * test_b = {"name": "t2", "input": (1, 2), "expected": 3} * is_redundant(test_a, test_b) should return True .

Informal example 2 (missing edge cases): * generated_tests = [
        {"name": "pos", "input": (1, 2), "expected": 3},
        {"name": "neg", "input": (-1, -2), "expected": -3}
      ] * required_cases = [
        {"input": (1, 2), "expected": 3},
        {"input": (0, 0), "expected": 0}
      ] * find_missing_edge_cases(generated_tests, required_cases) should return a list containing only the {"input": (0, 0), "expected": 0} case."""

from typing import List, Dict, Any


def is_redundant(test_a: Dict[str, Any], test_b: Dict[str, Any]) -> bool:
    """Return True if test_a and test_b are behaviorally redundant.

    Two tests are redundant if they have exactly the same 'input' tuple and the same
    'expected' value, regardless of their 'name' fields.

    Args:
        test_a: A dictionary with keys 'name', 'input', and 'expected'.
        test_b: A dictionary with keys 'name', 'input', and 'expected'.

    Returns:
        True if the tests are behaviorally redundant, False otherwise.
    """
    # TODO: Implement this function
    return (
        test_a['input'] == test_b['input']
        and test_a['expected'] == test_b['expected']
    )

def find_missing_edge_cases(
    generated_tests: List[Dict[str, Any]],
    required_cases: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Return required cases that are not covered by generated tests.

    A required case is covered if there exists at least one generated test with the
    same 'input' and 'expected' values. Use the behavior defined in is_redundant
    to determine equivalence.

    Args:
        generated_tests: List of test dictionaries produced by an AI assistant.
        required_cases: List of required behavior cases to be covered.

    Returns:
        A list of required case dictionaries that are not covered by any
        generated test.
    """
    # TODO: Implement this function
    missing_cases = []
    for required in required_cases:
        temp_required = {'name': '', 'input': required['input'], 'expected': required['expected']}
        covered = False
        for generated in generated_tests:
            if is_redundant(temp_required, generated):
                covered = True
            break
        if not covered:
            missing_cases.append(temp_required)
    return missing_cases

print(find_missing_edge_cases(
    generated_tests=[
        {"name": "pos", "input": (1, 2), "expected": 3},
        {"name": "neg", "input": (-1, -2), "expected": -3}
    ],
    required_cases=[
        {"input": (1, 2), "expected": 3},
        {"input": (0, 0), "expected": 0}
    ]
))  # Expected output: [{'name': '', 'input': (0, 0), 'expected': 0}]

# Practice 4: 
def refactor_sum_of_squares(numbers):
    """Return the sum of squares of all non-negative integers in the list.

    Constraints:
        - Do not use explicit `for` or `while` loops.
        - You may use built-ins like `sum`, `map`, `filter`, comprehensions, or `all`/`any`.
    """
    # TODO: Implement this function using a refactored, loop-free style.
    # Hint: Think about combining filtering and transformation into a single expression.
    if numbers is None or not numbers:
        return 0
    return sum(x ** 2 for x in numbers if x >= 0)


def analyze_refactor(original_func, test_cases):
    """Compare the behavior of `original_func` and `refactor_sum_of_squares`.

    Args:
        original_func: a function that takes a list of integers and returns an integer.
        test_cases: a list of lists of integers.

    Returns:
        True if both implementations return the same value for every test case.
        False otherwise.
    """
    # TODO: Implement this function without explicit loops.
    # Hint: Consider using `all` to aggregate comparisons across test cases.
    return all(original_func(tc) == refactor_sum_of_squares(tc) for tc in test_cases)

