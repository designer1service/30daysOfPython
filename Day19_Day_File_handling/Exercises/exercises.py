# Exercises: Day 19
import json
import os
import string
import re
# Exercises: Level 1

# 1
def read_line(path):

    with open(path) as f:
        counter = 0
        word_count = 0
        for line in f:
            if not line.isspace():
                counter += 1
            word_in_line = line.split()
            word_count += len(word_in_line)
    return counter, word_count

print(read_line("Day19_Day_File_handling\Exercises\michelle_obama_speech.txt"))

# 2
def most_spoken_languages(path,count):
    new_dict = {}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        for country in data:
            for lang in country['languages']:
                if lang not in new_dict:
                    new_dict[lang] = 1
                else:
                    new_dict[lang] += 1
    pairs = [(count, lang) for lang, count in new_dict.items()]
    pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
    return pairs[:count]

print(most_spoken_languages(path ="Day19_Day_File_handling\\Exercises\\countries_data.json",count = 10))

# 3
def most_populated_countries(path,count):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        sorted_data = sorted(data, key=lambda x:x['population'],reverse = True)
        top = sorted_data[:count]

        result = []
        for country in top:
            result.append({
                'country': country['name'],
                'population': country['population']
            })
        return result

print(most_populated_countries(path ="Day19_Day_File_handling\\Exercises\\countries_data.json",count = 10))

# Exercises: Level 2

# 1
with open("Day19_Day_File_handling\Exercises\email_exchanges_big.txt") as f:
    txt = f.readlines()
    new_list = []
    for line in txt:
        if line.startswith('To:'):
            new_list.append(line.removeprefix('To: ').removesuffix('\n'))
    set_mail = set(new_list)
    print(set_mail)

# 2 
def find_most_common_words(text_or_path, count):
    if os.path.exists(text_or_path):
        with open(text_or_path, encoding="utf-8") as f:
            text = f.read()
    else:
        text = text_or_path
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, " ")
    words = text.split()
    freq = {}
    for w in words:
        if w not in freq:
            freq[w] = 1
        else:
            freq[w] += 1
    pairs = [(cnt, word) for word, cnt in freq.items()]
    pairs.sort(key=lambda x: x[0], reverse=True)

    return pairs[:count]

# 3
print(find_most_common_words("Day19_Day_File_handling/Exercises/obama_speech.txt", 10))
print(find_most_common_words("Day19_Day_File_handling/Exercises/michelle_obama_speech.txt", 10))
# others are the same

# 4
from stop_words import stop_words
def clean_text(text):
    clean_text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    clean_text_lower = clean_text.lower()
    return clean_text_lower

def remove_support_words(text):
    new_text = clean_text(text).split()
    for text in new_text[::-1]:
        if text not in stop_words:
            continue
        else:
            new_text.remove(text)
    return new_text
            

def check_text_similarity(text1,text2):
    newtext1 = set(remove_support_words(text1))
    newtext2 = set(remove_support_words(text2))

    similarity = len(newtext1 & newtext2)/len(newtext1|newtext2)
    return similarity*100

# 5 
print(find_most_common_words("Day19_Day_File_handling/Exercises/romeo_and_juliet.txt", 10))

# 6 
import csv
with open('Day19_Day_File_handling/Exercises/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    javascript_count = 0
    java_count = 0
    for row in csv_reader:
        line = ''.join(row)
        if 'javascript' in line.lower():
            javascript_count += 1
        elif 'java' in line.lower():
            java_count += 1
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            line_count += 1
    print(f'Number of lines:  {line_count}')
    print(java_count)
    print(javascript_count)

