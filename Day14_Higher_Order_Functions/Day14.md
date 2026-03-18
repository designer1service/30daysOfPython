Day 14 — Higher Order Functions  

> **Today’s Focus:** Work with higher order functions, decorators, and built‑in tools like map, filter, and reduce to transform and aggregate data.
> **Author:** Luka Marinkovic  

## What I learned  

I reviewed what makes a function a **higher order function**: taking other functions as arguments or returning functions as results.  I also clarified the difference between higher order functions, closures, and decorators in my own words, which helped fix the concepts in my head.  On top of that, I practiced using `map`, `filter`, and `reduce` to build small data pipelines step by step.

## Functions, closures, and decorators  

I wrote functions that accept other functions as parameters (like `higher_order_function(sum_numbers, [1,2,3,4,5])`) and functions that return other functions, such as a selector that returns `square`, `cube`, or `absolute` depending on a string.  I implemented a simple closure (`add_ten`) where the inner function remembers a value defined in the outer scope and uses it later.  I also created decorators, including ones that convert a greeting to uppercase, split a string, apply multiple decorators to the same function, and a decorator that accepts parameters and prints an extra message about where I live. 

## Map, filter, and reduce in practice  

Using `map`, I transformed lists by squaring numbers, converting numeric strings to integers, and uppercasing names.  With `filter`, I extracted only even numbers, longer names, countries containing “land”, countries of certain lengths, and those starting with specific letters, even chaining filters together for combined conditions.  With `reduce`, I combined lists of numbers and strings into single values, such as summing or multiplying all numbers, and building a sentence that lists several Nordic countries in one string. 
## Small data transformations  

I used basic for‑loops to print each country, name, and number from the given lists to compare imperative style with functional tools.  I wrote helpers like `get_string_lists` to filter only strings from a mixed list and used lambda expressions inside `map`, `filter`, and `reduce` for concise inline logic.  I also wrote a function `categorize_countries` that filters countries by patterns in their names (like containing “Den”) and a `dict_country` function that builds a frequency dictionary of countries by their starting letter. 
## Working with country data  

Using the `countries_data` module, I sorted full country records by name, capital, and population, and then extracted the top 10 most populated countries.  I implemented `most_spoken_languages` to count how many countries each language appears in and return the top N languages sorted by this count.  Finally, I wrote simple helpers like `get_first_ten_countries` and `get_last_ten_countries` to slice out sections of the countries list, which gave me practice combining list slicing with higher level data processing. 