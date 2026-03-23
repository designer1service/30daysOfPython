# File Handling

# open('filename', mode)  # mode (r, a, w, x, t, b)


"""
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

# Opening a text file
f = open('Day19_Day_File_handling\\file.txt')
print(f)

# Read the whole file content as one string
txt = f.read()
print(type(txt))
print(txt)

# Move the file pointer back to the beginning
f.seek(0)
# Read only the first 11 characters
txt = f.read(11)
print(txt)

f.close()

# Read only the first line
f = open('Day19_Day_File_handling\\file.txt')
line = f.readline()
print(line)
f.close()

# Read all lines into a list
f = open('Day19_Day_File_handling\\file.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# Another way to get all lines as a list (using splitlines)
f = open('Day19_Day_File_handling\\file.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# Using context manager – file is closed automatically
with open('Day19_Day_File_handling\\file.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# Opening files for writing and updating
# Append text at the end of the file
with open('Day19_Day_File_handling/file.txt', 'a') as f:
    f.write('VAZI')

# Create a new file (or overwrite if it exists) and write text
with open('Day19_Day_File_handling/writing_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file')

# Deleting files
import os
if os.path.exists('Day19_Day_File_handling/writing_file_example.txt'):
    os.remove('Day19_Day_File_handling/writing_file_example.txt')
else:
    print('The file does not exist')

# File Types
# JSON EXTENSION - actually a Python dict when loaded

import json

# 1) Create an empty JSON file (a list) – run once to initialize the file
with open('Day19_Day_File_handling/file.json', 'w', encoding='utf-8') as f:
    json.dump([], f, ensure_ascii=False, indent=4)

# 2) JSON string -> dict (Changing JSON to Dictionary)
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# 3) Dict -> JSON string (Changing Dictionary to JSON)
person1 = {
    "name": "Luka",
    "country": "Croatia",
    "city": "Unknown",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json = json.dumps(person1, indent=4)
print(type(person_json))
print(person_json)

# 4) Load the existing JSON file (a list of people)
with open('Day19_Day_File_handling/file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)      # we expect a list, e.g. []

print(data)

# 5) Append both people (from JSON string and from dict) to the list
data.append(person_dct)
data.append(person1)

# 6) Save the whole list back to the JSON file (Saving as JSON File)
with open('Day19_Day_File_handling/file.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

"""
json.dump()  - writes a Python object directly to a .json file
json.dumps() - converts a Python object (dict, list, ...) to a JSON string
"""

# File with csv Extension
import csv
with open('Day19_Day_File_handling/file.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} is a teacher. He lives in {row[1]}, {row[2]}.')
            line_count += 1
        print(f'Number of lines:  {line_count}')

# File with xlsx Extension
"""import xlrd
excel_book = xlrd.open_workbook('Day19_Day_File_handling/sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)"""
# Bad explenation will get back to this


import xml.etree.ElementTree as ET
tree = ET.parse('Day19_Day_File_handling/sample.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)


