import pytest
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

    def test_get_ai_line_empty(self):
        expected = "Please specify a category."
        actual = pyrizz.get_ai_line(None)
        assert actual == expected, "Expected 'Please specify a category.' to be returned when no category is specified."
    