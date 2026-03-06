# Day 02 — Variables and Functions

> **Today's Focus:** Deep dive into variables, basic built-in functions, user input, and type casting.  
> **Author:** Luka Marinkovic

## What I learned

Today I focused on how Python handles **variables** and **built-in functions**. I learned the standard naming conventions in Python and how to convert data from one type to another (casting). 

## Key Concepts Covered

### Naming Conventions
- Python uses `snake_case` for variable names (e.g., `first_name`, `is_married`).
- Variables are created simply by assigning a value 
- I practiced **multiline declaration**, which allows assigning multiple variables in a single line:
  `first_name, age, is_student = 'luka', 21, True`

### Built-in Functions
I experimented with several essential built-in functions:
- `min()` and `max()` to find the smallest or largest item in a sequence.
- `sum()` to add up items in a list.
- `len()` to find the length of a string (or a list).
- `input()` to pause the program and take text input directly from the user.

### Type Casting (Converting Data Types)
Because `input()` always returns a string, I learned how to cast it into a number so I can do math with it. I practiced casting across multiple types:
- `int("10")` → converts string to an integer `10`
- `float(10)` → converts integer to a decimal `10.0`
- `str(10)` → converts integer to a string `"10"`
- `list("marko")` → splits a string into a list of characters `['m', 'a', 'r', 'k', 'o']`

## What I completed

I completed the Day 2 exercises by:
- Creating variables of different data types (strings, ints, booleans).
- Checking variable types using `type()` and lengths using `len()`.
- Performing arithmetic operations and saving the results into new variables.
- Using `input()` to prompt the user for their name, age, and country.
- Writing a simple `if/else` statement to compare the lengths of my first and last name.

