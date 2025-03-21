# Python - More Data Structures: Set, Dictionary

## Description
This project explores Python's powerful data structures, specifically sets and dictionaries, along with lambda functions and higher-order functions like map, filter, and reduce. Each task focuses on implementing specific functionality using these concepts.

## Learning Objectives
By the end of this project, you should be able to:
- Understand why Python programming is powerful for data manipulation
- Use sets and their common methods effectively
- Choose between sets, lists, and dictionaries for different scenarios
- Iterate through sets and dictionaries
- Implement lambda functions
- Utilize map, reduce, and filter functions

## Requirements
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/python3`
- Code should follow pycodestyle (version 2.7.*)
- All files must be executable

## Tasks

### 0. Squared Simple
* **File**: `0-square_matrix_simple.py`
* **Description**: Write a function that computes the square value of all integers of a matrix.
* **Prototype**: `def square_matrix_simple(matrix=[])`
* Returns a new matrix of the same size with each value squared, without modifying the original matrix.

### 1. Search and Replace
* **File**: `1-search_replace.py`
* **Description**: Write a function that replaces all occurrences of an element by another in a new list.
* **Prototype**: `def search_replace(my_list, search, replace)`
* Returns a new list with specified elements replaced.

### 2. Unique Addition
* **File**: `2-uniq_add.py`
* **Description**: Write a function that adds all unique integers in a list (only once for each integer).
* **Prototype**: `def uniq_add(my_list=[])`
* Returns the sum of unique integers.

### 3. Present in Both
* **File**: `3-common_elements.py`
* **Description**: Write a function that returns a set of common elements in two sets.
* **Prototype**: `def common_elements(set_1, set_2)`

### 4. Only Differents
* **File**: `4-only_diff_elements.py`
* **Description**: Write a function that returns a set of all elements present in only one set.
* **Prototype**: `def only_diff_elements(set_1, set_2)`

### 5. Number of Keys
* **File**: `5-number_keys.py`
* **Description**: Write a function that returns the number of keys in a dictionary.
* **Prototype**: `def number_keys(a_dictionary)`

### 6. Print Sorted Dictionary
* **File**: `6-print_sorted_dictionary.py`
* **Description**: Write a function that prints a dictionary by ordered keys.
* **Prototype**: `def print_sorted_dictionary(a_dictionary)`
* Keys are sorted alphabetically by first level only.

### 7. Update Dictionary
* **File**: `7-update_dictionary.py`
* **Description**: Write a function that replaces or adds key/value in a dictionary.
* **Prototype**: `def update_dictionary(a_dictionary, key, value)`
* Updates existing keys or creates them if they don't exist.

### 8. Simple Delete by Key
* **File**: `8-simple_delete.py`
* **Description**: Write a function that deletes a key in a dictionary.
* **Prototype**: `def simple_delete(a_dictionary, key="")`
* Only deletes if the key exists.

### 9. Multiply by 2
* **File**: `9-multiply_by_2.py`
* **Description**: Write a function that returns a new dictionary with all values multiplied by 2.
* **Prototype**: `def multiply_by_2(a_dictionary)`

### 10. Best Score
* **File**: `10-best_score.py`
* **Description**: Write a function that returns a key with the biggest integer value.
* **Prototype**: `def best_score(a_dictionary)`
* Returns None if no score is found.

### 11. Multiply by Using Map
* **File**: `11-multiply_list_map.py`
* **Description**: Write a function that returns a list with all values multiplied by a number using map.
* **Prototype**: `def multiply_list_map(my_list=[], number=0)`
* Maximum 3 lines of code.

### 12. Roman to Integer
* **File**: `12-roman_to_int.py`
* **Description**: Write a function that converts a Roman numeral to an integer.
* **Prototype**: `def roman_to_int(roman_string)`
* Handles Roman numerals between 1 and 3999.

## Resources
- Data structures
- Lambda, filter, reduce and map
- Learn to Program 12 Lambda Map Filter Reduce