# Python Programming Fundamentals

[ [Home](../README.md#6-python) ]

**A Beginner's Whitepaper**
*Zip Code Wilmington* v2

---

## About This Document <!-- omit from toc -->

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

This whitepaper introduces the fundamentals of Python for beginner programmers: how a Python program is written and run, the core data types and data structures, and the handful of ideas that shape how idiomatic Python code actually looks — indentation as syntax, an explicit `self`, comprehensions, and how variables refer to objects rather than holding them directly.

You don't need any prior programming experience to follow along, though some familiarity with general programming ideas (variables, loops) will help.

---

## Table of Contents <!-- omit from toc -->

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

- [Python Programming Fundamentals](#python-programming-fundamentals)
  - [1. Getting Started: Scripts, the REPL, and print()](#1-getting-started-scripts-the-repl-and-print)
  - [2. Importing Code: Modules and the Standard Library](#2-importing-code-modules-and-the-standard-library)
  - [3. Indentation Is Syntax](#3-indentation-is-syntax)
  - [4. Variables and Basic Data Types](#4-variables-and-basic-data-types)
  - [5. Control Flow: if/elif/else, while, and for](#5-control-flow-ifelifelse-while-and-for)
  - [6. Functions: def, Defaults, and \*args/\*\*kwargs](#6-functions-def-defaults-and-argskwargs)
  - [7. Data Structures: Lists, Tuples, Dicts, Sets, and Comprehensions](#7-data-structures-lists-tuples-dicts-sets-and-comprehensions)
  - [8. Classes and Objects](#8-classes-and-objects)
  - [9. References, Mutability, and Identity](#9-references-mutability-and-identity)
  - [10. Error Handling: try/except and EAFP](#10-error-handling-tryexcept-and-eafp)
  - [11. Key Takeaways](#11-key-takeaways)

---

## 1. Getting Started: Scripts, the REPL, and print()

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

```python
print("Hello, Zip Code!")
```

That's a complete, runnable Python program — no `main` function required. A Python file runs top to bottom, one statement at a time, the moment you execute it:

```bash
python hello.py
```

There's no separate compile step to think about (Python quietly byte-compiles things behind the scenes, but you'll rarely need to care). Python also gives you an interactive **REPL** — run `python` with no filename and you get a `>>>` prompt that evaluates one expression at a time and immediately shows the result:

```python
>>> 2 + 2
4
>>> print("hi")
hi
```

Because a Python file has no mandatory entry point, it's common to see this pattern once a script grows beyond a few lines:

```python
def main():
    print("Hello, Zip Code!")

if __name__ == "__main__":
    main()
```

`__name__` is a special variable Python sets automatically: it's `"__main__"` when a file is run directly, but it's set to the module's own name when that same file is *imported* by another file instead (Section 2). This idiom lets one file act as both a runnable script and an importable module, without its "script part" running by accident every time something else imports it.

---

## 2. Importing Code: Modules and the Standard Library

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

Any `.py` file is itself a **module**, and `import` is how you pull one into another:

```python
import math
from math import sqrt

print(math.sqrt(16))   # 4.0
print(sqrt(16))         # 4.0
```

Python ships with an enormous standard library — often summarized as "batteries included" — so a huge amount of common functionality never requires installing anything at all:

| Module | Purpose |
|---|---|
| `math` | Mathematical functions — `sqrt`, `floor`, `pi` |
| `os` | Interacting with the operating system and filesystem |
| `sys` | Command-line arguments and interpreter internals |
| `random` | Generating random numbers and choices |
| `datetime` | Working with dates and times |
| `json` | Reading and writing JSON data |

For code that isn't part of the standard library, `pip` (Python's package installer) downloads and installs third-party packages — `pip install requests`, for instance — which then become importable exactly like a standard-library module.

---

## 3. Indentation Is Syntax

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

This is the single most distinctive thing about Python, and it's worth sitting with directly: **indentation isn't a style preference — it's how the language marks where a block of code begins and ends.**

```python
if score >= 90:
    grade = "A"
else:
    grade = "B"
```

The colon `:` opens a new block, and every line indented at the same level underneath belongs to it; the moment the indentation decreases, the block is over. There's no separate closing symbol to match up — the indentation itself *is* the closing symbol.

> **Common mistake:** mixing tabs and spaces within the same block. Python can't always tell a tab and a handful of spaces apart, and inconsistent mixing produces a confusing `IndentationError` even when the code visually looks aligned in your editor. The standard convention (formalized in Python's style guide, PEP 8) is four spaces per indentation level, never tabs — most editors can be configured to insert spaces automatically when you press Tab.

---

## 4. Variables and Basic Data Types

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

Python is **dynamically typed** — a variable isn't declared with a type up front, and can be reassigned to a value of a different type later. A Python variable is really a name bound to an object, not a labeled box that a value sits inside — the name can be pointed at any kind of object at any time.

Python is also **strongly typed**, meaning it won't silently convert between unrelated types: `"5" + 5` raises an error rather than guessing what you meant.

```python
age = 34          # int
gpa = 3.9         # float
name = "Ada"      # str
enrolled = True   # bool
advisor = None    # None -- Python's "no value" singleton
```

`type(age)` tells you a value's current type, and `isinstance(age, int)` checks against one. For building output, the idiomatic tool is an **f-string** — a string literal prefixed with `f`, with `{ }` placeholders evaluated and inserted directly:

```python
print(f"{name} is {age} years old")   # "Ada is 34 years old"
```

`None` is Python's single, explicit way of representing "no value" — its own distinct value and type (`NoneType`), used constantly as a default or placeholder when there's genuinely nothing to store yet.

---

## 5. Control Flow: if/elif/else, while, and for

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

`if` checks a condition and runs its block only when that condition is true. `elif` ("else if") checks another condition only if the ones above it were false, and a final `else` catches everything else. Only one branch ever runs.

`while` behaves as you'd expect — it repeats as long as its condition stays true:

```python
count = 0
while count < 5:
    count += 1
```

Python's `for` loop is a **for-each**: it always walks through the elements of something iterable — a list, a string, a range of numbers — rather than managing a counter variable directly.

```python
for name in ["Ada", "Grace", "Alan"]:
    print(name)

for i in range(5):     # 0, 1, 2, 3, 4
    print(i)
```

`range(5)` produces a sequence of numbers, and `for` iterates over it exactly the way it iterates over the list of names above — `range()` is how you get counting behavior out of a loop that is, underneath, always a for-each.

`break` exits a loop immediately, and `continue` skips the rest of the current iteration and moves on to the next one.

---

## 6. Functions: def, Defaults, and *args/**kwargs

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ada")                 # "Hello, Ada!"
greet("Ada", greeting="Hi")  # "Hi, Ada!"
```

`def` defines a function. Parameters can have **default values** (`greeting="Hello"`), making them optional at the call site, and any parameter can be passed by name (`greeting="Hi"`) instead of by position.

For a function that should accept *any* number of arguments, `*args` and `**kwargs` are the standard pattern:

```python
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)   # 6
```

`*numbers` collects any number of positional arguments into a tuple (Section 7); `**kwargs`, by the same idea, collects extra *keyword* arguments into a dictionary. A string written directly below `def` as the function's first line becomes its **docstring** — accessible later via `help()` — the idiomatic way to document what a function does.

---

## 7. Data Structures: Lists, Tuples, Dicts, Sets, and Comprehensions

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

| Structure | Example | Mutable? | Notes |
|---|---|---|---|
| **list** | `["Python", "C", "Go"]` | Yes | Ordered, general-purpose collection |
| **tuple** | `(3, 4)` | No | Ordered, but fixed once created |
| **dict** | `{"Ada": 22, "Grace": 25}` | Yes | Key/value pairs |
| **set** | `{1, 2, 2, 3}` → `{1, 2, 3}` | Yes | Unique elements, no order |

A **list comprehension** is Python's idiomatic way to build a new list from an existing sequence in one expression, instead of writing out a separate loop:

```python
squares = [n * n for n in range(5)]          # [0, 1, 4, 9, 16]
evens = [n for n in range(10) if n % 2 == 0] # [0, 2, 4, 6, 8]
```

Read the first one as "`n * n`, for every `n` in `range(5)`," and the second as the same idea with a filter added: "only when `n % 2 == 0` is true." A comprehension replaces the pattern of creating an empty list, looping, and appending one item at a time, with a single, self-contained expression that says directly what the resulting list should contain.

---

## 8. Classes and Objects

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi, I'm {self.name}"

ada = Student("Ada", 22)
print(ada.greeting())   # "Hi, I'm Ada"
```

`class` defines a new type; `__init__` is the constructor, called automatically when you write `Student("Ada", 22)`. The detail most worth noticing: **every method explicitly takes `self` as its first parameter** — the instance the method was called on. `self` is simply the object itself, passed in automatically whenever you call a method with dot syntax, which is exactly why `ada.greeting()` and `Student.greeting(ada)` do the same thing.

Attributes set on `self` inside `__init__` (`self.name`, `self.age`) belong to that specific instance — a different `Student` object has its own separate `name` and `age`. Python also supports a family of special "dunder" (double-underscore) methods — `__str__`, for instance, controls what `print(ada)` actually shows — worth knowing exists, even before you need to reach for one yourself.

---

## 9. References, Mutability, and Identity

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

This is worth slowing down on, because it explains a lot of behavior that otherwise looks like a mistake: **a Python variable is a name bound to an object, not a box that directly holds a value.** Assigning one variable to another doesn't copy anything — it just gives a second name to the *same* object.

```python
a = [1, 2, 3]
b = a              # b refers to the same list object as a
b.append(4)
print(a)           # [1, 2, 3, 4] -- changed too!
```

Whether this matters depends entirely on whether the object is **mutable**. Lists, dictionaries, and sets can be changed in place; numbers, strings, and tuples cannot — any operation that looks like it "changes" one of those actually builds a brand-new object and rebinds the name to it:

| Action | What actually happens | Who sees it |
|---|---|---|
| `b.append(4)` | Mutates the shared list object itself | Every name referring to that object |
| `y = y + [4]` | Builds a new list, then rebinds `y` to it | Only `y` — the original object is untouched |

The same rule explains a classic beginner surprise with function arguments: passing a mutable object into a function hands the function a reference to your *actual* object, not a private copy.

```python
def add_item(lst):
    lst.append("new")

cart = ["apple"]
add_item(cart)
print(cart)   # ["apple", "new"] -- the function changed the caller's list
```

Python gives you two different comparison operators: `==` asks whether two objects have the same *contents*, while `is` asks whether they're *literally the same object*.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b   # True  -- same contents
a is b   # False -- two separate objects
a is c   # True  -- c is literally the same object as a
```

> **Common mistake:** using `is` where `==` was meant — `is` should be reserved for checking against singletons like `None` (`x is None`), not for comparing ordinary values. A second, genuinely famous Python trap: a **mutable default argument**. `def add(item, items=[])` creates that empty list *once*, when the function is defined — not fresh on every call — so every call that doesn't supply its own list ends up silently sharing (and appending to) the exact same one.

---

## 10. Error Handling: try/except and EAFP

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(result)
finally:
    print("Done")
```

`try` runs the code that might fail; `except` catches a specific kind of error if one occurs; `else` runs only when *no* exception was raised; `finally` always runs, whether or not one was. You can `raise` your own exceptions the same way built-in ones are raised.

Python's idiomatic attitude toward errors is often summarized as **EAFP** — "**E**asier to **A**sk **F**orgiveness than **P**ermission." Rather than checking every precondition before acting (`if key in dictionary: ...`), idiomatic Python often just attempts the operation and catches the exception if it fails:

```python
try:
    value = my_dict["missing_key"]
except KeyError:
    value = "default"
```

The idea behind EAFP is that the exceptional case (the key being missing) is handled only when it actually happens, rather than guarded against up front on every single attempt — which keeps the common, successful path free of extra checks.

---

## 11. Key Takeaways

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]

- **Indentation is syntax**, not a style choice — it's how Python marks the start and end of every block.
- **Dynamic but strong typing**: variables carry no declared type and can be reassigned freely, but Python still refuses to silently mix unrelated types.
- **`for` is a for-each**, not a counter — `range()` is how you get counting behavior, not a separate kind of loop.
- **List comprehensions** are Python's idiomatic way to transform (and optionally filter) a sequence in one expression.
- **`self` is explicit** in every method — it's simply the instance the method was called on, passed in automatically.
- **Variables are references, not copies** — assigning one name to another shares the same object, and mutable objects (lists, dicts, sets) can be changed through *any* name that refers to them, while immutable ones (numbers, strings, tuples) can only ever be replaced.
- **`is` checks identity, `==` checks equality** — they answer different questions, and mixing them up is a common source of bugs.
- **EAFP**: idiomatic Python often tries an operation and handles the exception if it fails, rather than checking every precondition first.

---

*Zip Code Wilmington — Python Programming Fundamentals*

[ [Top](#python-programming-fundamentals) | [Home](../README.md#6-python) ]
