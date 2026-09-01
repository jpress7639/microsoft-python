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
    summary = {
        "total_tests": 0,
        "passed_tests": 0,
        "failed_tests": 0,
        "integration_failures": [],
        "has_ai_suggestions": False
    }

    for test in test_results:
        if not all(key in test for key in ("name", "status", "type")):
            continue
        summary["total_tests"] += 1
        if test["status"] == "passed":
            summary["passed_tests"] += 1
        elif test["status"] == "failed":
            summary["failed_tests"] += 1
            if test["type"] == "integration":
                summary["integration_failures"].append(test["name"])

    summary["has_ai_suggestions"] = any(
        isinstance(suggestion, str) and suggestion.strip() for suggestion in ai_suggestions
    )

    return summary

def filter_passing_tests(results, threshold):
    """Return names of tests that passed and are within the duration threshold.

    Args:
        results (list): List of dictionaries with keys "name", "status", "duration".
        threshold (float): Maximum allowed duration for a test.

    Returns:
        list: Names of tests that meet the criteria.

    TODO:
    - Do not mutate the input list.
    - Only include tests with status "passed" and duration <= threshold.
    - Treat negative thresholds as disallowing all tests.
    - Skip entries missing required keys.
    - Preserve the original order.
    """
    # Write your implementation below following TDD principles.
    passing_tests = []
    if threshold < 0:
        return passing_tests

    for test in results:
        if not all(key in test for key in ("name", "status", "duration")):
            continue
        if test["status"] == "passed" and test["duration"] <= threshold:
            passing_tests.append(test["name"])

    return passing_tests