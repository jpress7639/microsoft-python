# Types of testing for automation scripts: 
# Unit, integration, and end-to-end

# testing stands as the vigilant guardian, ensuring the functionality, reliability, and efficiency of an application
# automation scripts - testing ensuring the margin for error is minimized (can be unforgiving)

# Unit testing: The building blocks of stability 
# scrutinizes the smallest testable components of your code, ensuring their individual functionality
# In automation scripts - unit testing helps catch errors early, ensuring each component works as intended before integrating them into larger workflows

# Unit testing provides a safety net during code refactoring, ensuring that modifications or enhancements don't inadvertently introduce regressions or disrupt existing functionality

# Unit testing libaries: 
# pytest and unittest - most popular choices 
# unittest, which provides a solid foundation for unit testing - comfortable option for those coming from other programming languages
# pytest - a third-party library, known for its simplicity and powerful features, making it a popular choice for modern Python testing

# Code example: Change the last line of the calculate_total function to return price - (price * tax_rate) to see failing tests

from asyncio import subprocess
import unittest

def calculate_total(price, tax_rate):
    return price + (price * tax_rate)

class TestCalculateTotal(unittest.TestCase):
    def test_calculate_total(self):
        # Example unit test
        self.assertEqual(calculate_total(100, 0.05), 105)

    def test_calculate_total_no_tax(self):
        # Example unit test
        self.assertEqual(calculate_total(200, 0), 200)

unittest.main()

# Integration testing - examines the connections and communication pathways between different modules or components in your automation scripts
# shifting the focus from individual units to their collaborative efforts

# The purpose of integration testing is to ensure seamless interaction between the various parts of your system

# Integration testing is crucial for uncovering unexpected issues arising when different components are combined, 
# such as incompatible data formats or unforeseen side effects not apparent during isolated unit testing

# Code Example: 

import pytest # type: ignore - make sure to begin the file with "test_"

import requests

def test_integration_api():

    response = requests.get("https://api.example.com/customers")

    assert response.status_code == 200

    assert 'customers' in response.json()


if __name__ == '__main__':

    pytest.main()

# This code defines a simple integration test using pytest and requests to check if an API endpoint returns a successful response and contains the expected data.

# End-to-end testing
# The ultimate validation of your system's functionality
# end-to-end tests ensure that the script accomplishes its intended goal when run in its entirety

# The purpose of end-to-end testing is to ensure a seamless and satisfying user experience.
# It also serves as a safety net for catching unexpected issues that might have slipped through the cracks during earlier testing phases.

# end-to-end testing leaves no stone unturned

# Code Example:


def test_end_to_end():
    result = subprocess.run(['python', 'your_script.py'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Expected output' in result.stdout

if __name__ == '__main__':
    test_end_to_end()       

# This code defines a simple end-to-end test that runs the entire script and checks for the expected output.

# NOTE: the risks associated with inadequate testing can be significant, including costly bugs, user dissatisfaction, and damaged reputations.

# PRACTICAL SCENARIO 
# Your team decides to refactor the part of the inventory update script that calculates shipping costs to make it more efficient

# If you just deploy the new shipping cost calculation without testing, you risk introducing a bug that might cause the entire inventory update process to fail, or worse, update product quantities incorrectly.
# Verify Existing Functionality: They would check if the core inventory update process (fetching data, updating quantities, etc.) still works exactly as it did before the shipping cost change.
# Catch New Bugs: They would specifically look for any new errors or unexpected behaviors introduced by the changes to the shipping cost calculation. 

# Why it's Relevant to You: As a full-stack developer, you'll often be making changes to existing codebases. 