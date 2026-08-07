# GenAI Test Generation Summary

# Unit testing tests individual functions or classes in isolation to verify they behave correctly; you typically write small, fast tests that run often.
# A test case is a specific input plus an expected output/behavior used to verify code; good tests include normal, edge, and error scenarios.
# Generative AI / GenAI can take code plus instructions and generate candidate test cases (e.g., pytest functions) or test data; you still need to review, run, and refine what it produces.
# Test prompting (a form of prompt engineering) means giving GenAI clear, detailed instructions about:
# what function/module to test,
# what frameworks to use (e.g., pytest),
# what scenarios to cover (happy path, edge cases, error handling).
# Effective prompts are clear and concise and include enough context (code snippet, function signature, requirements) so the AI can generate accurate tests or documentation.
# Code coverage analysis tells you what percentage of your code is executed by your tests; use it to find untested branches and add more tests where coverage is low.
# Common mistakes to watch out for:

# Writing unit tests that depend on external systems (DBs, APIs, file system) instead of isolating the unit; use mocks/stubs so tests stay fast and reliable.
# Letting GenAI-generated tests stand without human review; they may assert the wrong behavior, miss edge cases, or rely on unstable implementation details.
# Giving vague prompts like “write tests for this” without specifying language, framework, or behaviors to test; this leads to irrelevant or low-quality tests.
# Confusing unit testing with integration or system testing; unit tests focus on one component, integration tests on interactions between components, and system tests on the whole application.
# Relying only on high code coverage as proof of quality; coverage can be high even if assertions are weak—combine coverage with meaningful assertions and, when possible, mutation testing.
# Ignoring test case prioritization; running all tests all the time can be slow—prioritize high-risk or frequently failing areas first in larger suites.
