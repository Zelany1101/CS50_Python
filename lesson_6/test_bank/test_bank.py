"""
reimplement Home Federal Savings Bank from Problem Set 1, restructing code wherein value expects a str as input and returns an int, namely 0 if that str starts with
'hello', 20 if that str starts with an 'h' but not 'hello', or 100 otherwise, treating the str case-insensitively
    - assume the string passed to the value function will not contain any leading spaces
    - only main should call print

    def main():
        ...

    def value(greeting):
        ...

    if __name__ == '__main___':
        main()

Then in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin
with test_ so that you can execute your tests with:
    pytest test_bank.py
"""
import pytest
from bank import value

def test_hello_value():
    assert value('Hello') == 0
    assert value('hello') == 0

def test_h_value():
    assert value('hi') == 20
    assert value('hggggggg') == 20

def test_other_value():
    assert value('0') == 100
    assert value('.') == 100

