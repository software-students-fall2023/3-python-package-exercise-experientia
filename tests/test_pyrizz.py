import pytest
import pathlib
import sys
import re
from unittest.mock import Mock, patch
from unittest.mock import patch, MagicMock, mock_open
import openai
sys.path.append(f"{pathlib.Path(__file__).parent.resolve()}/../src")
from pyrizz import pyrizz

class Tests:

    # Tests if this returns a list
    def test_get_lines_list(self):
        actual = pyrizz.get_lines('all')
        assert isinstance(actual, list)
    
    # Tests if this returns an empty or not a proper category
    def test_get_lines_nonempty(self):
        actual = pyrizz.get_lines()
        assert isinstance(actual, list)
        assert bool(actual) is True


    # Tests if this returns a string
    def test_get_random_line_str(self):
        actual = pyrizz.get_random_line()
        assert isinstance(actual, str)

    # Tests if the get random line is a non-empty value
    def test_get_random_line_nonempty(self):
        actual = pyrizz.get_random_line()
        assert isinstance(actual, str)
        assert len(actual) > 0

    # Tests if the get random line is a empty value
    def test_get_random_line_empty(self):
        actual = pyrizz.get_random_line()
        assert isinstance(actual, str)
        assert bool(actual)

    # Tests if the get random line is long enough
    def test_get_random_line_long_enough(self):
        actual = pyrizz.get_random_line()
        assert isinstance(actual, str)
        assert len(actual) > 1


    # Tests if this returns a string
    def test_get_random_category_line_str(self):
        actual = pyrizz.get_random_category_line("romantic")
        assert isinstance(actual, str)

    # Tests if the get random category line is a non-empty value
    def test_get_random_category_line_nonempty(self):
        actual = pyrizz.get_random_category_line("romantic")
        assert isinstance(actual, str)
        assert len(actual) > 0

    # Tests if the get random cateogory line is a empty value
    def test_get_random_category_line_empty(self):
        actual = pyrizz.get_random_category_line()
        assert isinstance(actual, str)
        assert bool(actual)

    # Tests if the get random line is long enough
    def test_get_random_category_line_longenough(self):
        actual = pyrizz.get_random_category_line("romantic")
        assert isinstance(actual, str)
        assert len(actual) > 0


    # Tests if the input for ai line is empty
    def test_get_ai_line_empty(self):
        actual = pyrizz.get_ai_line("")
        expected = "Please specify a category."
        assert actual.strip() == expected.strip()

    # Tests if the input is way too long
    def test_get_ai_line_long(self):
        actual = pyrizz.get_ai_line("This is a very long category that is definitely more than 50 characters long.")
        expected = "Please specify a category that is less than 50 characters."
        assert actual.strip() == expected.strip()


    # Tests if the input for ai line actually results in a string
    def test_get_ai_line_str(self):
        actual = pyrizz.get_ai_line("test")
        assert isinstance(actual, str)


    # Tests if the rate line is empty
    def test_rate_line_empty(self):
        actual = pyrizz.rate_line("")
        assert actual == "No pickup line? You gotta use our other features before you come here buddy."

    # Tests if the rate line function follows a specific format
    def test_rate_line_format(self):
        actual = pyrizz.rate_line("Do you come with Wi-Fi? Because I'm really feeling a connection.")
        assert re.match(r'\d+/10 - .+', actual) is not None
     
    # Tests for user input validation 
    def test_is_line_valid_length(self):
        long_line = "x" * 141  
        assert not pyrizz.is_line_valid(long_line), "Expected the line to be flagged as too long."
    
    @patch("builtins.input", side_effect=["1", "word1, word2"])
    def test_get_user_input_for_line(self, mock_input):
        template_number, words = pyrizz.get_user_input_for_line()
        assert template_number == 0
        assert words == ["word1", "word2"]
        
    def test_create_line_invalid_template_number(self):
        _, message = pyrizz.create_line(999, ["word1", "word2"])
        assert message == "Template number out of range. Please choose between 0 and {}.".format(len(pyrizz.templates) - 1)