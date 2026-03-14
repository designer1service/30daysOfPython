Day 10 — Loops  

> **Today's Focus:** Practice while and for loops, `range()`, nested loops, and loop control (`break`, `continue`, `else`, `pass`) to handle repetitive tasks in Python.
> **Author:** Luka Marinkovic  

## What I learned  

I used **while** loops to repeat code while a condition is true and saw how an optional `else` block runs when the loop finishes without a `break`. I practiced `break` to stop a loop early and `continue` to skip the rest of the current iteration, both in while and for loops. I also learned how **for** loops work over different iterables such as lists, tuples, strings, sets, and dictionaries, including iterating over keys and key–value pairs with `.items()`. 
## For loops, range, and patterns  

I used `range()` to generate sequences of numbers with different start, stop, and step values (up, down, even steps) and looped over them with for loops. With nested loops I printed a grid of `#` characters, and I also built a triangle pattern and a small multiplication table of squares from 0 to 10. I rewrote simple counting tasks (0→10 and 10→0) using both for and while loops to see how the two approaches compare. 

## Loop control and special constructs  

I combined for loops with `break` and `continue` to stop at a specific value (like 3) or to skip printing extra messages for that value while still continuing the loop. I tried the `for ... else` pattern, where the `else` executes after the loop completes, and used `pass` as a placeholder in a loop body. This helped me understand how to structure loops cleanly even when I have not yet implemented all the logic. 

## Exercises with collections and data  

I iterated over a list of technologies (`['Python', 'Numpy', 'Pandas', 'Django', 'Flask']`) and printed each item using a for loop. I used loops to sum all numbers from 0 to 100, then separately calculated the total of even numbers and the total of odd numbers. I reversed a fruit list using a while loop and index swapping, and for the country/language data I looped through nested structures to count unique languages, find the most spoken languages, and list the top 10 most populated countries. 