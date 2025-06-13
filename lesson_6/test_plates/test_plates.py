"""
Reimplement Vanity Plates from Problem Set 2, restructing code as
    def main():
        ...
    def is_valid(s):
        ...
    if __name__ == "__name__":
        main()
wherein is_valid(s) still expects a str s as input and returns True if that str meets all
requirements and False if it does not, but main is only called if the value of __name__ is
"__main__"

Then in a file called test_plates.py, implement four or more functions that collectively test your
implementation of is_valid thoroughly, each of whose names should begin with test_ to execute test
with pytest

"""

import pytest
from plates import is_valid

def test_is_valid():
    assert is_valid('abc123') == True
    assert is_valid('a') == False
    assert is_valid('abc1234') == False
    assert is_valid('ab123c') == False
    assert is_valid('abc.12') == False
    assert is_valid('abc012') == False
    assert is_valid('12abcs') == False
    assert is_valid('12') == False
