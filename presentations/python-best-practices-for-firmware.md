---
title: "Python Best Practices (for firmware)"
author: John Prince (platform)
patat:
  pandocExtensions:
    - patat_extensions
    - autolink_bare_uris
    - emoji
# use patat for presentation
# yay -S patat-bin
# patat -w <presentation>
# consider https://github.com/vinayak-mehta/present in future
---

# Overview

Python best practices with a focus on firmware scripting

* ecosystem
* style and formatting
* stdlib tools you could/should be using

# Why Best Practices

Because *reasons*.

Widespread adoption can be viewed as a *reason*:

    "drafting coefficient"

# Not set in stone

Best practices are relative to your context and always evolving. For example:

* docker environment vs. local user environment
* new dict merge syntax superior to previous (newdict = dict1 | dict2)
* my presentation breaks some best practices

# Python2 is dead, long live Python3

Python2 is *dead*

* Last maintenance release was supposed to be 2015, extended to April 2020
* Arch has used python3 as default system python for > 10 years
* If a library has not been migrated to python 3 at this point, who is using
  and maintaining it?

Python 3 is better (e.g., internal unicode)

# Most popular python IDEs in 2020

* Visual Studio Code (*vscodium*)
* Pycharm
* Spyder (especially data science)
* Eclipse

Lightweight:

* Vim (or *Neovim*)
* Sublime Text

# Choosing your tools

- python is fairly hands-off with ecosystem tools
- best practices includes choosing good ecosystem tools

# Pyenv: handle python versions

```bash
pyenv global          # -> system
pyenv install 3.8.5

# set your global/default
pyenv global 3.8.5
pyenv global          # ->  3.8.5
```

# Virtualenv: isolated environments

pyenv virtualenv plugin

```bash
# inside my-project
pyenv virtualenv 3.8.5 my-project-3.8.5
pyenv local my-project-3.8.5
```

# Dependency management (dep mgmt)

* Good: requirements.txt
* Best: **deterministic** dependency mgmt (e.g., Poetry)

# Good dependency mgmt: requirements.txt

**Good**
```text
----------------
requirements.txt
----------------
arrow
requests
```

**Better**
```text
----------------
requirements.txt
----------------
arrow>=0.16,<=1.0
requests==2.24.0
```

# Best dependency mgmt: Poetry

**Best**
```
poetry new my-project
```

```
poetry add arrow
poetry add --dev ipython flake8 pytest
```

# Formatting and style tools

Recommended:

* flake8 - fast linter
* pylint - deep linter
* black - opinionated formatter
* isort - sorts and formats your imports

Enforce many best practices!

**Can be integrated into your editor or IDE.**

# Avoid one-letter variables

* longer variables are easier to read
* pylint will not yell at you
* it's not much more work (autocomplete!)
* one-letter vars don't search and replace well

Bad
```python
for x in range(15):
    x += 1
    ...
```

Good
```python
for value in range(15):
    value += 1
    ...
```

# Enumerate instead of counters

*Using a counter*
```python
cnt = 0
for value in range(10):
    ...
    cnt += 1
```

*Using enumerate*
```python
for cnt, value in enumerate(range(10)):
    print(f"{cnt}: {value}")
```

# List comprehensions instead of loops

*Lots of code starts like this:*
```python
odds_squared = []
for val in [1, 2, 3, 4, 5]:
    if not val % 2:
        calculation = val**2
        odds_squared.append(calculation)
```

*Use a list comprehension instead:*
```python
odds_squared = [val**2 for val in [1, 2, 3, 4, 5] if not val % 2]
```

# List comprehensions instead of filter/map

*Ruby*
```ruby
[1, 2, 3].select {|val| val < 3}.map {|val| val.to_s }
[1, 2, 3].select {|val| val < 3}.map(&:to_s)
```

*Python*
```python
# example with filter and map
list(
    map(str, filter(lambda val: val < 3, [1, 2, 3]))
)

# instead, prefer list comprehension
[str(val) for val in [1, 2, 3] if val < 3]
```

# Dict comprehensions


*A dict comprehension:*
```python
val_to_str_val = {val: str(val) for val in [1, 2, 3]}
    # --> {1: '1', 2: '2', 3: '3'}
```

*Which is equivalent to:*
```python
val_to_str_val = dict((val, str(val)) for val in [1, 2, 3])
# --> {1: '1', 2: '2', 3: '3'}
```

# Set comprehensions

*A set comprehension:*
```python
my_vals = {str(val) for val in [1, 2, 3, 3, 9, 2]}
```

*Which is equivalent to:*
```python
my_vals = set([str(val) for val in [1, 2, 3, 3, 9, 2]])
```

# f-strings FTW

*old school '%' formatting:*
```python
for cnt, value in enumerate([1,2,3,4,5]):

    # oldschool
    print("The %d value is %s" % (cnt, value))

    # format is sometimes handy
    print("The {} value is {}".format(cnt, value))

    # F-strings are easier to read (python 3.6+)
    print(f"The {cnt} value is {value}")
```

# Typing

Many new stdlib and external libraries rely on typing (here to stay).

*Simple example:*
```python
def is_adult(self, country: str, age: int) -> bool:
    ...
```

*More complex example:*
```python
from typing import Dict, Optional

def make_mapping(input: Optional[list] = None) -> Dict[str, int]:
    ...
```

# Use the standard library

* Less code
* Self-documenting code
* Performant
* Robust
* Zero maintenance

# Stdlib highlights

* itertools
* collections
* dataclasses
* pathlib

# itertools: infinite

**Infinite**
```python
import itertools

itertools.count(10)          # --> 10 11 12 13 14 ...

itertools.cycle('ABCD')      # --> A B C D A B C D ...

itertools.repeat(10, 3)      # --> 10 10 10
```

# itertools: accumulation

**Accumulation**
```python
from functools import reduce

reduce(lambda accum, value: accum + value, [1,2,3,4,5])      # --> 15

sum([1,2,3,4,5])                                             # --> 15

# leaves droppings
import itertools

itertools.accumulate([1,2,3,4,5])                   # --> 1 3 6 10 15
```

# itertools: chaining

```python
from itertools import chain

chain('ABC', 'DEF')                 # --> A B C D E F

# often more useful programmatically
chain.from_iterable(['ABC', 'DEF']) # --> A B C D E F
```

# itertools: take/drop while

```python
from itertools import dropwhile, takewhile

takewhile(lambda x: x<5, [1,4,6,4,1]) # --> 1 4

dropwhile(lambda x: x<5, [1,4,6,4,1]) # --> 6 4 1
```

# itertools: others

```
starmap            # for mapping with splatting arguments

tee                # split an iterable
zip (builtin)      # join iterables
zip_longest

product            # cartesian product
permutations
combinations
combinations_with_replacement
```

# collections

Most useful:

* Counter
* defaultdict
* ChainMap

# collections.Counter

* counts anything iterable
* addition, subtraction, union, intersection

```python
import collections

some_colors = ['blue', 'blue', 'green', 'red', 'blue', 'red']
more_colors = ['sapphire', 'blue', 'red']

some_color_counts = collections.Counter(some_colors)
# -> Counter({'blue': 3, 'green': 1, 'red': 2})

more_color_counts = collections.Counter(more_colors)

all_counts = some_color_counts + more_color_counts
# -> Counter({'blue': 4, 'green': 1, 'red': 3, 'sapphire': 1})
```

# collections.defaultdict

```python
import collections

name_to_breed = {
    "fido": "labrador", "scooby doo": "great dane",
    "balto": "huskie", "fritz": "huskie",
}

breed_to_name = collections.defaultdict(list)
for name, breed in name_to_breed.items():
    breed_to_name[breed].append(name)

breed_to_name  # -> {..., 'huskie': ['balto', 'fritz']}
```

# dataclasses

Data-centric classes

```python
from dataclasses import dataclass

@dataclass
class Rectangle:
    height: int = 0
    width: int = 0


rect = Rectangle(10, 5)
rect.height
rect.height = 12
```

# dataclasses: frozen

use *frozen=true* to get tuple or named-tuple like behavior:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Rectangle:
    height: int = 0
    width: int = 0

rectangles = [
    Rectangle(10, 4),
    Rectangle(4, 4),
    Rectangle(10, 4),
    ...
]

unique_rectangles = set(rectangles)

rectangle_to_name = {
    Rectangle(10, 4): "tall",
    Rectangle(3, 15): "wide",
}
```

# pathlib

```python
import os

os.path.isfile(os.path.join(os.path.expanduser('~'), 'somefile.txt'))
```

```python
import pathlib

(pathlib.Path.home() / 'somefile.txt').is_file()
```

# argparse with pathlib

```python
import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("path", type=pathlib.Path)
args = parser.parse_args()

print("reading:", args.path.resolve())
zeroed_lines = [line.replace("o", "0") for line in args.path.open()]

file_in_home = pathlib.Path.home() / (args.path.name + ".zeroed")

print("writing:", file_in_home.resolve())
file_in_home.write_text("".join(zeroed_lines))
```
