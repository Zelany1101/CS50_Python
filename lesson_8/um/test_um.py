"""
Test three or more functions that collectively test your implementation of count thoroughly,
each of whose names should begin with test_ so that you can execute your tests with pytest.
"""
import pytest
from um import count

def test_words():
    assert count('album') == 0
def test_space():
    assert count('um um um') == 3
def test_capital():
    assert count('UM') == 1
