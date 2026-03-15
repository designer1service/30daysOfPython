Day 11 — Functions  

> **Today’s Focus:** Define, call, and combine functions with different kinds of parameters, returns, recursion, and small utility helpers for math and validation.
> **Author:** Luka Marinkovic  

## What I learned  

I defined many **functions** to avoid repeating code and to give each piece of logic a clear name and purpose. I practiced functions with no parameters, simple return values, and functions that accept one or more parameters. I also used default values, variable‑length positional arguments (`*args`), and keyword arguments (`**kwargs`) to make functions more flexible. 

## Core function patterns  

I started with basic examples like `generate_full_name`, `add_two_numbers`, `square_number`, `area_of_circle`, and `calculate_age` to see how parameters and return values work. Then I wrote small utilities such as `is_even`, `find_even_numbers`, `sum_of_numbers`, `sum_of_odds`, and `sum_of_evens` to work with numeric ranges. I used default parameters (for example in `generate_full_name` and `calculate_age`) and keyword arguments to call functions in a more explicit way. 

## Flexible arguments and higher-order functions  

I used `*args` in functions like `sum_all_nums`, `add_all_nums`, and `generate_groups` to handle an arbitrary number of positional arguments. I used `**kwargs` to accept arbitrary named arguments and looped through them to print keys and values, as in `arbitrary_named_args` and `show_args`. I also passed a function as an argument to another function in `do_something(square_num, 3)`, which showed how functions can be treated as first‑class values. 

## Problem‑solving with functions  

I solved practical problems by wrapping logic in functions: temperature conversion (`convert_celsius_to_fahrenheit`), season detection (`check_season`), line slope (`calculate_slope`), and quadratic equations (`solve_quadratic_eqn`). I worked with lists using helpers such as `print_list`, `reverse_list`, `capitalize_list_items`, `add_item`, `remove_item`, and several versions of `is_unique` to check item uniqueness. I also implemented `evens_and_odds`, a recursive `factorial`, and validation helpers like `valid_variable` and `is_unique_data`. 

## Simple statistics and data utilities  

I wrote a small statistics toolkit with functions to compute **mean**, **median**, **mode**, **range**, **variance**, and **standard deviation** for a list of numbers, using loops and formulas instead of built‑in libraries. I implemented `is_prime` to test primality efficiently, using `sqrt` and checking only necessary divisors. Finally, I handled more complex country/language data with `most_spoken_languages` and `most_populated_countries`, which build dictionaries, sort items, and return the top results. 
