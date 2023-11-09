![Workflow Status](https://github.com/software-students-fall2023/3-python-package-exercise-experientia/actions/workflows/python.yml/badge.svg)

# PyRizz: Your Source for Playful Pickup Lines
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

```
from pyrizz import pyrizz

print(pyrizz.get_random_categoryy_line('romantic'))
print(pyrizz.get_random_categoryy_line('clever'))
print(pyrizz.get_random_categoryy_line('geeky'))
print(pyrizz.get_random_categoryy_line('dev'))
```

### get_ai_line(keyword)

In this function, you can retreive a generated pickup line using openai based on any keyword that you suggest. In this example, it would output a Shakespearean pickup line: 

```
from pyrizz import pyrizz

print(pyrizz.get_ai_line('shakespeare'))
```

### rate_line(pickup_line)

In this function, you can rate your very own pickup line out of 10 using openai. Simply type your pickup line and a rating will output: 

```
from pyrizz import pyrizz

print(pyrizz.rate_line('Are you from Tennesse? Cause you're the only 10 I see.'))
```

### create_line(template_number, words)

In this function, if you're new to pickup lines, you can create your very own pickup using some of our templates!
- **template_number** - You need to input a template number (0-39). You can find out the templates by calling the list_templates() function: `print(pyrizz.list_templates())`. This way you can see how the templates look like, how many words you need to include and which one you like!
- **words** - You need to input a list of all the words, for example if you need to input 2 words: `words = ["word1", "word2"]`

This function returns your line with some lovely ASCII art as well! Enjoy!
Here is an example: 
```
from pyrizz import pyrizz

words_to_use = ["sun"]
output = pyrizz.create_line(1, words_to_use)
print(output)
```

### Accessing an Example: 
You can access our example file which utilizes all of these functions with an awesome user interface: 
[Example File](https://github.com/software-students-fall2023/3-python-package-exercise-experientia/blob/main/src/pyrizz/__main__.py)

To access it simply run: `pipenv run python -m pyrizz` on the directory of the repository when cloned. 

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

### Reporting Bugs

Report bugs at https://github.com/yourusername/pyrizz/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Submitting Enhancements

If you're proposing enhancements or new features:

* Open a new issue at https://github.com/yourusername/pyrizz/issues, describing the enhancement.
* Include the 'enhancement' label on the issue.

Thank you for your interest in rizz! 
