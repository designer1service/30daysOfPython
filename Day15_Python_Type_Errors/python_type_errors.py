# Day 15 — Python Type & Runtime Errors
# Author: Luka Marinkovic
#
# REPL session – examples of common errors and fixes
#
# >>> print hello world
#   File "<stdin>", line 1
#     print hello world
#     ^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
#
# >>> print(age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     print(age)
#           ^^^
# NameError: name 'age' is not defined
#
# >>> age = 25
# >>> print(age)
# 25
#
# >>> numbers = [1, 2, 3, 4, 5]
# >>> numbers[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     numbers[5]
#     ~~~~~~~^^^
# IndexError: list index out of range
#
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import maths
# ModuleNotFoundError: No module named 'maths'
#
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     math.PI
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
#
# >>> math.pi
# 3.141592653589793
#
# >>> users = {'name': 'Asab', 'age': 250, 'country': 'Finland'}
# >>> users['name']
# 'Asab'
#
# >>> user['country']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     user['country']
#     ^^^^
# NameError: name 'user' is not defined. Did you mean: 'users'?
#
# >>> users['country']
# 'Finland'
#
# >>> 4 + '3'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     4 + '3'
#     ~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
# >>> 4 + int('3')
# 7
#
# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     from math import power
# ImportError: cannot import name 'power' from 'math'
#
# >>> from math import pow
# >>> pow(2, 3)
# 8.0
#
# >>> int('12a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     int('12a')
#     ~~~^^^^^^^
# ValueError: invalid literal for int() with base 10: '12a'
#
# >>> 1 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     1/0
#     ~^~
# ZeroDivisionError: division by zero
