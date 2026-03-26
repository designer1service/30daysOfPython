# Python Web Scraping

import requests
from bs4 import BeautifulSoup
import json

url = 'https://archive.ics.uci.edu/datasets'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
print(len(tables))
print(soup.prettify())

# No tables like in the tutorial so we use this tom find script with JSON
script = soup.find("script", attrs={"data-sveltekit-fetched": True, "type": "application/json"})

data = json.loads(script.string)                 # 1. pars content with script tag
body = json.loads(data["body"])                 # 2. body is another tag
datasets = body[0]["result"]["data"]["json"]["datasets"]

for d in datasets:
    print(d["Name"], "->", d["URLFolder"])

# Exercises: Day 22

# 1
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
"""print(soup.title.get_text())
print(soup.body)
print(response.status_code)
"""
data = {}

quick_facts_stats = {}
h4_section1 = soup.find('h4', class_='stat-group-title', string='Quick Facts & Stats')
section_title  = h4_section1.get_text(strip=True)
section1 = h4_section1.parent
div = section1.find('div', class_='bu-stat-list')
articles = div.find_all('article', class_='bu-stat-single')
for article in articles:
    article_title = article.find('h3', class_='bu-stat-title')
    value_spans = article.find_all('span', class_='bu-stat-value-field')
    label = article_title.get_text(strip=True)
    parts = [span.get_text(strip=True) for span in value_spans]
    value = "".join(parts)
    quick_facts_stats[label] = value
data[section_title] = quick_facts_stats

community = {}
h4_section2 = soup.find('h4', class_='stat-group-title', string='Community')
section_title1 = h4_section2.get_text(strip=True)
section2 = h4_section2.parent
ul = section2.find('ul', class_='custom-stat-list')
items = ul.find_all('li')
for item in items:
    label_span = item.find('span', class_='stat-label')
    figure_span = item.find('span', class_='stat-figure')
    label1 = label_span.get_text(strip=True)
    value = figure_span.get_text(strip=True)
    community[label1] = value
data[section_title1] = community

campus = {}
h4_section3 = soup.find('h4', class_='stat-group-title', string='Campus')
section_title2 = h4_section3.get_text(strip=True)
section3 = h4_section3.parent
div = section3.find('div', class_='bu-stat-list')
articles1 = div.find_all('article', class_='bu-stat-single')
for article in articles1:
    article_title1 = article.find('h3', class_='bu-stat-title')
    label2 = article_title1.get_text(strip=True)
    value_spans = article.find('span', class_='bu-stat-value-field')
    value = value_spans.get_text(strip=True)
    campus[label2] = value
data[section_title2] = campus

Academics = {}
h4_section4 = soup.find('h4', class_='stat-group-title', string='Academics')
section_title3 = h4_section4.get_text(strip=True)
section4 = h4_section4.parent
ul = section4.find('ul', class_='custom-stat-list')
items = ul.find_all('li')
for item in items:
    label_span = item.find('span', class_='stat-label')
    figure_span = item.find('span', class_='stat-figure')
    label3 = label_span.get_text(strip=True)
    value = figure_span.get_text(strip=True)
    Academics[label3] = value
data[section_title3] = Academics


print(data)
"""
with open("task.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)"""


# 2
url = 'https://archive.ics.uci.edu/datasets'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
"""print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)"""


script = soup.find("script", attrs={"data-sveltekit-fetched": True, "type": "application/json"})

data = json.loads(script.string)                
body = json.loads(data["body"])                 
datasets = body[0]["result"]["data"]["json"]["datasets"]


clean_datasets = []
for d in datasets:
    item = {
        "name": d["Name"],
        "area": d["Area"],
        "task": d["Task"],
        "types": d["Types"],
        "instances": d["NumInstances"],
        "features": d["NumFeatures"],
        "feature_types": d["FeatureTypes"],
        "url_folder": d["URLFolder"],
    }
    clean_datasets.append(item)
data = {"datasets": clean_datasets}
print(data)

"""with open("task2.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)"""

# 3
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers = {
    "User-Agent": "YourNamePresidentsScraper/0.1 (contact: email@example.com)"
}
response = requests.get(url, headers=headers)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
# print(soup.body)
print(response.status_code)

tables = soup.find_all('table', class_="wikitable")
table = tables[0]
tbody = table.find("tbody")
rows = tbody.find_all("tr")
presidents_by_name = {}
current_number = None
current_name = None
current_term_text = None
current_party = None
current_vp = None

for row in rows:
    cells_td = row.find_all("td")
    cells_th = row.find_all("th")

    if not cells_td and not cells_th:
        continue

    first_th = row.find("th", scope="row")
    if first_th:
        try:
            current_number = int(first_th.get_text(strip=True))
        except ValueError:
            current_number = None
        tds = row.find_all("td")

        # 0: Portrait
        # 1: Name
        # 2: Term
        # 3: Party (color)
        # 4: Party name
        # 5: Election
        # 6: Vice President

        if len(tds) < 5:
            continue

        # Name
        name_cell = tds[1]
        name_link = name_cell.find("a")
        current_name = name_link.get_text(strip=True) if name_link else name_cell.get_text(strip=True)

        # Term ("April 30, 1789 – March 4, 1797")
        term_cell = tds[2]
        current_term_text = term_cell.get_text(" ", strip=True)

        # Party
        party_cell = tds[4] 
        current_party = party_cell.get_text(" ", strip=True)

        # Election 
        election_cell = tds[5]
        election_text = election_cell.get_text(" ", strip=True)

        # Vice President
        vp_cell = tds[6]
        vp_text = vp_cell.get_text(" ", strip=True)

        if current_name not in presidents_by_name:
            presidents_by_name[current_name] = {
                "name": current_name,
                "number": current_number,
                "terms": []
            }

        term_obj = {
            "term_text": current_term_text,
            "party": current_party,
            "elections": [election_text] if election_text else [],
            "vice_president": vp_text
        }
        presidents_by_name[current_name]["terms"].append(term_obj)

    else:
        tds = row.find_all("td")
        if not tds:
            continue

        election_text = tds[0].get_text(" ", strip=True)

        if current_name is None:
            continue

        terms = presidents_by_name[current_name]["terms"]
        if terms:
            last_term = terms[-1]
            if election_text:
                last_term.setdefault("elections", [])
                last_term["elections"].append(election_text)

data = {
    "presidents": list(presidents_by_name.values())
}

with open("task3.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Scraped {len(data['presidents'])} presidents.")
