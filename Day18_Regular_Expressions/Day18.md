Day 18 — Regular Expressions  

> **Today’s Focus:** Use Python’s `re` module to search, match, replace, split, and validate text with regular expressions.
> **Author:** Luka Marinkovic  

## What I learned  

I imported the `re` module and practiced the core regex functions: `match`, `search`, `findall`, `sub`, and `split`.  I saw how `match` checks only at the start of a string, `search` finds the first occurrence anywhere, and `findall` returns all matches as a list. I also used `sub` to replace substrings and `split` to break text into pieces based on a regex pattern. 

## Basic patterns and text cleaning  

I wrote simple patterns to find words like “python” or “language”, using flags like `re.I` for case‑insensitive matches and character classes like `[Pp]ython`.  I used `sub` to replace all occurrences of “Python”/“python” with “Java”, and to strip out `%` characters from a noisy text before splitting it into sentences with `re.split('\n', ...)`. These examples showed how regex can clean and transform raw text. 

## Character classes, quantifiers, and anchors  

I used character classes such as `[Aa]pple|[Bb]anana` to match multiple word variants, and escape sequences like `\d` and `\d+` to extract digits and full numbers from a sentence.  I practiced quantifiers: `+` (one or more), `*` (zero or more), `?` (optional hyphen in `e-mail`/`email`), and `{n}`/`{m,n}` to match exact or ranged counts like 4‑digit years. I also used a negated character class `[^A-Za-z ]+` to grab all non‑letter, non‑space characters, understanding the role of `^` inside brackets.  

## Word frequency and numeric extraction exercises  

In the Level 1 exercises, I used `re.findall(r'\b\w+\b', paragraph.lower())` to extract all words from a paragraph, built a frequency dictionary, and sorted by count to see the most frequent words.  I also extracted both negative and positive numbers from a descriptive physics text using the pattern `-?\d+`, converted them to integers, and computed the distance between the two furthest particles as `max − min`. 

## Validation and cleaning with regex  

I implemented `is_valid_variable(name)` to validate Python variable names using the pattern `^[A-Za-z_][A-Za-z0-9_]*$`, which enforces that the name starts with a letter or underscore and is followed by letters, digits, or underscores.  In the Level 3 exercise, I cleaned a very noisy sentence by removing all non‑alphanumeric and non‑space characters with `re.sub(r'[^A-Za-z0-9\s]', '', sentence)`, then used regex again to extract words and compute word frequencies. Finally, I sorted and printed the top three most frequent words, combining regex with basic dictionary and sorting logic. 

## Regex Cheat Sheet (Python `re`)

### Common character classes
- `\d`  – digit (0–9)
- `\D`  – non‑digit
- `\w`  – word char (letters, digits, underscore)
- `\W`  – non‑word char
- `\s`  – whitespace (space, tab, newline)
- `\S`  – non‑whitespace
- `.`   – any character except newline

### Quantifiers
- `*`   – 0 or more times (greedy)
- `+`   – 1 or more times
- `?`   – 0 or 1 time (optional)
- `{n}` – exactly n times
- `{m,n}` – between m and n times
- `{m,}` – m or more times

### Anchors and boundaries
- `^`   – start of string (or line with MULTILINE)
- `$`   – end of string (or line with MULTILINE)
- `\b`  – word boundary
- `\B`  – not a word boundary

### Character classes
- `[abc]`      – any one of a, b, or c
- `[A-Za-z]`   – any letter A–Z or a–z
- `[^abc]`     – any char *except* a, b, or c
- `[0-9]`      – any digit 0–9

### Groups and alternation
- `(abc)`      – capturing group
- `(?:abc)`    – non‑capturing group
- `a|b`        – a or b

### Escaping
- `\.`         – literal dot
- `\\`         – literal backslash
- `\[` `\]` etc. – escape special characters if needed

### Useful Python functions
- `re.match(pattern, text)` – match at start of string
- `re.search(pattern, text)` – first match anywhere
- `re.findall(pattern, text)` – list of all matches
- `re.sub(pattern, repl, text)` – replace matches
- `re.split(pattern, text)` – split by pattern
