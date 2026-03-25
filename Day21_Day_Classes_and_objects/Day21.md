## Day 21 — Classes and Objects  

> Today’s focus: define custom classes with constructors and methods, use inheritance, and encapsulate statistics and accounting logic in objects.  
> Author: Luka Marinkovic  

### Person and Student classes  

I defined a `Person` class with an `__init__` constructor that accepts first name, last name, age, country, and city, with sensible default values. Inside the class I stored data in instance attributes and initialized an empty `skills` list. I added methods like `personal_info()` to return a formatted description string and `add_skill()` to append new skills to the list.  

I then created a `Student` class that inherits from `Person` and adds a `gender` attribute. In its constructor I set `gender` and then called `super().__init__` to initialize the inherited fields. I overrode the info method (named `person_info` in the subclass) to include gender‑aware pronouns like “He” or “She”, while still using the name, age, city, and country attributes from the parent.  

### Statistics class for numeric data  

I implemented a `Statistics` class to wrap a list of ages and provide various descriptive statistics. The constructor stores the data, and methods like `count`, `sum`, `min`, `max`, `range`, `mean`, `median`, `std`, and `var` either compute values directly or use the `statistics` module. For mode and frequency distribution I built a frequency dictionary manually, sorted it, and returned the most common value or a list of `(percentage, value)` pairs.  

The `describe()` method prints a full summary report by calling the other methods and showing all key metrics in one place. Using this class on the given `ages` list allowed me to treat statistical analysis as an object with clear, reusable operations instead of a collection of loose functions.  

### PersonAccount class for incomes and expenses  

I created a `PersonAccount` class to model simple personal finances using sets of `(description, amount)` tuples for incomes and expenses. The constructor stores first and last name along with the income and expense sets. Methods `total_income()` and `total_expense()` loop through these collections, summing the amounts to compute totals.  

The `account_info()` method returns a formatted string summarizing total incomes and expenses, while `add_income()` and `add_expense()` interactively ask the user for a description and amount and add new entries to the corresponding sets. Finally, `account_balance()` calculates the difference between total income and total expense to show the current balance. This class pulls together related data and behavior into one coherent object that can evolve as more features are needed.