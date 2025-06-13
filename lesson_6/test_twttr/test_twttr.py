"""
implment one or more functions that collectively test your
implementation of shorten thoroughly, each of whose names should
begin with test_ so that you can execute your test with
    'pytest test_twttr.py'
"""

import pytest
from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("AExIOU") == "x"
    assert shorten("1234") == "1234"
    assert shorten(".,!@?") == ".,!@?"
