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

    def test_get_dev_lines_dict(self):
        '''
        Verify get_dev_lines() returns a dict.
        '''
        actual = pyrizz.get_dev_lines()
        assert isinstance(actual, dict), f"Expected get_dev_lines() to return a dict. Instead, it returned a {type(actual)}"

    def test_get_dev_lines_nonempty(self):
        '''
        Verify get_dev_lines() returns a non-empty dict.
        '''
        actual = pyrizz.get_dev_lines()
        assert isinstance(actual, dict), f"Expected get_dev_lines() to return a dict. Instead, it returned a {type(actual)}"
        assert bool(actual) is True, f"Expected get_dev_lines() not to be empty. Instead, it returned a dict with {len(actual.keys())} keys and {len(actual.values())} values"

    def test_get_dev_lines_three_categories(self):
        '''
        Verify get_dev_lines() returns a dict with three categories: 'romantic&sweet', 'clever&playful', 'technical&geeky'.
        '''
        actual = pyrizz.get_dev_lines()
        assert isinstance(actual, dict), f"Expected get_dev_lines() to return a dict. Instead, it returned a {type(actual)}"
        assert ('romantic&sweet' in actual) is True, f"Expected get_dev_lines() to have key 'romantic&sweet'. Instead, it returned a dict with{'' if ('romantic&sweet' in actual) is True else 'out'} key 'romantic&sweet'"
        assert ('clever&playful' in actual) is True, f"Expected get_dev_lines() to have key 'clever&playful'. Instead, it returned a dict with{'' if ('clever&playful' in actual) is True else 'out'} key 'clever&playful'"
        assert ('technical&geeky' in actual) is True, f"Expected get_dev_lines() to have key 'technical&geeky'. Instead, it returned a dict with{'' if ('technical&geeky' in actual) is True else 'out'} key 'technical&geeky'"

    def test_get_dev_line_categories_list(self):
        '''
        Verify get_dev_line_categories() returns a list.
        '''
        actual = pyrizz.get_dev_line_categories()
        assert isinstance(actual, list), f"Expected get_dev_line_categories() to return a list. Instead, it returned a {type(actual)}"

    def test_get_dev_line_categories_nonempty(self):
        '''
        Verify get_dev_line_categories() returns a non-empty list.
        '''
        actual = pyrizz.get_dev_line_categories()
        assert isinstance(actual, list), f"Expected get_dev_line_categories() to return a list. Instead, it returned a {type(actual)}"
        assert len(actual) > 0, f"Expected get_dev_line_categories() not to be empty. Instead, it returned a list with {len(actual)} elements"

    def test_get_dev_line_categories_three_categories(self):
        '''
        Verify get_dev_line_categories() returns a list with three values: 'romantic&sweet', 'clever&playful', 'technical&geeky'.
        '''
        actual = pyrizz.get_dev_line_categories()
        assert isinstance(actual, list), f"Expected get_dev_line_categories() to return a list. Instead, it returned a {type(actual)}"
        assert ('romantic&sweet' in actual) is True, f"Expected get_dev_line_categories() to have element 'romantic&sweet'. Instead, it returned a list with{'' if ('romantic&sweet' in actual) is True else 'out'} value 'romantic&sweet'"
        assert ('clever&playful' in actual) is True, f"Expected get_dev_line_categories() to have element 'clever&playful'. Instead, it returned a list with{'' if ('clever&playful' in actual) is True else 'out'} value 'clever&playful'"
        assert ('technical&geeky' in actual) is True, f"Expected get_dev_line_categories() to have element 'technical&geeky'. Instead, it returned a list with{'' if ('technical&geeky' in actual) is True else 'out'} value 'technical&geeky'"

    def test_get_random_line_str(self):
        '''
        Verify get_random_line() returns a str.
        '''
        actual = pyrizz.get_random_line()
        assert isinstance(actual, str), f"Expected get_random_line() to return a str. Instead, it returned a {type(actual)}"

    def test_get_random_line_nonempty(self):
        '''
        Verify get_random_line() returns a non-empty str.
        '''
        actual = pyrizz.get_random_line()
        assert isinstance(actual, str), f"Expected get_random_line() to return a str. Instead, it returned a {type(actual)}"
        assert len(actual) > 0, f"Expected get_random_line() not to be empty. Instead, it returned a string with {len(actual)} characters"

    def test_get_random_line_long_enough(self):
        '''
        Verify get_random_line() returns a sentence longer than 1 character.
        '''
        actual = pyrizz.get_random_line()
        assert isinstance(actual, str), f"Expected get_random_line() to return a str. Instead, it returned a {type(actual)}"
        assert len(actual) > 1, f"Expected get_random_line() has at least 1 character. Instead, it returned a string with {len(actual)} characters"

    def test_get_random_categorized_line_invalid(self):
        expected = "Please select a valid category."
        actual = pyrizz.get_random_categorized_line("")
        assert actual == expected, "Expected 'Please select a valid category.' to be returned when invalid category number is selected."
    
    def test_get_random_categorized_line_not_found(self):
        expected = "System error: category not found."
        actual = pyrizz.get_random_categorized_line("shoulda&exist")
        assert actual == expected, "Expected 'System error: category not found.' to be returned when a should-exist category is not found."

    def test_get_random_categorized_line_str(self):
        expected = str
        actual = type(pyrizz.get_random_categorized_line("romantic&sweet"))
        assert actual == expected, "Expected a string to be returned when a valid category is selected."