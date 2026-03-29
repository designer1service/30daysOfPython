import pandas as pd 
import numpy  as np 

# Creating Pandas Series with custom index
nums = [1, 2, 3, 4,5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# Creating Pandas Series from a Dictionary
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)

# Creating a Pandas Series Using Linspace
s = pd.Series(np.linspace(5, 20, 10))
print(s)

# Creating DataFrames from List of Lists
data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# Creating DataFrame Using Dictionary
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)


path = 'Day25_Pandas/'
df = pd.read_csv(path + 'weight-height.csv')
print(df.head())
print(df.tail())
print(df.columns)

heights = df['Height']
print(heights)

print(heights.describe())
print(df.describe())

# Creating a DataFrame
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

# Adding a New Column
weights = [74, 78, 69]
df['Weight'] = weights
print(df)

heights = [173, 175, 169]
df['Height'] = heights
print(df)

# Modifying column values
df['Height'] = df['Height'] * 0.01
print(df)

def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()
df['BMI'] = bmi
print(df)

# Formatting DataFrame columns
df['BMI'] = round(df['BMI'], 1)
print(df)

birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year


# Checking data types of Column values
print(df.Weight.dtype)
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype)
df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype)
ages = df['Current Year'] - df['Birth Year']
print(ages)

df['Ages'] = ages
print(df)


# Exercises: Day 25

# Read the hacker_news.csv file from data directory
path = 'Day25_Pandas/'
df = pd.read_csv(path + 'hacker_news.csv')

# 2
print(df.head())

# 3
print(df.tail())

# 4
title = df.columns
s = pd.Series(title)
print(s)

# 5
rows, cols = df.shape
print("Number of rows:", rows)
print("Number of columns:", cols)

python_titles = df[df['title'].str.contains('python', case=False, na=False)]
print(python_titles)

js_titles = df[df['title'].str.contains('javascript', case=False, na=False)]
print(js_titles)

print(df.head())     
print(df.info())      
print(df.describe()) 