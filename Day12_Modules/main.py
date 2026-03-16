# Modules

# Importing a Module
import mymodule as mod
print(mod.generate_fullname('luka','marinkovic'))

# Import Functions from a Module
from mymodule import generate_full_name, sum_two_nums, person, gravity # functions don't exist
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])

# Import Functions from a Module and Renaming
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g # same as import mymodule as mod
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

# Import Built-in Modules

# OS Module
import os

os.mkdir('directory_name')
os.chdir('path')
os.getcwd()
os.rmdir()


# Sys Module

import sys
print(sys.argv[0], sys.argv[1], sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

print("Max size:", sys.maxsize)
print("Python version:", sys.version)

sys.exit()

print("Ovo se neće pokrenuti")


# Statistics Module
from statistics import * # all modules 
import statistics as stat # naming it

ages = [20,20,24,24,25,22,26,20,23,22,26]
print(stat.median(ages))
print(median(ages))

print(median(ages))
print(stat.mode(ages))
print(stdev(ages))

# Math Module
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

from math import pi as  PI
print(PI) # 3.141592653589793

# String module
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Random Module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive


# Exercises: Level 1

# 1 
import random
import string 
def random_user_id():
    first_input = int(input('Enter number 1: '))
    second_input = int(input('Enter number 2: '))
    id_list = []
    counter = 0

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_char = letters + digits + symbols
    while counter < first_input:
        random_string = ''.join(random.choice(all_char) for _ in range(second_input))
        id_list.append(random_string)
        counter +=1
    return id_list

ids = random_user_id()
for id in ids:
    print(id)

# 3

def rgb_color_gen():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    generator = f'rgb({red},{green},{blue})'
    return generator

print(rgb_color_gen())

# Exercises: Level 2

def list_of_rgb_colors(number):
    rgb_list = []
    for _ in range(number):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        generator = f'rgb({red},{green},{blue})'
        rgb_list.append(generator)
    return rgb_list

def list_of_hexa_colors(number):
    hexa_list = []
    for _ in range(number):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        hexa_list.append(f'#{r:02x}{g:02x}{b:02x}')
    return hexa_list

def generate_colors(name,number):
    if name.lower() == 'rgb':
        print(list_of_rgb_colors(number))
    elif name.lower() == 'hexa':
        print(list_of_hexa_colors(number))
    else:
        print('wrong name haha run again')


generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

# Exercises: Level 3
ordered_list = [1,2,3,4,5,6,8,8]

def shuffle_list(item_list):
    random.shuffle(item_list)
    return item_list

print(shuffle_list(ordered_list))

def unique_list():
    uniq_list = []
    while len(uniq_list) < 7:
        num = random.randint(0,9)
        if num not in uniq_list:
            uniq_list.append(num)
    return uniq_list

print(unique_list())