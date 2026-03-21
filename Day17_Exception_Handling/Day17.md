Day 17 — Exception Handling  

> **Today’s Focus:** Handle errors with try–except blocks and practice packing, unpacking, spreading, enumerate, and zip to write cleaner Python code. 
> **Author:** Luka Marinkovic  

## What I learned  

I learned how to use `try`, `except`, `else`, and `finally` blocks to handle exceptions without crashing the program.  I practiced catching specific error types like `TypeError`, `ValueError`, and `ZeroDivisionError`, as well as using `except Exception as e` to capture and print a generic error message. This made error handling feel more controlled and predictable. 

## Packing and unpacking arguments  

I used unpacking to pass a list into a function expecting separate arguments, like using `range(*args)` instead of hard‑coding bounds.  I unpacked lists into variables with the star syntax, for example `fin, sw, nor, *rest = countries` and `one, *middle, last = numbers`, which let me grab the first, middle, and last elements in a single line. I also unpacked a dictionary of person information into a function call with `**dct`, making keyword arguments map directly from dictionary keys. 

## Packing with *args and **kwargs  

I wrote a `sum_all(*args)` function that accepts any number of positional arguments, loops through them, and returns their sum.  I experimented with a `packing_person_info(**kwargs)` function aimed at collecting keyword arguments into a dictionary, which reinforced how `**kwargs` captures named parameters. Although my first version reset `kwargs` inside the function, it still helped me understand how packing dictionaries is supposed to work. 

## Spreading, enumerate, and zip  

I used the “spreading” pattern with `*` to merge multiple lists into a single one, such as combining two number lists or building a list of Nordic countries from two smaller lists.  With `enumerate`, I iterated over lists while also getting the index, and used it to print a message when a specific country like “Finland” was found. I used `zip` to iterate over fruits and vegetables in parallel, building a combined list of dictionaries with paired `fruit` and `vege` keys. 

## Exercises and destructuring practice  

In the Day 17 exercise, I used star unpacking on the `names` list to assign all Nordic countries to `nordic_countries` and separate out `Estonia` and `Russia` into their own variables.  This exercise showed how flexible unpacking can be when splitting a list into “main group + extras”. Overall, the day connected exception handling with powerful argument and iteration patterns that make Python code more expressive and concise.

