# Python Data Structures

This project focuses on understanding and implementing various data structures in Python, particularly lists and tuples. These fundamental data structures are essential for efficient data organization and manipulation in Python programming.

## Resources

### Read or Watch
- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (until 5.3. Tuples and Sequences included)
- [Learn to Program 6: Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

## Learning Objectives

At the end of this project, you should be able to explain the following without external assistance:

### General
- What lists are and how to use them
- Differences and similarities between strings and lists
- Common methods of lists and their usage
- How to use lists as stacks and queues
- What list comprehensions are and how to use them
- What tuples are and how to use them
- When to use tuples versus lists
- What a sequence is
- What tuple packing is
- What sequence unpacking is
- What the `del` statement is and how to use it

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should follow the pycodestyle (version 2.7.*)
- All files must be executable
- The length of files will be tested using wc

## Tasks

### 0. Print a list of integers
Write a function that prints all integers of a list.
- Prototype: `def print_list_integer(my_list=[])`
- Format: one integer per line
- Not allowed to import any module
- Assume the list only contains integers
- Use `str.format()` to print integers

### 1. Secure access to an element in a list
Write a function that retrieves an element from a list.
- Prototype: `def element_at(my_list, idx)`
- Return None if idx is negative or out of range
- Not allowed to use try/except

### 2. Replace element
Write a function that replaces an element of a list at a specific position.
- Prototype: `def replace_in_list(my_list, idx, element)`
- Return original list if idx is negative or out of range

### 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.
- Prototype: `def print_reversed_list_integer(my_list=[])`
- Use `str.format()` to print integers

### 4. Replace in a copy
Write a function that replaces an element in a list without modifying the original.
- Prototype: `def new_in_list(my_list, idx, element)`
- Return a copy of the original list if idx is negative or out of range

### 5. Can you C me now?
Write a function that removes all characters c and C from a string.
- Prototype: `def no_c(my_string)`
- Not allowed to use `str.replace()`

### 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.
- Prototype: `def print_matrix_integer(matrix=[[]])`

### 7. Tuples addition
Write a function that adds 2 tuples.
- Prototype: `def add_tuple(tuple_a=(), tuple_b=())`
- Returns a tuple with 2 integers
- Use 0 for missing integers in tuples smaller than 2
- Use only the first 2 integers for tuples bigger than 2

### 8. More returns!
Write a function that returns a tuple with the length of a string and its first character.
- Prototype: `def multiple_returns(sentence)`
- First character should be None if string is empty

### 9. Find the max
Write a function that finds the biggest integer of a list.
- Prototype: `def max_integer(my_list=[])`
- Return None if list is empty
- Not allowed to use the built-in `max()`

### 10. Only by 2
Write a function that finds all multiples of 2 in a list.
- Prototype: `def divisible_by_2(my_list=[])`
- Return a new list with True/False values

### 11. Delete at
Write a function that deletes an item at a specific position in a list.
- Prototype: `def delete_at(my_list=[], idx=0)`
- Not allowed to use `pop()`

### 12. Switch
Complete the source code to switch the values of a and b.
- Program should be exactly 5 lines long