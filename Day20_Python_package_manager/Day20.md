## Day 20 — Python Packages and APIs  

> Today’s focus: manage packages with pip, use third‑party libraries (like `requests` and `numpy`), and work with HTTP APIs and online text data.  
> Author: Luka Marinkovic  

### What I learned  

I practiced using `python -m pip` to install, uninstall, list, and inspect packages such as `numpy` and `pandas`. I checked installed versions with `pip list`, viewed detailed metadata with `pip show`, and saw how `pip freeze` can generate exact version pins suitable for a `requirements.txt` file. Inside Python, I imported `numpy`, converted a list to a NumPy array, and performed vectorized operations like scaling and shifting all elements at once.  

I used the `requests` library to send HTTP GET requests to different URLs and inspected the response status code, headers, raw text, and JSON content. I experimented with scraping a plain text book from Project Gutenberg, cleaning the text using regular expressions, and counting word frequencies to find the ten most common words. This combined HTTP requests, regex cleaning, and basic dictionary frequency analysis.  

From a cat breeds API, I downloaded JSON data and computed descriptive statistics about cat weights and life spans. I parsed metric weight strings like `"3 - 5"` into numeric ranges, converted them to floats, and averaged the endpoints for each breed. Using the `statistics` module, I calculated minimum, maximum, mean, median, and standard deviation for the resulting lists. I repeated the same pattern for life span values and also counted how many breeds come from each country of origin.  

Using the REST Countries API, I fetched country data fields such as name, population, area, and languages. I sorted countries by area to build a list of the ten largest countries with their official names and areas. I also iterated through the nested `languages` objects, counted how many times each language appears across all countries, sorted the counts, and printed the ten most common languages along with the total number of distinct languages. These tasks showed how to navigate nested JSON structures, aggregate information, and sort complex data returned by web APIs.  

***

## Further Information About Packages  

### Database  

- **SQLAlchemy / SQLObject** – Object‑oriented access to different database systems  
  - `pip install SQLAlchemy`  

### Web development  

- **Django** – High‑level web framework  
  - `pip install django`  
- **Flask** – Micro web framework based on Werkzeug and Jinja2 (BSD licensed)  
  - `pip install flask`  

### HTML parsing  

- **Beautiful Soup** – HTML/XML parser for quick screen‑scraping and messy markup  
  - `pip install beautifulsoup4`  
- **PyQuery** – jQuery‑like HTML parser in Python, often faster than BeautifulSoup  

### XML processing  

- **ElementTree** – Flexible container for hierarchical data structures like XML infosets  
  - (Included in the Python standard library in modern versions)  

### GUI  

- **PyQt** – Python bindings for the cross‑platform Qt framework  
- **Tkinter** – Traditional GUI toolkit bundled with Python  

### Data analysis, data science, and machine learning  

- **NumPy** – Core numerical computing library for Python (arrays, linear algebra, etc.)  
- **Pandas** – High‑level data structures and tools for data analysis and time series  
- **SciPy** – Scientific computing library with optimization, linear algebra, integration, image processing, and statistics  
- **Scikit‑Learn** – Machine learning library built on NumPy and SciPy, great for working with complex data  
- **TensorFlow** – Machine learning and deep learning library originally from Google  
- **Keras** – High‑level neural networks API that simplifies model definition, training, and visualization  

### Network  

- **requests** – User‑friendly HTTP client for sending GET, POST, PUT, DELETE and other requests  
  - `pip install requests`