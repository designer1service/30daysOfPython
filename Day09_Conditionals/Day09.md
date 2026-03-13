Day 9 — Conditionals

> Today I worked with conditionals to control the flow of my Python programs using if, elif, else, logical operators, and nested decisions.
> Author: Luka Marinkovic  

## What I learned

I learned how to use `if`, `elif`, and `else` to run different blocks of code depending on whether conditions are true or false. I practiced simple conditions, chained conditions, shorthand one‑line conditionals, and nested conditions that check multiple properties of a value. I also used logical operators `and` and `or` to combine more than one condition in a single expression. 
## Basic conditionals and nesting

I started with simple checks to see if a number is positive, negative, or zero using `if`, `if/else`, and `if/elif/else` structures. Then I wrote nested `if` statements to check if a number is positive and at the same time even or odd, which showed how conditions can be placed inside other conditions. I later simplified some nested logic using `and` so one `if` line could describe two requirements at once.

## Short hand and logical operators

I used shorthand if expressions to write compact one‑line conditionals, such as printing whether a number is positive or negative in a single statement. With logical operators, I checked combinations like “positive and even” or “user is admin or has high access level”. This made my code more readable than deeply nested structures for the same checks. 
## User input and simple applications

I wrote small programs that asked the user for input and reacted based on the answers. These included checking if someone is old enough to drive, comparing the user’s age with my own, and determining which of two numbers is greater. I also implemented a grading script that maps numeric scores to letter grades and a month‑to‑season converter based on the month name. 
## Lists, sets, and dictionaries with conditionals

I used `if` with the `in` keyword to check if a fruit is already in a list and only append it if it is missing. For the `person` dictionary, I first checked if the `skills` key exists and then printed the **middle** skill using the corrected index `len(person['skills']) // 2`. I checked whether `'Python'` is in the skills, classified the person as front‑end, back‑end, full‑stack, or unknown based on their skills set, and finally combined conditions on `is_married` and `country` to print a formatted sentence about their life situation. 

