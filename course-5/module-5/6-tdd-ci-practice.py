def get_user_full_name(api_client, user_id):
    """Return the user's full name using the provided api_client.

    The api_client is expected to have a get_user(user_id) method that
    returns a dictionary with "first_name" and "last_name" keys.

    If either key is missing, this function should raise ValueError.
    """
    # TODO: implement this function
    user = api_client.get_user(user_id)
    try:
        first_name = user["first_name"]
        last_name = user["last_name"]
    except KeyError:
        raise ValueError("Missing first_name or last_name")
    return f"{first_name} {last_name}"


def create_mock_api_client(expected_user_id, user_response):
    """Create and return a mock-like API client test double.

    The returned object must:
        - Provide a get_user(user_id) method.
        - Store the last user_id it was called with in an attribute
          named last_called_with.
        - Return user_response when called with expected_user_id.
        - Raise LookupError when called with any other user_id.
    """
    # TODO: implement this function
    class MockApiClient:
        def __init__(self):
            self.last_called_with = None

        def get_user(self, user_id):
            self.last_called_with = user_id
            if user_id == expected_user_id:
                return user_response
            else:
                raise LookupError("User not found")

    return MockApiClient()


def select_test_double(purpose: str) -> str:
    """Select an appropriate test double type based on the given purpose.

    Should return one of: "mock", "stub", or "fake".
    Use keywords in the purpose string (case-insensitive) to decide.
    """
    purpose_lower = purpose.lower()
    if "verify" in purpose_lower or "expect" in purpose_lower:
        return "mock"
    elif "return" in purpose_lower or "provide" in purpose_lower:
        return "stub"
    elif "simulate" in purpose_lower or "realistic" in purpose_lower:
        return "fake"
    else:
        raise ValueError("Cannot determine appropriate test double type")

def summarize_ci_run(test_results, ai_suggestions):
    """Summarize a CI pipeline run with test outcomes and GenAI suggestions.

    Args:
        test_results (list): List of dicts with keys "name", "status", "type".
        ai_suggestions (list): List of strings representing AI-generated suggestions.

    Returns:
        dict: Summary with keys:
            - "total_tests"
            - "passed_tests"
            - "failed_tests"
            - "integration_failures" (list of names)
            - "has_ai_suggestions" (bool)

    TODO:
    - Ignore test entries missing required keys.
    - Do not mutate the input lists.
    - Correctly count passed/failed tests and integration failures.
    - Treat only non-empty, non-whitespace strings as valid AI suggestions.
    - Handle empty inputs gracefully.
    """
    # Implement your solution here.
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    integration_failures = []

    for test in test_results:
        if not all(key in test for key in ("name", "status", "type")):
            continue
        total_tests += 1
        if test["status"] == "passed":
            passed_tests += 1
        elif test["status"] == "failed":
            failed_tests += 1
        if test["type"] == "integration" and test["status"] == "failed":
            integration_failures.append(test["name"])

    has_ai_suggestions = any(
        isinstance(suggestion, str) and suggestion.strip() for suggestion in ai_suggestions
    )

    return {
        "total_tests": total_tests,
        "passed_tests": passed_tests,
        "failed_tests": failed_tests,
        "integration_failures": integration_failures,
        "has_ai_suggestions": has_ai_suggestions,
    }

def select_test_double(purpose: str) -> str:
    """Select an appropriate test double type based on the given purpose.\n\n   
     Should return one of: \"mock\", \"stub\", or \"fake\".\n    
     Use keywords in the purpose string (case-insensitive) to decide."""    
     # TODO: implement keyword-based selection logic
    purpose_lower = purpose.lower()
    if "verify" in purpose_lower or "expect" in purpose_lower:
        return "mock"
    elif "return" in purpose_lower or "provide" in purpose_lower:
        return "stub"
    elif "simulate" in purpose_lower or "realistic" in purpose_lower:
        return "fake"
    else:
        raise ValueError("Cannot determine appropriate test double type")
