"""
Implement three or more functions that collectively test implementation of convert thoroughly, each of whose names
should begin with test_.
"""
import pytest
from working import convert

#9 AM to 5PM == 09:00 to 17:00
#9:00 AM to 5:00 PM == 09:00 to 17:00
#8 PM to 8 AM == 20:00 to 08:00
#8:00 PM to 8:00 AM == 20:00 to 08:00
# 12 AM to 12 PM == 00:00 to 12:00
# 12:00 AM to 12:00 PM == 00:00 to 12:00

def test_no_semi_colon():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_no_semi_colon2():
    with pytest.raises(ValueError):
        assert convert("9 am to 5 pm")
def test_no_semi_colon3():
    with pytest.raises(ValueError):
        assert convert("13 AM to 24 PM")

def test_semi_colon():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
def test_semi_colon2():
    with pytest.raises(ValueError):
        assert convert("9:00 am to 5:00 pm")
def test_semi_colon3():
    with pytest.raises(ValueError):
        assert convert("9:64 AM to 5:75 PM")

def test_other():
    with pytest.raises(ValueError):
        assert convert("9:00 AM - 5:oo PM")
def test_other2():
    with pytest.raises(ValueError):
        assert convert("9:00 to 5:oo")
def test_other3():
    with pytest.raises(ValueError):
        assert convert("9:00AM - 5:ooPM")
def test_other4():
    with pytest.raises(ValueError):
        assert convert("9:00AM-5:ooPM")


