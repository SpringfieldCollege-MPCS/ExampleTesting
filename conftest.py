import pytest
import string
from mypackage import Line


@pytest.fixture
def short_list():
    return ["a", "b", "c"]

@pytest.fixture
def long_list():
    return list(string.ascii_uppercase)

@pytest.fixture
def short_line():
    return Line(["a", "b", "c"])

@pytest.fixture
def long_line():
    return Line(list(string.ascii_uppercase))