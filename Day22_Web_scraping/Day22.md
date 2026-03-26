## Day 22 — Web Scraping  

> Today’s focus: fetch web pages with `requests`, parse HTML and embedded JSON using BeautifulSoup and `json`, and reshape scraped data into clean Python and JSON structures.  
> Author: Luka Marinkovic  

### What I learned  

I used the `requests` library to send HTTP GET requests and inspected the response status code, raw content, and HTML body. With BeautifulSoup I parsed the HTML using the `'html.parser'` parser and explored elements like `<title>`, `<body>`, and collections of tags found via `find` and `find_all`. I also learned that some modern sites expose data inside `<script>` tags as JSON, so scraping sometimes means parsing JSON rather than only traversing visible HTML tables.  

### Scraping UCI Machine Learning Archive  

On the UCI archive page, I first looked for old‑style HTML tables but found none with the expected structure. Instead I located a `<script>` tag with `type="application/json"` and a custom `data-sveltekit-fetched` attribute, extracted its text, and parsed it twice with `json.loads` to reach the nested data. From the resulting object I pulled out the `datasets` list and iterated over it, printing each dataset name along with its URL folder. In a second pass I normalized each dataset into a dictionary with keys like `name`, `area`, `task`, `types`, `instances`, `features`, `feature_types`, and `url_folder`, and wrapped them into a `"datasets"` object suitable for saving as a JSON file.  

### Scraping Boston University facts and stats  

For the Boston University “Facts & Stats” page, I used BeautifulSoup to target specific sections whose titles are in `<h4 class="stat-group-title">` elements. I found the “Quick Facts & Stats”, “Community”, “Campus”, and “Academics” sections, then navigated into their parent containers to locate lists of statistics. Depending on the section, I extracted stat labels and values from combinations of `<article>` tags with `bu-stat-single` class and `<li>` items inside `custom-stat-list` lists. I built nested dictionaries where each section title maps to another dictionary of `{label: value}` pairs, then combined all sections into one top‑level `data` dictionary.  

### Scraping US presidents from Wikipedia  

On the Wikipedia page listing presidents of the United States, I identified the first `.wikitable` and iterated its `<tr>` rows inside the `<tbody>`. I distinguished rows that start a new president (with a numbered `<th scope="row">`) from continuation rows that only add extra election information. For each new president row I extracted the ordinal number, name, term text (dates), party, election description, and vice presidential data from specific table cells. I grouped data by president name in a `presidents_by_name` dictionary, storing a list of term objects so that presidents with multiple terms have multiple entries. For continuation rows, I added extra elections to the last term’s `elections` list.  

### Saving structured scrape results  

After processing all rows, I converted the `presidents_by_name` dictionary into a list under a `"presidents"` key and wrote it out to `task3.json` using `json.dump` with indentation and UTF‑8 encoding. I used the same pattern (commented in the code) for the BU stats and UCI dataset scraping tasks, where the cleaned Python structures can be persisted as JSON for analysis later. This day tied together HTTP requests, HTML parsing, JSON handling, and careful table/DOM navigation to build reliable web scrapers.