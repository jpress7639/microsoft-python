# Test doubles: Mocks, stubs, and fakes

# Test doubles are objects that stand in for real dependencies in tests.

# Types of test toubles: 
# 1.) Mocks - Objects that record how they are used and can be configured to return specific values.
# Think of a mock as a very specific kind of stand-in, almost like an actor who has been given a very detailed script.
# Example of a Mock:
"""
from unittest.mock import Mock

mock_object = Mock()
mock_object.some_method.return_value = "mocked value"

assert mock_object.some_method() == "mocked value"
"""

# 2.) Stubs - Objects that provide predefined responses to method calls, usually not recording how they were used.
# Think of a stub as a simple stand-in that provides canned responses, like a prop in a play that always looks the same.
# It's different than a mock due to not recording how it was used; it only provides predefined responses.
# Example of a Stub: 
"""
class Stub:
    def some_method(self):
        return "stubbed value"

stub_object = Stub()
assert stub_object.some_method() == "stubbed value"
"""

# 3.) Fakes - Objects that have working implementations, but are simplified versions of real dependencies.
# Think of a fake as a functional stand-in that behaves like the real dependency, but is simpler and easier to use in tests.
# Example of a Fake:
"""
class Fake:
    def some_method(self):
        return "fake value"

fake_object = Fake()
assert fake_object.some_method() == "fake value"
"""