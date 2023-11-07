import pytest

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

    