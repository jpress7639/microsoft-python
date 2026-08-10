# Creating and Reviewing Documentation Summary

# Gen AI tools can read Python code (including comments and docstrings) 
# and generate or improve documentation such as function descriptions, parameter explanations, and API references.

# Docstrings are formal, structured strings inside functions, classes, or modules that describe what they do, 
# their parameters, return values, and side effects.

# Comments are informal notes in code (e.g., # this calculates tax) that 
# add context but are not a substitute for proper docstrings.

# API reference documentation is the detailed “instruction manual” for an API: 
# listing functions/methods, parameters, types, defaults, return values, and usage notes.

# Templates (for docstrings, API entries, or GenAI outputs) give a consistent structure, 
# making it easier for both humans and Gen AI to produce clear, complete documentation.

# Human oversight is required after Gen AI generates documentation: 
# you must review for accuracy, completeness, and alignment with Python conventions (e.g., PEP 257-style docstrings).

# Common mistakes to watch out for:

# Relying on Gen AI output without review: AI-generated docstrings or API docs 
# can be plausible but wrong; always verify behavior, parameters, and edge cases against the actual code.

# Mixing up comments and docstrings: using only # comments where a proper docstring is 
# expected will weaken auto-generated documentation and API tools that rely on docstrings.

# Inconsistent or missing structure: skipping templates or style conventions leads 
# to uneven documentation that Gen AI can’t reliably extend or update.

# Letting documentation drift from code: changing function signatures or behavior without updating docstrings/API docs 
# causes confusion and makes Gen AI more likely to propagate outdated info.

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
    return sum(x ** 2 for x in numbers if isinstance(x, int) and x >= 0)

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

def score_prompt_match(requirement, code_snippet):
    """Score how well code_snippet matches requirement using simple heuristics.

    Returns an integer score from 0 to 100:
      - +30 if code_snippet contains "def"
      - +40 if code_snippet contains all requirement words (len >= 4, after
        lowercasing and stripping punctuation)
      - +30 if code_snippet contains at least one digit
      - capped at 100
    """
    score = 0

    if "def" in code_snippet:
        score += 30

    punctuation = ".,:;!?"

    def clean_words(text):
        words = text.lower().split()
        return {word.strip(punctuation) for word in words}

    requirement_words = clean_words(requirement)
    code_words = clean_words(code_snippet)

    requirement_words = {w for w in requirement_words if len(w) >= 4}

    if requirement_words and requirement_words.issubset(code_words):
        score += 40

    if any(char.isdigit() for char in code_snippet):
        score += 30

    score = min(100, max(0, score))
    return score