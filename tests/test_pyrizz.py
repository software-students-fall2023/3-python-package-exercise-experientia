import pytest
import pathlib
import sys
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
        
 
# pytest tests/test_pyrizz.py 