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
        actual = pyrizz.get_random_category_line("romantic_lines")
        assert isinstance(actual, str)

    # Tests if the get random category line is a non-empty value
    def test_get_random_category_line_nonempty(self):
        actual = pyrizz.get_random_category_line("romantic_lines")
        assert isinstance(actual, str)
        assert len(actual) > 0

    # Tests if the get random cateogory line is a empty value
    def test_get_random_category_line_empty(self):
        actual = pyrizz.get_random_category_line()
        assert isinstance(actual, str)
        assert bool(actual)

    # Tests if the get random line is long enough
    def test_get_random_category_line_longenough(self):
        actual = pyrizz.get_random_category_line("romantic_lines")
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
    # def test_add_user_line_success(self, mock_open_json, mock_json_load, mock_insert_one, mock_input, capsys):
    #     pyrizz.add_user_line()
    #     captured = capsys.readouterr()
    #     assert "Here's your custom pick-up line:" in captured.out

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