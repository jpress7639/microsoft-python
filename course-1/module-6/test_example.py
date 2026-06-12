# PYTEST
# pytest is a testing framework that makes it easy to write small, 
# readable tests and scale them up to support complex functional testing for your applications and libraries.

# simple and readable 
# flexible and extensible 
# powerful features 
import pytest
from calculator import add


add(5, 6)

def test_add():
    assert add(2, 3) == 5

# Fixtures 
# Fixtures in pytest are functions that provide a baseline for reliable testing., 

@pytest.fixture
def sample_data():
    data = [1, 2, 3, 4, 5]
    return data

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_max(sample_data):
    assert max(sample_data) == 5

# this above is subjecting the data is passing two tests 

@pytest.fixture
def enhanced_data():
    print("Setting up enhanced data fixture...")

    data = [10, 20, 30, 40, 50]

    enhanced_data = [x * 2 for x in data]

    return enhanced_data

# above is more powerful test setups - printing, returning enhanced data