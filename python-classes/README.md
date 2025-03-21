# Python - Classes and Objects

## Background Context
Understanding Object-Oriented Programming (OOP) is crucial for Python development. This project focuses on learning and experimenting with OOP concepts. It is highly recommended to read and practice all the material provided below to gain a solid understanding.

## Resources
Read or watch the following resources in the given order:

1. **Object Oriented Programming**
	- Read everything until the paragraph "Inheritance" (excluded).
	- Skip class attributes, classmethod, and staticmethod for now.

2. **Object-Oriented Programming**
	- Focus on the following sections:
	  - General Introduction
	  - First-class Everything
	  - A Minimal Class in Python
	  - Attributes (skip class attributes)
	  - Methods
	  - The `__init__` Method
	  - Data Abstraction, Data Encapsulation, and Information Hiding
	  - Public, Protected, and Private Attributes

3. **Properties vs. Getters and Setters**
4. **Learn to Program 9: Object-Oriented Programming**
5. **Python Classes and Objects**
6. **Object-Oriented Programming**

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without external help:

### General
- What is OOP?
- What does "first-class everything" mean?
- What is a class?
- What is an object and an instance?
- Difference between a class and an object or instance.
- What is an attribute?
- How to use public, protected, and private attributes.
- What is `self`?
- What is a method?
- What is the special `__init__` method and how to use it?
- What are Data Abstraction, Data Encapsulation, and Information Hiding?
- What is a property?
- Difference between an attribute and a property in Python.
- Pythonic way to write getters and setters.
- How to dynamically create arbitrary new attributes for existing instances of a class.
- How to bind attributes to objects and classes.
- What is the `__dict__` of a class or instance, and what does it contain?
- How Python finds the attributes of an object or class.
- How to use the `getattr` function.

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code must follow the `pycodestyle` (version 2.7.*) style guide.
- All files must be executable.
- File length will be tested using `wc`.
- All modules, classes, and functions must have documentation using Google Style Python Docstrings.

## Tasks

### 0. My First Square
- Write an empty class `Square` that defines a square.
- **File:** `0-square.py`

### 1. Square with Size
- Add a private instance attribute `size` to the `Square` class.
- **File:** `1-square.py`

### 2. Size Validation
- Validate that `size` is an integer and greater than or equal to 0.
- **File:** `2-square.py`

### 3. Area of a Square
- Add a public instance method `area()` to calculate the square's area.
- **File:** `3-square.py`

### 4. Access and Update Private Attribute
- Add a getter and setter for `size` using the `@property` decorator.
- **File:** `4-square.py`

### 5. Printing a Square
- Add a method `my_print()` to print the square using the `#` character.
- **File:** `5-square.py`

### 6. Coordinates of a Square
- Add a private instance attribute `position` to define the square's position.
- Validate that `position` is a tuple of 2 positive integers.
- Update `my_print()` to account for `position`.
- **File:** `6-square.py`

## Repository
- **GitHub Repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-classes`
