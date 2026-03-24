# PIP

# python -m pip --version
# pip 26.0.1 from Python\pythoncore-3.14-64\Lib\site-packages\pip (python 3.14)

# Installing packages using pip
# python -m pip install numpy

"""PS E:\GitHub\30daysOfPython> python
Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) 
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'2.4.2'
>>> lst = [1,2,3,4,5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array([3, 4, 5, 6, 7])
>>>"""

# pandas install # already have it
# python -m pip install pandas
# import pandas

"""import webbrowser

url_list = [
    'http://www.python.org',
    'https://youtube.com',
    'https://github.com',
    'https://instagram.com',
]

for url in url_list:
    webbrowser.open_new_tab(url)"""

# Uninstalling Packages
# python -m pip uninstall numpy

"""
PS E:\GitHub\30daysOfPython> python -m pip list             
Package                 Version
----------------------- -----------
asttokens               3.0.1
attrs                   25.4.0
beautifulsoup4          4.14.3
certifi                 2026.2.25
...
typing_extensions       4.15.0
tzdata                  2025.3
urllib3                 2.6.3
wcwidth                 0.6.0
webdriver-manager       4.0.2
websocket-client        1.9.0
wsproto                 1.3.2
xlrd                    2.0.2
"""

# python -m pip show pandas
"""
Name: pandas
Version: 3.0.1
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author:
Author-email: The Pandas Development Team <pandas-dev@python.org>
License: BSD 3-Clause License

 Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
 All rights reserved.

 Copyright (c) 2011-2026, Open source contributors.
....
"""

# python -m pip show --verbose pandas for more details

# python -m pip freeze 
"""docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2"""
# suitable to use for requirements file

# Reading from URL
# python -m pip install requests


import requests # importing the request module
import re
"""url = 'https://www.ferit.unios.hr/studenti/raspored-nastave-i-ispita/2026-03-24/3-59#raspored'

response = requests.get(url) 
print(response)
print(response.status_code)
print(response.headers)    
print(response.text) # gives all the text from the page

url = 'https://restcountries.com/v3.1/all?fields=name,capital,region,population'  
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])

from mypackage import arithmetic

operation = arithmetic.subtract(2,5)
print(operation)

from mypackage import greet
greets = greet.greet_person('luka','marinkovic')
print(greets)
"""

# Exercises: Day 20
# 1
import requests
import re
url = 'https://www.gutenberg.org/cache/epub/1112/pg1112.txt'
response = requests.get(url)
print(response)
print(response.status_code)
text = response.text
clean_text = re.sub(r'[^A-Za-z0-9\s]', '', text)
clean_text_lower = clean_text.lower().split()

most_common_dict = {}
for word in clean_text_lower:
    counter = 0
    if word not in most_common_dict:
        most_common_dict[word] = 1
    else:
        most_common_dict[word] += 1
sorted_dict = sorted(most_common_dict.items(), key=lambda x:x[1], reverse=True)
print(sorted_dict[:10])

# 2
import statistics 
url = 'https://api.thecatapi.com/v1/breeds'  
response = requests.get(url)  
print(response) 
print(response.status_code)  
cats = response.json()
avg_list = []
for cat in cats:
    avg = 0
    s = cat['weight']['metric']      
    parts = s.split()
    numbers = []
    for p in parts:
        if p.replace('.', '', 1).isdigit():
            numbers.append(float(p))
    avg += (numbers[0]+numbers[1])/len(numbers)
    avg_list.append(avg)
print(min(avg_list))
print(max(avg_list))
print(statistics.mean(avg_list))
print(statistics.median(avg_list))
print(statistics.stdev(avg_list))

url = 'https://api.thecatapi.com/v1/breeds'  
response = requests.get(url)  
print(response) 
print(response.status_code)  
cats = response.json()
life_list = []
for cat in cats:
    avg = 0
    s = cat['life_span']  
    parts = s.split()
    numbers = []
    for p in parts:
        if p.replace('.', '', 1).isdigit():
            numbers.append(float(p))
    avg += (numbers[0]+numbers[1])/len(numbers)
    life_list.append(avg)
print(life_list)
print(min(life_list))
print(max(life_list))
print(statistics.mean(life_list))
print(statistics.median(life_list))
print(statistics.stdev(life_list))

url = 'https://api.thecatapi.com/v1/breeds'  
response = requests.get(url)  
print(response) 
print(response.status_code)  
cats = response.json()
breed_country = {}
for cat in cats:
    country = cat['origin']
    if country not in breed_country:
        breed_country[country] = 1
    else:
        breed_country[country] += 1
print(breed_country)

# 3
url = 'https://restcountries.com/v3.1/all?fields=name,population,area,languages'
response = requests.get(url)  
print(response) 
print(response.status_code)  
countries = response.json()
sorted_data = sorted(countries, key=lambda x:x['area'],reverse = True)
result = []
for country in sorted_data:
    result.append({
        'country': country['name']['official'],
        'area': country['area']
        })
print(result[:10])

url = 'https://restcountries.com/v3.1/all?fields=name,population,area,languages'
response = requests.get(url)  
print(response) 
print(response.status_code)  
countries = response.json()
lang_dict = {}
for country in countries:
    for lang in country['languages'].values():
        if lang not in lang_dict:
            lang_dict[lang] = 1
        else:
            lang_dict[lang] += 1
lang_dict = sorted(lang_dict.items(), key=lambda x:x[1], reverse=True)
print(lang_dict[:10])

total_languages = len(lang_dict)
print(total_languages)