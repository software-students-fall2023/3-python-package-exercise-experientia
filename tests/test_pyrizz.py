import pytest
import pathlib
import sys

sys.path.append(f"{pathlib.Path(__file__).parent.resolve()}/../src")

from pyrizz import pyrizz

class Tests: 
    # An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
    @pytest.fixture
    def example_fixture(self):
        yield

    # Test debugging... making sure that we can run a simple test that always passes.
    def test_sanity_check(self, example_fixture):
        expected = True 
        actual = True 
        assert actual == expected, "Expected True to be equal to True!"

    # Tests for get_ai_line function.
    def test_get_ai_line_empty(self):
        expected = "Please specify a category."
        actual = pyrizz.get_ai_line("")
        assert actual == expected, "Expected 'Please specify a category.' to be returned when no category is specified."
    
    def test_get_ai_line_long(self):
        expected = "Please specify a category that is less than 50 characters."
        actual = pyrizz.get_ai_line("This is a very long category that is definitely more than 50 characters long.")
        assert actual == expected, "Expected 'Please specify a category that is less than 50 characters.' to be returned when a category that is more than 50 characters long is specified."

    def test_get_ai_line_str(self):
        expected = str
        actual = type(pyrizz.get_ai_line("test"))
        assert actual == expected, "Expected a string to be returned when a category is specified."