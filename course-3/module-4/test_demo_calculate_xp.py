import pytest #type: ignore

def calculate_xp(score, difficulty_multiplier, time_bonus):
    """This function calculates the experience points (XP) earner by a player
    based on their score, a difficulty multiplier, and a time bonus.
    """
    base_xp = score * difficulty_multiplier
    total_xp = base_xp + (base_xp * time_bonus / 100)
    return total_xp

def test_calculate_xp_basic():
    score = 100
    difficulty_multiplier = 1.5
    time_bonus = 20
    expected_xp = 180.0 # 150 + (150 * 0.2)
    assert calculate_xp(score, difficulty_multiplier, time_bonus) == expected_xp

def test_calculate_xp_zero_score():
    score = 0
    difficulty_multiplier = 2.0
    time_bonus = 10
    assert calculate_xp(score, difficulty_multiplier, time_bonus) == 0

# pytest also offers fixtures
# Code Example:
@pytest.fixture
def xp_data():
    return {
        "score": 100,
        "difficulty_multiplier": 1.5,
        "time_bonus": 20,
        "expected_xp": 180.0
    }                      

# In this example: we define a fixture named xp_data that provides a dictionary containing the input data and expected result for the calculate_xp function. This fixture can be used in test functions to access the predefined data.

# and markers
# Code Example: 
@pytest.mark.parametrize(
    "score, difficulty_multiplier, time_bonus, expected_xp",
    [
        (100, 1.5, 20, 180.0),
        (0, 2.0, 10, 0),
        (50, 1.0, 0, 50.0)
    ]
)
def test_calculate_xp_parametrized(score, difficulty_multiplier, time_bonus, expected_xp):
    assert calculate_xp(score, difficulty_multiplier, time_bonus) == expected_xp       

# in this example, we use the @pytest.mark.parametrize decorator to run the same test function with multiple sets of input data, allowing us to efficiently test different scenarios for the calculate_xp function.