import pytest


from src.func import *


def test_add():

    res = add(1, 6)

    assert res == 7

def test_sub():

    res = sub(10, 6)

    assert res == 4

def test_div():

    res = divide(20, 4)

    assert res == 5