![Workflow Status](https://github.com/software-students-fall2023/3-python-package-exercise-experientia/actions/workflows/python.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/pyrizz.svg)](https://badge.fury.io/py/pyrizz)

# PyRizz: Your Source for Playful Pickup Lines

[PyRizz PyPi Link](https://pypi.org/project/pyrizz/)

[PyRizz GitHub Link](https://github.com/software-students-fall2023/3-python-package-exercise-experientia)

```
pip install pyrizz
```

Looking to add a dash of humor to your day or spark some laughter in your conversations? PyRizz is here to help! PyRizz is a delightful Python package that provides a collection of randomly generated pickup lines in various categories. Whether you're looking for a clever one-liner, a cheesy quip, or a charming compliment, PyRizz has you covered.

# Contributors 
- [Aditya Pandhare](https://github.com/awesomeadi00)
- [Anzhelika Nastashchuk](https://github.com/annsts)
- [Baani Pasrija](https://github.com/zeepxnflrp)
- [Zander Chen](https://github.com/ccczy-czy)

# Key Features

In our package we have 5 special functions which you can use to enhance your dating life: 

### get_random_line()

In this function, you can retreive any random pickup line amongst all the categories that we have: 

```
from pyrizz import pyrizz

print(pyrizz.get_random_line())
```

### get_random_category_line(category)

In this function, you can retreive any random pickup line from a specific category. We have 4 main categories to choose from: 
- 'romantic': Will output a random romantic pickup line
- 'clever': Will output a random clever pickup line
- 'geeky': Will output a random geeky pickup line
- 'dev': Will output a random specially handselected pickup line from the developers
- 'all': Will output a random pickup line across ALL categories (basically get_random_line())

```
from pyrizz import pyrizz

print(pyrizz.get_random_category_line('romantic'))
print(pyrizz.get_random_category_line('clever'))
print(pyrizz.get_random_category_line('geeky'))
print(pyrizz.get_random_category_line('dev'))
print(pyrizz.get_random_category_line('all'))
```

### create_line(template_number, words)

In this function, if you're new to pickup lines, you can create your very own pickup using some of our templates!
- **template_number** - You need to input a template number (0-39). You can find out the templates by calling the list_templates() function: `templates = pyrizz.list_templates()`. This way you can see how the templates look like, how many words you need to include and which one you like! You can print these templates like this: 
```
for idx, template in enumerate(templates, 1):
    print(f"Template {idx}: {template}")
```
- **words** - You need to input a list of all the words, for example if you need to input 2 words: `words = ["word1", "word2"]`

This function returns your line with some lovely ASCII art as well! Enjoy!
Here is an example: 
```
from pyrizz import pyrizz

words_to_use = ["sun"]
output = pyrizz.create_line(1, words_to_use)
print(output)
```

## Use AI to spice up your pickup lines!

In order to access these two bottom functions, you need to have an openai api key! You can set up it as shown in the bottom two examples: 

### get_ai_line(keyword, your_openai_key)

In this function, you can retreive a generated pickup line using openai gpt-3.5 model based on any keyword that you suggest. In this example, it would output a Shakespearean pickup line: 

```
from pyrizz import pyrizz
import openai

client = pyrizz.init_openai("your_api_key")
print(pyrizz.get_ai_line("shakespeare", client))
```

### rate_line(pickup_line, your_openai_key)

In this function, you can rate your very own pickup line out of 10 using openai gpt-3.5 model. Simply type your pickup line and a rating will output: 

```
from pyrizz import pyrizz
import openai

client = pyrizz.init_openai("your_api_key")
print(pyrizz.rate_line('Are you from Tennesse? Cause you're the only 10 I see.', openai))
```

Note: Please make sure you are using `openai==0.28.1`. 


### Accessing an Example: 
You can access our example file which utilizes all of these functions with an awesome user interface: 
[Example File](https://github.com/software-students-fall2023/3-python-package-exercise-experientia/blob/main/src/pyrizz/__main__.py)

To run our main file simply run: `python3 -m pyrizz` on the terminal. 

# Contributing

We love contributions from everyone. By participating in this project, you agree to abide by the [code of conduct](https://github.com/eads/generic-code-of-conduct.git).

### Setting Up the Development Environment

1. **Clone the repository**:

    Use the following command to clone the Pyrizz repository:

    ```shell
    git clone https://github.com/software-students-fall2023/3-python-package-exercise-experientia
    ```

2. **Navigate to the project directory**:

    Change into the cloned directory:

    ```shell
    cd 3-python-package-exercise-experientia
    ```

3. **Install pipenv**:

    If you don't have pipenv installed, use pip to install it:

    ```shell
    pip install pipenv
    ```

4. **Install dependencies**:

    Use pipenv to create a virtual environment and install the necessary packages:

    ```shell
    pipenv install --dev
    ```

5. **Activate the virtual environment**:

    Enter the virtual environment using:

    ```shell
    pipenv shell
    ```

6. **Make your changes**:

    Make the changes you want to contribute to the project.

7. **Run tests**:

    Ensure your changes pass all tests using pytest:

    ```shell
    pipenv run python -m pytest
    ```

8. **Submit a Pull Request**:

    After making your changes and verifying the functionality, commit your changes and push your branch to GitHub. Then, submit a pull request to the main branch for review.

## Testing your __main__.py file locally: 

If you wish to test and run the `__main__.py` file locally (not test and run the `__main__.py` from the package), all you have to do is uncomment the bottom imports from the `pyrizz.py` and `__main__.py` file and comment the top ones as shown below: 

**pyrizz.py:**
```
# Uncomment when using pytest and uploading the package to PyPi
# from pyrizz.pickuplines import pickuplines
# from pyrizz.templates import templates

# Uncomment when testing the __main__.py file locally
from pickuplines import pickuplines
from templates import templates
```

**__main__.py**:
```
# Uncomment when using pytest and uploading the package to PyPi
# import pyrizz.pyrizz as pyrizz

# Uncomment when testing the __main__.py file locally
import pyrizz as pyrizz
```
Then you can run the command: `python3 src/pyrizz/__main__.py` to execute the main file locally. 

As always, when you wish to finally test the program and repackage it, you must comment the imports you just uncommented to run the main locally, and uncomment the top imports as they are necessary for testing and packaging. 

### Reporting Bugs

Report bugs at [Issues](https://github.com/software-students-fall2023/3-python-package-exercise-experientia/issues).

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Submitting Enhancements

If you're proposing enhancements or new features:

* Open a new issue [here](https://github.com/software-students-fall2023/3-python-package-exercise-experientia/issues), describing the enhancement.
* Include the 'enhancement' label on the issue.

Thank you for your interest in rizz! 
