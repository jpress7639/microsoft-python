# Introduction to TDD
# Test-Driven Development (TDD) is a software development approach where you write tests before writing the actual code. 
# The TDD cycle typically follows the "Red-Green-Refactor" pattern:
# 1. Red: Write a failing test for the new functionality.
# 2. Green: Write the minimum code necessary to make the test pass.
# 3. Refactor: Improve the code while ensuring that all tests still pass.

# Benefits of TDD:
# - Ensures code quality by catching bugs early.
# - Provides a safety net for refactoring.
# - Encourages better design and modular code.
# - Improves developer confidence and productivity.

# Example TDD workflow:
# 1. Write a failing test for a new function.
# 2. Write the minimum code necessary to make the test pass.
# 3. Refactor the code while ensuring all tests still pass.

# Example:
def test_addition():
    result = add(2, 3)
    assert result == 5

def add(a, b):
    return a + b

# Challenges of TDD:
# - Writing tests first can be time-consuming initially.
# - It may be challenging to write tests for complex scenarios upfront.
# - Developers need to be disciplined to follow the TDD cycle consistently.
# - Refactoring can be risky if tests are not comprehensive.

# Step by Step
# isEven function that 2 is true, false is 3

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False

def is_even(n):
    return n % 2 == 0


# REVIEW SUMMARY 

# Before you practice, remember:

# Test-Driven Development (TDD): write tests before implementation; tests encode the requirements and drive what code you write next.
# Red-Green-Refactor cycle:
# Red: write a new test and run it to see it fail.
# Green: write the minimum code needed to make the test pass.
# Refactor: clean up code (and tests) without changing behavior; tests must stay green.
# Failing tests are expected at first: a new test should fail before you implement the feature, proving the test is meaningful.
# Quality control in TDD: your test suite is a safety net; when you change or refactor code, re-run tests to catch regressions immediately.
# Continuous Integration (CI): an automated process that builds and tests code on every change; a CI pipeline typically runs steps like build → test → report feedback.
# Integration testing: tests how multiple components work together (e.g., API + database), complementing unit tests that focus on single functions or classes.
# Common mistakes to watch out for:

# Writing implementation code before tests: this breaks TDD’s feedback loop; always add or update a test first, see it fail, then implement.
# Skipping the refactor step once tests pass: leaving duplication or messy design makes future changes harder; refactor while tests keep you safe.
# Making tests too broad or vague: tests should assert specific, observable behavior; overly general tests are hard to debug when they fail.
# Treating CI as optional: if you only run tests locally, you may miss environment-specific or integration issues; ensure tests run automatically in the CI pipeline.
# Relying only on unit tests and ignoring integration tests: code can pass unit tests but still fail when components interact; add integration tests for critical flows.