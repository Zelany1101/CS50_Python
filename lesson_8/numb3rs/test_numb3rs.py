import pytest
from numb3rs import validate

def testvalid():
    assert validate("127.0.0.1") == True
def test3values():
    assert validate("8.8.8") == False
def test5vlues():
    assert validate("10.10.10.10.10") == False
def teststring():
    assert validate("cat") == False
def testipv6():
    assert validate("2001:0db8:85a4:0000:0000:8a2e:0370:7334") == False
def testnumbers():
    assert validate("127.555.10.10") == False

