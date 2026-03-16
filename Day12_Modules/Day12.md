Day 12 — Modules  

> **Today’s Focus:** Import and use both built‑in and custom modules, and build small utilities using randomness, strings, and colors.  
> **Author:** Luka Marinkovic  

## What I learned  

I practiced different ways of importing modules: importing a whole module with an alias, importing specific functions or variables, and renaming them on import. I looked at examples with custom modules and several standard library modules like `os`, `sys`, `statistics`, `math`, `string`, and `random`. This showed how much functionality Python gives “out of the box” without having to write everything myself.  

## Built-in modules I explored  

With the `os` module I reviewed typical filesystem operations such as creating, changing, and removing directories. The `sys` examples showed how to read command‑line arguments, inspect the Python version, and exit a program early. I also saw how `statistics` can compute median, mode, and standard deviation, how `math` provides constants and numeric helpers, how `string` exposes ready‑made character sets (letters, digits, punctuation), and how `random` generates random floats and integers.  

## Random IDs and colors  

Using `random` and `string`, I wrote `random_user_id()` which generates a configurable number of random user IDs, each of a configurable length, built from letters, digits, and symbols. I created `rgb_color_gen()` to generate a single random RGB color string of the form `rgb(r,g,b)` with each component between 0 and 255. I then expanded this idea with `list_of_rgb_colors(number)` and `list_of_hexa_colors(number)` to return lists of random RGB and hexadecimal colors.  

## Color generator interface  

On top of the color helpers, I implemented `generate_colors(name, number)` as a small interface that decides whether to produce RGB or hex colors based on the `name` argument. It calls the appropriate list function and returns a list of random colors for further use. This exercise helped me combine multiple small functions into one higher‑level utility that behaves differently depending on the input parameters.  

## Shuffling and unique random lists  

I used `random.shuffle()` inside `shuffle_list(item_list)` to randomly reorder the elements of a list and return the shuffled result. I also wrote `unique_list()` to generate a list of seven unique random digits in the range 0–9 by repeatedly drawing numbers and only appending them if they are not already present. Together, these exercises strengthened my understanding of randomness, uniqueness checks, list mutation, and how modules make such tasks straightforward in Python.  

