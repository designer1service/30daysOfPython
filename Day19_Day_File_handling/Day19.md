## Day 19 — File Handling  

> **Today’s Focus:** Read and write text, JSON, CSV, and XML files in Python, and solve small data tasks using file input and output.  
> **Author:** Luka Marinkovic  

### File mode cheat sheet

```python
open("filename", mode)
```

| Mode | Meaning                                           |
|------|---------------------------------------------------|
| `r`  | Read (default). Error if file does not exist.     |
| `a`  | Append. Creates file if it does not exist.        |
| `w`  | Write. Overwrites file or creates it if missing.  |
| `x`  | Create. Error if file already exists.             |
| `t`  | Text mode (default).                              |
| `b`  | Binary mode (e.g. images).                        |

### What I learned  

I practiced opening files with different modes and reading text files using `read()`, `read(n)`, `readline()`, `readlines()`, and `splitlines()`. I used a `with` context manager so files close automatically and rewound the file pointer with `seek(0)` when needed. I also learned how to append to a file, create/overwrite files, and delete them safely using `os.path.exists()` and `os.remove()`.  

### JSON, CSV, and XML handling  

I used the `json` module to move between JSON and Python data structures. I parsed a JSON string into a dictionary with `json.loads`, converted a dict back to a JSON string with `json.dumps`, and maintained a JSON file containing a list of people using `json.load` and `json.dump`. With the `csv` module I read rows from a CSV file, printed the header, and formatted each row into a human‑readable sentence. I also parsed an XML file using `xml.etree.ElementTree`, accessed the root tag and attributes, and iterated over child elements to inspect their fields.  

### Text and JSON exercises  

I wrote `read_line(path)` to count non‑empty lines and total words in a text file. I implemented `most_spoken_languages(path, count)` to load a countries JSON file, count how often each language appears, sort the results, and return the top N languages. I also created `most_populated_countries(path, count)` to sort countries by population and build a list of dictionaries with `country` and `population` for the top entries.  

### Email extraction and word frequency  

From an email log, I extracted all recipient addresses by selecting lines starting with `To:` and cleaning the prefix before putting them into a set of unique emails. I wrote `find_most_common_words(text_or_path, count)` that can accept either a filename or raw text, normalizes the text to lowercase, strips punctuation, counts word frequencies, and returns the most common words.  

### Text cleaning, similarity, and CSV analysis  

Using regular expressions and a stop‑word list, I built `clean_text`, `remove_support_words`, and `check_text_similarity` to compare two texts based on the important words they share, calculating similarity with a Jaccard‑style formula. Finally, I analyzed a `hacker_news.csv` file: I iterated through each row, counted how many lines mention “javascript” versus “java”, and tracked the total line count while printing the CSV header.