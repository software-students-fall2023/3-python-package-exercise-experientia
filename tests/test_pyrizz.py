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

    # Fixture for mocking open()
    @pytest.fixture
    def mock_open_json(self, monkeypatch):
        data = {"templates": ["Here is a {}, and here is another {}."]}
        mock_file = mock_open(read_data=str(data))
        monkeypatch.setattr("builtins.open", mock_file)

    # Fixture for mocking json.load()
    @pytest.fixture
    def mock_json_load(self, monkeypatch):
        data = {"templates": ["Here is a {}, and here is another {}."]}
        monkeypatch.setattr("json.load", lambda x: data)

    # Fixture for mocking MongoDB insert_one
    @pytest.fixture
    def mock_insert_one(self, monkeypatch):
        def mock(*args, **kwargs):
            return MagicMock(inserted_id=1)
        monkeypatch.setattr("pymongo.collection.Collection.insert_one", mock)

    # Fixtures for mocking user input as numbers
    @pytest.fixture
    def mock_input(self, monkeypatch):
        inputs = iter(["1", "test, input"])
        monkeypatch.setattr("builtins.input", lambda x: next(inputs))

    @pytest.fixture
    def mock_input_value_error(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'not a number')

    # Fixture for handling openai 
    @pytest.fixture
    def mock_openai_offensive(self, monkeypatch):
        monkeypatch.setattr(openai.Completion, 'create', Mock(return_value={
            "choices": [{"text": "2"}]  # "2" simulates offensive content
        }))

    @pytest.fixture
    def mock_openai_error(self, monkeypatch):
        def openai_error(*args, **kwargs):
            raise openai.error.OpenAIError("Test error")
        monkeypatch.setattr(openai.Completion, 'create', openai_error)
        
    # Tests for add_user_line() function 
    def test_add_user_line_success(self, mock_open_json, mock_json_load, mock_insert_one, mock_input, capsys):
        pyrizz.add_user_line()
        captured = capsys.readouterr()
        assert "Here's your custom pick-up line:" in captured.out

    def test_add_user_line_invalid_template_number(self, mock_open_json, mock_json_load, capsys):
        with patch('builtins.input', side_effect=["21", "exit"]):
            pyrizz.add_user_line()
            captured = capsys.readouterr()
            assert "Template number out of range. Please choose between 1 and 20." in captured.out

    def test_add_user_line_not_enough_words(self, mock_open_json, mock_json_load, capsys):
        with patch('builtins.input', side_effect=["1", "test"]):
            pyrizz.add_user_line()
            captured = capsys.readouterr()
            assert "Not enough words provided for the placeholders." in captured.out

    def test_add_user_line_json_error(self, monkeypatch, capsys):
        m = mock_open()
        m.side_effect = FileNotFoundError("The file was not found.")
        monkeypatch.setattr("builtins.open", m)

        pyrizz.add_user_line()
        captured = capsys.readouterr()
        assert "templates.json was not found" in captured.out
     
    # Tests for user input validation 
    def test_is_line_valid_length(self):
        long_line = "x" * 141  
        assert not pyrizz.is_line_valid(long_line), "Expected the line to be flagged as too long."

    def test_is_offensive_detection(self, mock_openai_offensive):
        offensive_line = "An example offensive line"
        assert pyrizz.is_offensive(offensive_line) is True, "Expected the line to be flagged as offensive."

    def test_is_offensive_openai_error_handling(self, mock_openai_error):
        line = "This should cause an OpenAIError"
        assert pyrizz.is_offensive(line) is False, "Expected to return False when an OpenAIError occurs."

    def test_add_user_line_value_error(self, mock_input_value_error, capsys):
        with patch('builtins.input', side_effect=["not a number", "exit"]):
            pyrizz.add_user_line()
            captured = capsys.readouterr()
            assert "Please enter a valid number." in captured.out

    # Testing for the rate line functionality 
    def test_rate_line_empty(self, example_fixture):
        pickup_line = ""
        expected_response = "No pickup line? You gotta use our other features before you come here buddy."
        actual_response = pyrizz.rate_line(pickup_line)
        assert actual_response == expected_response
        
    def test_rate_line(self, example_fixture):
        pickup_line = "Do you come with Wi-Fi? Because I'm really feeling a connection."
        actual_response = pyrizz.rate_line(pickup_line)
        
        # Define a regular expression pattern for expected response format
        # In this case, the expected pattern response is a number/10 - some characters as a response. 
        expected_pattern = r'\d+/10 - .+'

        # Check if the actual response matches the expected pattern
        assert re.match(expected_pattern, actual_response) is not None
 
# pytest tests/test_pyrizz.py 
