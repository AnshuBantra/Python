import pytest
from calculator import add

def test_add():
    assert add(1, 2) == 3 #, f"Failed on positive integers 1 & 2, expected 3 received {add(1, 2)}"

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
    (4, 5, 9),
    (5, 6, 11),
    (0, 0, 0),
    (0, -1, -1),
    (1, -1, 0)
])
def test_add_param(x, y, expected):
    assert add(x, y) == expected

@pytest.fixture
def sample_data():
    return 1, 2, 3, 4, 5

def test_sum_fixture(sample_data):
    assert sum(sample_data) == 15