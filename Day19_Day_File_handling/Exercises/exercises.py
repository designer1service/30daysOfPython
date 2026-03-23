# Exercises: Day 19
import json
# Exercises: Level 1

# 1
def read_line(path):
    with open(path) as f:
        counter = 0
        for line in f:
            if not line.isspace():
                counter += 1
    return counter

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
    new_dict = {}
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
