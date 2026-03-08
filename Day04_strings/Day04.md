# Day 04 — Strings & String Methods

> **Today's Focus:** Working with strings in Python – indexing, slicing, formatting, and using built-in string methods to search and transform text.  
> **Author:** Luka Marinkovic  

## What I learned

Today I focused on treating **Python strings** as sequences of characters and using many built-in methods to inspect, transform, and analyze them. I practiced indexing and slicing, negative indices, escape sequences, and several ways of formatting strings including `%`, `str.format()`, and f-strings. I also learned how methods like `split()`, `join()`, `find()`, `replace()`, `strip()`, and various `is*` checks help with real-world text processing.  

## Key Concepts Covered

### 1. Basic strings and escape sequences
- Creating single-line and multi-line strings, measuring length with `len()`, and printing them.  
- Using escape sequences: `\n` for a new line, `\t` for tabs, `\\` for backslash, and quoting characters with `\"` or `\'` inside strings.  
- Formatting simple text tables using `\t` and `\n` to align headers and rows in console output.  

### 2. String formatting (`%`, `format`, f-strings)
- Old-style `%` formatting with `%s`, `%d`, `%f`, and precision like `%.2f` to format strings, integers, and floats.  
- Using `str.format()` with `{}` placeholders and format specifiers such as `{:.2f}` for two decimal places.  
- F-strings for clear, modern interpolation, for example `f"{a} / {b} = {a/b:.2f}"` and building readable mathematical expressions in one line.  

### 3. Indexing, slicing, and treating strings as sequences
- Accessing characters by index (`word[0]`, `word[1]`, `word[-1]`) and computing the last index via `len(word) - 1`.  
- Slicing substrings with `[start:end]`, using steps like `[start:end:step]`, reversing with `word[::-1]`, and skipping characters.  
- Unpacking characters into multiple variables (for example `a, b, c, d, e = word`) to work with each character separately.  

### 4. String methods for searching and checking content
- Case and style methods: `upper()`, `lower()`, `capitalize()`, `title()`, `swapcase()` for transforming how text looks.  
- Searching for substrings using `find()`, `rfind()`, `index()`, and `rindex()` to get the first or last occurrence, and understanding how they behave when the substring is missing.  
- Using predicate methods like `isalnum()`, `isalpha()`, `isdigit()`, `isdecimal()`, `isnumeric()`, `startswith()`, `endswith()`, and `isidentifier()` to validate and classify strings, including how Unicode digits and superscripts behave.  

### 5. Text processing with `split`, `join`, `replace`, and `strip`
- Splitting text into lists of words using `split()` with default whitespace or with a custom separator such as `', '` or `'y'`.  
- Joining lists back into strings using `' '.join(list)` or `'# '.join(list)` to build phrases, acronyms, and formatted outputs.  
- Replacing parts of strings using `replace()` to change words or clean up noisy substrings.  
- Trimming characters at the start and end of strings with `strip()`, and understanding that its argument is treated as a set of characters, not a full word, plus the related `lstrip()` and `rstrip()` variants.  

## What I completed
I completed the Day 4 string exercises by concatenating words into full phrases and building acronyms like `"PFE"` and `"CFA"` from multi-word names. I practiced checking for substrings using `in`, `index()`, and `find()`, and used `rfind()` and slicing to correctly extract the phrase `"because because because"` from a longer sentence. I worked with methods such as `split()`, `join()`, `replace()`, `strip()`, `startswith()`, `endswith()`, and `isidentifier()` on real examples like company names and library lists, and formatted both descriptive text and arithmetic results with `%`, `format()`, and f-strings to produce clean, readable console output.  