# Python - More Classes and Objects

## Resources
To complete this project, it is recommended to read or watch the following resources:

- **Object-Oriented Programming**
	Read everything until the paragraph “Inheritance” (excluded).
- **Object-Oriented Programming**
	Focus on the following sections:
	- General Introduction
	- First-class Everything
	- A Minimal Class in Python
	- Attributes
	- Methods
	- The `__init__` Method
	- Data Abstraction, Data Encapsulation, and Information Hiding
	- `__str__`- and `__repr__`-Methods
	- Public, Protected, and Private Attributes
	- Destructor
- **Class and Instance Attributes**
- **`classmethods` and `staticmethods`**
- **Properties vs. Getters and Setters**
	Focus on the last part: “Public instead of Private Attributes.”
- **`str` vs `repr`**

---

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without external resources:

### General
- Why Python programming is awesome.
- What is Object-Oriented Programming (OOP)?
- What does “first-class everything” mean in Python?
- What is a class?
- What is an object or instance?
- What is the difference between a class and an object/instance?
- What is an attribute?
- How to use public, protected, and private attributes.
- What is `self` in Python?
- What is a method?
- What is the special `__init__` method, and how is it used?
- What are Data Abstraction, Data Encapsulation, and Information Hiding?
- What is a property in Python?
- What is the difference between an attribute and a property?
- What is the Pythonic way to write getters and setters?
- What are the special `__str__` and `__repr__` methods, and how are they used?
- What is the difference between `__str__` and `__repr__`?
- What is a class attribute?
- What is the difference between an object attribute and a class attribute?
- What is a class method?
- What is a static method?
- How to dynamically create arbitrary new attributes for existing instances of a class.
- How to bind attributes to objects and classes.
- What is the `__dict__` attribute of a class and an instance?
- How does Python find the attributes of an object or class?
- How to use the `getattr` function.

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should follow the `pycodestyle` (version 2.7.*) style guide.
- All files must be executable.
- File lengths will be tested using `wc`.

---

## Tasks

### 0. Simple Rectangle
- Create an empty class `Rectangle` that defines a rectangle.
- **File:** `0-rectangle.py`

---

### 1. Real Definition of a Rectangle
- Add private instance attributes `width` and `height` with property getters and setters.
- **File:** `1-rectangle.py`

---

### 2. Area and Perimeter
- Add methods to calculate the area and perimeter of the rectangle.
- **File:** `2-rectangle.py`

---

### 3. String Representation
- Implement `__str__` to print the rectangle using the `#` character.
- **File:** `3-rectangle.py`

---

### 4. Eval is Magic
- Implement `__repr__` to return a string representation that can recreate the instance using `eval()`.
- **File:** `4-rectangle.py`

---

### 5. Detect Instance Deletion
- Print a message when an instance of `Rectangle` is deleted.
- **File:** `5-rectangle.py`

---

### 6. How Many Instances
- Add a public class attribute `number_of_instances` to track the number of instances.
- **File:** `6-rectangle.py`

---

### 7. Change Representation
- Add a public class attribute `print_symbol` to customize the string representation.
- **File:** `7-rectangle.py`

---

### 8. Compare Rectangles
- Add a static method `bigger_or_equal` to compare two rectangles based on their area.
- **File:** `8-rectangle.py`

---

### 9. A Square is a Rectangle
- Add a class method `square` to create a square (a rectangle with equal width and height).
- **File:** `9-rectangle.py`

---

## Repository
- **GitHub Repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-more_classes`

---