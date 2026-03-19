Day 15 — Python Type & Runtime Errors  

> **Today’s Focus:** Explore common Python errors (syntax, name, index, import, attribute, type, value, zero division) and learn how to interpret and fix their messages.  
> **Author:** Luka Marinkovic  

## What I learned  

I experimented directly in the Python REPL to trigger different kinds of errors and read their messages. I saw how Python points to the exact line and position of a problem and usually explains what went wrong and often suggests a fix. This made me more comfortable with errors instead of being afraid of them.  

## Syntax and indentation issues  

I triggered a `SyntaxError` by writing `print hello world` without parentheses and learned that Python now even suggests using `print(...)`. I also caused `IndentationError` by accidentally starting a line with a space before `import`, which showed that stray indentation can break otherwise valid code. These examples taught me to watch both syntax and indentation carefully.  

## Name, index, import, and attribute errors  

I saw a `NameError` when using a variable (`age`, `user`) before defining it or using a wrong variable name. I got an `IndexError` by accessing `numbers[5]` when the list only had indices 0–4, reminding me to stay inside bounds. I triggered `ModuleNotFoundError` by trying to import a non‑existent module `maths` and `ImportError` when importing `power` from `math` instead of the correct `pow`. I also caused an `AttributeError` by calling `math.PI` instead of `math.pi`, which emphasized that attribute names are case‑sensitive.  

## Type, value, and zero-division errors  

I produced a `TypeError` by adding an integer and a string (`4 + '3'`) and then fixed it by converting the string to an integer with `int('3')`. I triggered a `ValueError` when trying to convert `'12a'` to an integer because it contains non‑digit characters. Finally, I saw a `ZeroDivisionError` by computing `1/0`, which confirmed that Python does not allow division by zero. Together, these examples helped me connect specific error types with the underlying logical mistakes in the code.  

