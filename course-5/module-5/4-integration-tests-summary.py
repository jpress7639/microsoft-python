# Before you practice, remember:

# Integration testing verifies that multiple modules/components work together correctly after they’ve been individually built or unit-tested. It sits between unit testing (single component in isolation) and system/end-to-end testing (entire app + external systems).

# Top-down integration testing starts from higher-level modules (often UI or controllers) and uses stubs to stand in for lower-level modules that aren’t ready yet.
# → You call real high-level code; calls to not-yet-implemented lower layers are routed to simple stubs that return canned values.

# Bottom-up integration testing starts from lower-level modules and uses drivers to simulate higher-level callers.
# → You write small driver programs/functions that call low-level modules directly and check their integrated behavior.

# Mock objects and test doubles (mocks, stubs, fakes) are stand-ins for real dependencies so you can isolate the code under test and control behavior (e.g., external APIs, databases, message queues).
# → Mocks verify how they were used (calls, arguments); stubs just return predefined values; fakes are lightweight in-memory implementations.

# In Python, the unittest.mock tools (including the @patch decorator) and PyTest’s mocking support let you replace real objects with mocks during tests.
# → With @patch("package.module.ClassName") you temporarily replace ClassName with a mock for the duration of the test.

# PyTest is the main framework: tests are simple functions named test_*, you use plain assert statements, and can share setup via fixtures.
# → Example:
def test_integration_example(client, db_session):
    resp = client.get("/items")
    assert resp.status_code == 200
    assert len(resp.json()) > 0
# Common mistakes to watch out for:

# Confusing unit tests with integration tests: unit tests should mock/isolate dependencies; integration tests should intentionally exercise real interactions between multiple components.

# Overusing mocks in integration tests: if you mock every dependency, you’re back to unit testing. In integration tests, only mock truly external systems (e.g., third-party APIs), not your own internal modules.

# Misusing mocks vs stubs vs fakes: using a mock when you only need a fixed return value adds unnecessary complexity; use stubs for simple canned responses and fakes when an in-memory implementation (e.g., in-memory repo) is enough.

# Incorrect @patch target: patching the class/function where it’s defined instead of where it’s used leads to tests that don’t actually replace the dependency. Always patch the import path used by the code under test.

# Treating end-to-end tests as integration tests: E2E tests hit the full stack plus real external systems and are slower/flakier; integration tests should focus on your app’s components working together, often with external systems mocked.

# Skipping assertions of interactions when using mocks: if you don’t assert calls/arguments on a mock, you’re not verifying behavior, only that the test ran. Use checks like mock_dep.assert_called_once_with(...) to validate integration behavior.