## Day 25 — First steps with pandas  

> Today’s focus: learn how to create and inspect pandas Series and DataFrames, load CSV files, manipulate columns, and perform simple analysis on tabular datasets.  
> Author: Luka Marinkovic  

### Creating Series and DataFrames  

I started by creating pandas Series from Python lists, custom indices, dictionaries, and even from NumPy linspace values. This showed how flexible Series are as labeled one‑dimensional data structures. Then I built DataFrames from lists of lists, dictionaries, and lists of dictionaries to understand different ways of structuring tabular data. Seeing the same small dataset created in multiple ways helped me understand how to choose the most convenient input format in real projects.  

### Loading CSV data and basic inspection  

I loaded real data from CSV files using `pd.read_csv`, such as a `weight-height.csv` dataset and a `hacker_news.csv` dataset. With methods like `head()`, `tail()`, `columns`, `shape`, `info()`, and `describe()`, I checked the first and last rows, column names, data types, and basic statistics. This gave me a workflow for quickly understanding an unfamiliar dataset before doing any deeper analysis or cleaning.  

### Adding, transforming, and formatting columns  

On a small custom DataFrame containing names and locations, I added new columns for weight and height and then converted height from centimeters to meters by multiplying by `0.01`. I wrote a simple function to calculate BMI row by row, added it as a new column, and rounded the values for a cleaner display. Later, I added birth year and current year columns, converted string years to integers, and computed ages, which showed how numeric operations can be applied across an entire column.  

### Working with data types and arithmetic  

I inspected the data types of columns using attributes like `dtype` and converted types with `.astype()`. Converting the `Birth Year` and `Current Year` columns from strings to integers allowed me to subtract them and derive an `Ages` column. This emphasised how important correct data types are for computations and how pandas makes bulk type conversion and arithmetic straightforward.  

### Filtering text data in a real dataset  

With the `hacker_news.csv` data, I practiced filtering rows based on text conditions in the `title` column. Using `str.contains` with `case=False`, I selected all rows whose titles mention “python” or “javascript”, creating focused subsets of the data. This showed how powerful and concise pandas is for searching and filtering text within large datasets, which is a common task in data exploration and analysis.