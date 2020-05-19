# This file is discovered because it is in the working directory and the file name is 'test_*.py'
# '*_test.py' is also an option
# We

import pytest


# This function's name is not prefixed by 'test' and will not be discovered by pytest
def func1(x):
    return x + 1


# These function's names are prefixed by 'test' and will be discovered by pytest
def test_func():
    assert func1(1) == 2


def testfunc():
    assert func1(1) == 2


def test1func():
    assert func1(1) == 2


# Pytest will also discover classes prefixed with the word 'test' and functions within by the same rules
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        assert 2 + 2 == 4

    def not_test(self):
        x = "this will not be discovered"
        assert "q" in x

    def sys_exit(self):
        raise SystemExit(1)

    # Tests to see if sys_exit raises an exception
    def test_three(self):
        with pytest.raises(SystemExit):
            self.sys_exit()
