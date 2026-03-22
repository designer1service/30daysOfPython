# Regular Expressions or RegEx

import re

txt = 'I love to learn python'

# match returns a match on the start of the string
match = re.match('i love to learn',txt,re.I)
print(match)

span = match.span()
print(span)

start,end = span
substring = txt[start:end]
print(substring)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# search returns the first match 
match = re.search('first',txt,re.I)
print(match)

span = match.span()
print(span)

start, end = span
substring = txt[start:end]
print(substring)

# findall returns all matches of substring
matches = re.findall('language', txt, re.I)
print(matches)

matches = re.findall('python', txt, re.I)
print(matches)

matches = re.findall('Python|python',txt)
matches = re.findall('[Pp]ython',txt)
print(matches)

# Replacing a Substring

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('python|Python','Java',txt,re.I)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

match_fix = re.sub('%','',txt)
print(match_fix)

# Splitting Text Using RegEx Split
# returns a list of strings split by a given substring
print(re.split('\n',match_fix))

# Writing RegEx Patterns
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '

regex_pattern = r'apple'
matches = re.findall(regex_pattern,txt,re.I)
print(matches)

regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern,txt)
print(matches)

# Square Bracket
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '

regex_pattern = r'[Aa]pple|[Bb]anana'
matches = re.findall(regex_pattern,txt)
print(matches)

# Escape character(\) in RegEx
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'

regex_pattern = r'\d'
matches = re.findall(regex_pattern,txt)
print(matches)

# One or more times(+)
regex_pattern = r'\d+'
matches = re.findall(regex_pattern,txt)
print(matches)

# Period(.)
txt = '''Apple and banana are fruits'''

regex_pattern = r'[Aa].'
matches = re.findall(regex_pattern,txt)
print(matches)

# Zero or more times(*)
# matches zero or more occurrences of the preceding pattern (e.g., any string starting with 'a')
regex_pattern = r'[a].*'
matches = re.findall(regex_pattern, txt)
print(matches) 

# Zero or one time(?)
# matches zero or one occurrence (makes the '-' optional in 'e-mail' vs 'email')
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches) 

# Quantifier in RegEx
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern,txt)
print(matches)

# Cart ^
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)

# Exercises: Level 1
# 1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph.lower())
paragraph_dict = {}
for word in words:
    paragraph_dict[word] = paragraph_dict.get(word, 0) + 1
result = sorted([(count, word) for word, count in paragraph_dict.items()], reverse=True)
print(result)

# 2
txt = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 
in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
Extract these numbers from this whole text and find the distance between the 
two furthest particles."""

regex_pattern = r'-?\d+'
matches = re.findall(regex_pattern,txt)
matches_list = list(map(int,matches))
print(max(matches_list) - min(matches_list))

# Exercises: Level 2
def is_valid_variable(name):
    regex_pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    match = re.match(regex_pattern,name)
    if match:
        return True
    return False

print(is_valid_variable('firstname'))

# Exercises: Level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_text = re.sub(r'[^A-Za-z0-9\s]', '', sentence)
new_dict = {}
words = re.findall(r'\b\w+\b', clean_text.lower())
for word in words:
    new_dict[word] = new_dict.get(word,0) + 1
result = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
print(result[:3])