# Python - Test-Driven Development

This project focuses on the principles of **Test-Driven Development (TDD)** in Python. It includes the implementation of various functions and their corresponding test cases to ensure correctness and robustness.

## Learning Objectives

By completing this project, you will learn:

- The importance of writing tests before implementing code.
- How to write documentation for modules and functions.
- How to use `doctest` and `unittest` for testing Python code.
- How to identify and handle edge cases in your code.

## Project Structure

The project is organized as follows:

```
holbertonschool-higher_level_programming/
├── python-test_driven_development/
│   ├── 0-add_integer.py
│   ├── 2-matrix_divided.py
│   ├── 3-say_my_name.py
│   ├── 4-print_square.py
│   ├── 5-text_indentation.py
│   ├── 6-max_integer.py
│   ├── tests/
│   │   ├── 0-add_integer.txt
│   │   ├── 2-matrix_divided.txt
│   │   ├── 3-say_my_name.txt
│   │   ├── 4-print_square.txt
│   │   ├── 5-text_indentation.txt
│   │   ├── 6-max_integer_test.py
```

## Files and Descriptions

### Python Files

1. **`0-add_integer.py`**
   - Function: `add_integer(a, b=98)`
   - Adds two integers or floats and returns the result as an integer.
   - Raises `TypeError` if inputs are not integers or floats.

2. **`2-matrix_divided.py`**
   - Function: `matrix_divided(matrix, div)`
   - Divides all elements of a matrix by a number and returns a new matrix.
   - Raises `TypeError` or `ZeroDivisionError` for invalid inputs.

3. **`3-say_my_name.py`**
   - Function: `say_my_name(first_name, last_name="")`
   - Prints "My name is `<first_name>` `<last_name>`".
   - Raises `TypeError` if inputs are not strings.

4. **`4-print_square.py`**
   - Function: `print_square(size)`
   - Prints a square of size `size` using the `#` character.
   - Raises `TypeError` or `ValueError` for invalid inputs.

5. **`5-text_indentation.py`**
   - Function: `text_indentation(text)`
   - Prints text with two new lines after `.`, `?`, and `:`.
   - Raises `TypeError` if input is not a string.

6. **`6-max_integer.py`**
   - Function: `max_integer(list=[])`
   - Returns the maximum integer in a list.
   - Returns `None` if the list is empty.
   - Raises `TypeError` if input is not a list.

### Test Files

1. **`tests/0-add_integer.txt`**
   - Contains `doctest` cases for `add_integer`.

2. **`tests/2-matrix_divided.txt`**
   - Contains `doctest` cases for `matrix_divided`.

3. **`tests/3-say_my_name.txt`**
   - Contains `doctest` cases for `say_my_name`.

4. **`tests/4-print_square.txt`**
   - Contains `doctest` cases for `print_square`.

5. **`tests/5-text_indentation.txt`**
   - Contains `doctest` cases for `text_indentation`.

6. **`tests/6-max_integer_test.py`**
   - Contains `unittest` cases for `max_integer`.

## How to Run Tests

### Using `doctest`

To run `doctest` cases, use the following command:

```bash
python3 -m doctest -v ./tests/<test_file>.txt
```

Example:

```bash
python3 -m doctest -v ./tests/0-add_integer.txt
```

### Using `unittest`

To run `unittest` cases, use the following command:

```bash
python3 -m unittest tests.<test_file>
```

Example:

```bash
python3 -m unittest tests.6-max_integer_test
```

## Requirements

- Python 3.8.5
- All files are interpreted/compiled on Ubuntu 20.04 LTS.
- Code follows the `pycodestyle` (version 2.7.*) style guide.

## Author

This project was completed as part of the curriculum at Holberton School.
**Author:** Ali MEdjnoun
**GitHub Repository:** [holbertonschool-higher_level_programming](https://github.com/your-repo-link)
