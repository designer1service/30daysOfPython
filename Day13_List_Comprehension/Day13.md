Day 13 — List Comprehension  

> **Today’s Focus:** Use list comprehensions and lambda functions to write shorter, more expressive Python code.  
> **Author:** Luka Marinkovic  

## What I learned  

I practiced **list comprehensions** as a compact way to create lists from sequences, often replacing longer for‑loops. I also worked with **lambda functions** to define small anonymous functions inline, including using them inside other functions. This helped me write more concise code while keeping the logic readable.

## List comprehensions in practice  

I rewrote simple loops as comprehensions, such as turning a string into a list of characters and generating ranges of numbers and their squares. I created lists of tuples like `(i, i²)` and extended that idea to build sequences of powers from `i⁰` to `i⁵` for values from 0 to 10. I also filtered sequences with conditions, for example selecting only even or odd numbers, positive even numbers from a mixed list, and flattening nested lists into a single flat list. 

## Exercises with structured data  

Using list comprehension, I filtered only negative and zero values from a list. I flattened a list of country–capital pairs into different structures: one as a list of `[COUNTRY, CODE, CAPITAL]` (upper‑cased with country codes), another as a list of dictionaries with `country` and `city` keys. I also transformed a list of name tuples into a list of full name strings by concatenating first and last names in a single comprehension. 

## Lambda functions and power helpers  

I converted a normal `add_two_nums` function into a lambda and used other lambdas for squaring a number and computing expressions with multiple variables. I defined a `power(x)` function that returns a lambda, allowing me to compute `x**n` in a higher‑order style like `power(2)(3)`. Finally, I wrote lambda functions to calculate the slope and y‑intercept of a linear function from two points, which combined math with concise anonymous functions. 