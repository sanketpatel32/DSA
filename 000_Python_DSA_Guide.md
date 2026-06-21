# 000 — Essential Modern Python Guide for DSA

A focused reference for solving Data Structures & Algorithms problems in **modern Python (3.10+)**.
Read it once, bookmark it, and come back as you work through the 236 problems in this folder.

> **Goal:** the 80% of Python you use in 80% of LeetCode-style problems.
> Nothing esoteric — just the idioms that make solutions short, fast, and correct.

---

## Table of Contents

1. [Environment & Style](#1-environment--style)
2. [Core Syntax That Pays Off](#2-core-syntax-that-pays-off)
3. [Built-in Data Structures (the big four)](#3-built-in-data-structures-the-big-four)
4. [The `collections` Module](#4-the-collections-module)
5. [Heap / Priority Queue — `heapq`](#5-heap--priority-queue--heapq)
6. [Bisect — Binary Search on Sorted Sequences](#6-bisect--binary-search-on-sorted-sequences)
7. [Sorting & Custom Keys](#7-sorting--custom-keys)
8. [Itertools — Combinatorics & More](#8-itertools--combinatorics--more)
9. [Functions: `*args`, `**kwargs`, Lambdas, `partial`](#9-functions-args-kwargs-lambdas-partial)
10. [Strings & `str` Methods](#10-strings--str-methods)
11. [Math, `math`, and Number Theory](#11-math-math-and-number-theory)
12. [Bit Manipulation](#12-bit-manipulation)
13. [Common Patterns Cheatsheet](#13-common-patterns-cheatsheet)
14. [Big-O Reference Table](#14-big-o-reference-table)
15. [Common Pitfalls & Bugs](#15-common-pitfalls--bugs)
16. [Testing & Running Snippets](#16-testing--running-snippets)
17. [Python vs Other Languages](#17-python-vs-other-languages)
18. [Quick One-Liners](#18-quick-one-liners)

---

## 1. Environment & Style

### Versions
- Use **Python 3.10+**. Many LeetCode-style idioms (match-case, `int.bit_count()`, better error
  messages) require 3.10+.
- Avoid Python 2 patterns: `print` is a function, `range()` is lazy, no `xrange`, integer division
  is `//`.

### Recommended setup
```bash
# Create a virtual env in the DSA folder
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate

pip install pytest ipython
```

### Style conventions for DSA
- **Snake_case** for functions and variables: `def two_sum(nums, target):`
- **UPPER_CASE** for constants: `MOD = 10**9 + 7`
- **Type hints** are optional but helpful for graph/node code:
  ```python
  def binary_search(arr: list[int], target: int) -> int:
      ...
  ```
- Keep functions **pure** (no global state) when possible — easier to reason about.

### Useful interpreter flags
```bash
python -O script.py        # strip asserts, slightly faster
python -X dev script.py    # extra warnings, useful while debugging
python -m cProfile script.py  # profiler
```

---

## 2. Core Syntax That Pays Off

### Walrus operator `:=` (Python 3.8+)
Assigns and returns a value in one expression — great for `while` loops and comprehensions.
```python
# Read until a short line is found
while (line := input().strip()) != "END":
    process(line)

# Inside a comprehension
nums = [1, 2, 3, 4, 5]
squares_over_10 = [y for x in nums if (y := x * x) > 10]  # [16, 25]
```

### Multiple assignment & swap
```python
a, b = 1, 2
a, b = b, a          # swap, no temp variable
x, *rest = [1, 2, 3, 4]   # x=1, rest=[2,3,4]
first, *middle, last = [1, 2, 3, 4, 5]
```

### Unpacking in loops
```python
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(x + y)
```

### Ternary expression
```python
sign = "positive" if x > 0 else "non-positive"
```

### `enumerate` and `zip`
```python
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

names = ["Al", "Bo", "Cy"]
ages = [10, 20, 30]
for name, age in zip(names, ages):
    print(name, age)

# enumerate with custom start
for i, val in enumerate(arr, start=1):  # 1-indexed
    ...
```

### `any()` / `all()` short-circuit
```python
has_neg = any(x < 0 for x in nums)
all_pos = all(x > 0 for x in nums)
```

### `f-strings` (3.6+)
```python
name = "world"
print(f"hello {name}")

# Format spec
pi = 3.14159
print(f"{pi:.2f}")     # 3.14
print(f"{1000000:,}")  # 1,000,000
print(f"{42:08b}")     # 00101010  (binary, 8 digits)
print(f"{255:x}")      # ff         (hex)
```

### `match` statement (3.10+)
Pattern matching — handy for parsing or state machines.
```python
def describe(point):
    match point:
        case (0, 0):
            return "origin"
        case (0, y):
            return f"y-axis at {y}"
        case (x, 0):
            return f"x-axis at {x}"
        case (x, y):
            return f"point ({x}, {y})"
```

### Conditional & chained comparison
```python
if 0 <= x < 10:    # valid Python
    print("single digit")
```

### Truthiness — what is `False`?
`None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()` are all falsy.
Everything else is truthy.
```python
if not stack:           # instead of `if len(stack) == 0`
    return -1
if queue:               # instead of `if len(queue) > 0`
    ...
```

---

## 3. Built-in Data Structures (the big four)

| Structure | Literal | Ordered? | Mutable? | Duplicates? | Lookup |
|-----------|---------|----------|----------|-------------|--------|
| `list`    | `[1, 2]` | Yes | Yes | Yes | O(n) |
| `tuple`   | `(1, 2)` | Yes | No | Yes | O(n) |
| `dict`    | `{1: 'a'}` | Yes (insertion order, 3.7+) | Yes | Keys unique | O(1) avg |
| `set`     | `{1, 2}` | No | Yes | No | O(1) avg |

### 3.1 Lists
```python
a = [1, 2, 3]

# Adding
a.append(4)         # O(1) amortized, adds to end
a.insert(0, 0)      # O(n), inserts at index
a.extend([5, 6])    # O(k), appends iterable

# Removing
a.pop()             # O(1), removes & returns last
a.pop(0)            # O(n), removes & returns index 0
a.remove(2)         # O(n), removes first matching value
del a[1:3]          # slice deletion

# Searching
a.index(2)          # O(n), raises ValueError if missing
2 in a              # O(n)

# Slicing (returns a new list)
a[1:3]              # [a[1], a[2]]
a[::-1]             # reversed copy
a[::2]              # every other element
a[-2:]              # last two elements

# Sorting
a.sort()            # in-place, O(n log n)
sorted(a)           # returns new sorted list
a.sort(reverse=True)
```

> ⚠️ **`list.pop(0)` and `list.insert(0, x)` are O(n).** Use `collections.deque` for FIFO queues.

### 3.2 Tuples
Immutable, hashable (can be dict keys / set members).
```python
point = (1, 2)
point[0] = 10   # TypeError: tuples are immutable

# Single-element tuple needs trailing comma
single = (42,)   # NOT (42), which is just int 42

# Useful for multi-key dict keys
graph = {(0, 0): "start", (1, 1): "end"}
```

### 3.3 Dictionaries
```python
d = {"a": 1, "b": 2}

# Access
d["a"]              # KeyError if missing
d.get("c")          # None if missing
d.get("c", 0)       # 0 if missing  (default)

# Insert/update
d["c"] = 3
d.update({"d": 4, "e": 5})

# Delete
del d["a"]
val = d.pop("b")         # remove and return
val = d.pop("z", None)   # safe pop with default

# Iteration
for k in d:              # keys
for k, v in d.items():   # key, value pairs
list(d.values())
list(d.keys())

# Modern API (3.7+ guarantees insertion order)
d = {3: "c", 1: "a", 2: "b"}
list(d.items())  # [(3,'c'), (1,'a'), (2,'b')]  — insertion order
```

#### `setdefault` and `defaultdict` — avoid manual key checks
```python
# Old way (verbose)
if k not in d:
    d[k] = []
d[k].append(x)

# Better: setdefault
d.setdefault(k, []).append(x)

# Best for grouping: defaultdict
from collections import defaultdict
d = defaultdict(list)
d[k].append(x)   # works even if k not yet present
```

### 3.4 Sets
```python
s = {1, 2, 3}
s.add(4)
s.discard(4)        # no error if missing (unlike remove)
s.remove(99)        # KeyError if missing
3 in s              # O(1) avg

# Set operations (return new sets)
{1, 2, 3} & {2, 3, 4}    # intersection -> {2, 3}
{1, 2, 3} | {2, 3, 4}    # union        -> {1, 2, 3, 4}
{1, 2, 3} - {2, 3, 4}    # difference   -> {1}
{1, 2, 3} ^ {2, 3, 4}    # symmetric diff -> {1, 4}
{1, 2}.issubset({1, 2, 3})
{1, 2, 3}.issuperset({1, 2})
```

### Hashability rule
> **Only hashable objects can go in a `set` or be `dict` keys.**
> Hashable = immutable (`int`, `float`, `str`, `tuple` of hashables). Lists and dicts are **not**
> hashable. Use `tuple` instead of `list` when you need a key.

```python
{(0, 0): "start"}     # OK — tuple of ints
{[0, 0]: "start"}     # TypeError — list is unhashable
```

---

## 4. The `collections` Module

The single most useful module for DSA. Memorize these four.

### 4.1 `Counter` — frequency counting
```python
from collections import Counter

c = Counter("abracadabra")
print(c)                # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
c["a"]                  # 5
c["z"]                  # 0  (no KeyError — returns 0 for missing)

# Most common
c.most_common(2)        # [('a', 5), ('b', 2)]

# Arithmetic
Counter(a=3, b=1) + Counter(a=1, c=2)   # Counter({'a': 4, 'c': 2, 'b': 1})
Counter(a=3) - Counter(a=5)             # Counter() — no negative counts by default

# Useful: anagram check
def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

### 4.2 `defaultdict` — auto-initialized values
```python
from collections import defaultdict

# Group items
groups = defaultdict(list)
for word in ["eat", "tea", "tan", "ate"]:
    key = "".join(sorted(word))
    groups[key].append(word)

# Counters
count = defaultdict(int)
for x in nums:
    count[x] += 1

# Nested structures
graph = defaultdict(list)
graph[1].append(2)   # works even if 1 not yet in graph
```

### 4.3 `deque` — double-ended queue
O(1) append/pop on **both** ends. Use for BFS, sliding windows, queues.
```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)           # append right  -> deque([1,2,3,4])
q.appendleft(0)       # append left   -> deque([0,1,2,3,4])
q.pop()               # pop right     -> 4
q.popleft()           # pop left      -> 0  (O(1), unlike list.pop(0))

# Rotations
q.rotate(1)           # rotate right by 1: [a,b,c,d] -> [d,a,b,c]
q.rotate(-1)          # rotate left by 1:  [a,b,c,d] -> [b,c,d,a]

# BFS pattern
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            queue.append(nei)
```

### 4.4 `OrderedDict` (mostly historical)
Since 3.7 regular `dict` keeps insertion order. `OrderedDict` is still useful for:
- **LRU cache** (its `.move_to_end()` and `.popitem(last=False)` are gold):
  ```python
  from collections import OrderedDict

  class LRU:
      def __init__(self, capacity):
          self.cap = capacity
          self.od = OrderedDict()
      def get(self, key):
          if key not in self.od:
              return -1
          self.od.move_to_end(key)    # mark recently used
          return self.od[key]
      def put(self, key, value):
          if key in self.od:
              self.od.move_to_end(key)
          self.od[key] = value
          if len(self.od) > self.cap:
              self.od.popitem(last=False)   # evict LRU (front)
  ```

### 4.5 `namedtuple` (lightweight records)
```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p.x        # 3
p.y        # 4
```

---

## 5. Heap / Priority Queue — `heapq`

Python has only a **min-heap**. For a max-heap, negate values.

```python
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 2)
heapq.heappop(h)        # 1 (smallest first)
h[0]                    # peek smallest (without popping)

# Build heap from list in O(n)
nums = [5, 3, 8, 1]
heapq.heapify(nums)     # in-place

# Get k smallest / largest
heapq.nsmallest(3, nums)
heapq.nlargest(3, nums)
```

### Max-heap via negation
```python
maxh = []
for x in [5, 3, 8, 1]:
    heapq.heappush(maxh, -x)
top = -heapq.heappop(maxh)   # 8
```

### Heap of tuples (priority queue)
Tuples compare lexicographically — the first element is the priority.
```python
pq = []
heapq.heappush(pq, (2, "low priority"))
heapq.heappush(pq, (1, "high priority"))
heapq.heappop(pq)    # (1, 'high priority')

# Dijkstra-style relaxation
heapq.heappush(pq, (dist, node))
```

> ⚠️ If two priorities are equal, Python tries to compare the second element. If that's a non-
> comparable object (e.g. a node), you'll get a `TypeError`. Add a tiebreaker:
> `heappush(pq, (dist, tiebreak_index, node))`.

### k-way merge / "top k" pattern
```python
# Keep only k largest items in a heap of size k (min-heap)
import heapq
def k_largest(nums, k):
    return heapq.nlargest(k, nums)   # or maintain manually:
    # h = []
    # for x in nums:
    #     heapq.heappush(h, x)
    #     if len(h) > k:
    #         heapq.heappop(h)
    # return h
```

---

## 6. Bisect — Binary Search on Sorted Sequences

`bisect` gives you binary search for free on any sorted sequence.
```python
import bisect

a = [1, 3, 5, 7, 9]

# Where to insert x to keep a sorted?
bisect.bisect_left(a, 5)    # 2  (leftmost position for 5)
bisect.bisect_right(a, 5)   # 3  (rightmost position+1 for 5)

# Insert while keeping sorted
bisect.insort(a, 6)         # a -> [1,3,5,6,7,9]
```

### Counting elements in range
```python
# How many elements in [lo, hi]?
def count_in_range(a, lo, hi):
    return bisect.bisect_right(a, hi) - bisect.bisect_left(a, lo)
```

> `bisect_left` is your go-to for "find the lower bound" (first index `>= x`).

---

## 7. Sorting & Custom Keys

### `sort()` vs `sorted()`
- `list.sort()` sorts in-place.
- `sorted(iterable)` returns a new sorted list (works on any iterable).

### Custom sort key
```python
words = ["apple", "kiwi", "banana"]
sorted(words, key=len)                  # by length
sorted(words, key=lambda w: w[-1])      # by last letter

# Sort intervals by start, then end
intervals = [[1, 3], [2, 6], [8, 10]]
intervals.sort(key=lambda iv: iv[0])

# Multi-criteria: by start ascending, then end descending
intervals.sort(key=lambda iv: (iv[0], -iv[1]))
```

### `operator.itemgetter` / `attrgetter` (faster than lambdas)
```python
from operator import itemgetter

intervals.sort(key=itemgetter(0))             # by first element
intervals.sort(key=itemgetter(0, 1))          # by first, then second
```

### Negative number for "descending" in tuple keys
```python
# Secondary sort descending via negation (numbers only)
items = [(1, 5), (1, 3), (2, 9), (1, 7)]
items.sort(key=lambda t: (t[0], -t[1]))
# -> [(1, 7), (1, 5), (1, 3), (2, 9)]
```

### Stable sort
Python's sort is **stable** — equal elements keep their original relative order.
```python
# Sort by score descending; ties keep input order
students = [("Al", 90), ("Bo", 90), ("Cy", 95)]
students.sort(key=lambda s: -s[1])
# [("Cy", 95), ("Al", 90), ("Bo", 90)]   <- Al still before Bo
```

### Reverse with `reverse=True`
```python
sorted([3, 1, 2], reverse=True)   # [3, 2, 1]
```

---

## 8. Itertools — Combinatorics & More

`itertools` is a Swiss-army knife for backtracking and enumeration problems.

### `product` — Cartesian product
```python
from itertools import product

list(product([1, 2], ["a", "b"]))
# [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

list(product("AB", repeat=2))
# [('A','A'), ('A','B'), ('B','A'), ('B','B')]
```

### `permutations` & `combinations`
```python
from itertools import permutations, combinations

list(permutations([1, 2, 3]))             # all orderings
list(permutations([1, 2, 3], 2))          # length-2 permutations
list(combinations([1, 2, 3, 4], 2))       # unordered pairs
list(combinations_with_replacement([1,2], 2))
```

### `accumulate` — prefix sums
```python
from itertools import accumulate
import operator

list(accumulate([1, 2, 3, 4]))                  # [1, 3, 6, 10]
list(accumulate([1, 2, 3, 4], operator.mul))    # [1, 2, 6, 24]
```

### `chain` — flatten iterables
```python
from itertools import chain

list(chain([1, 2], [3, 4], [5]))    # [1, 2, 3, 4, 5]
list(chain.from_iterable([[1, 2], [3, 4]]))   # same, takes one arg
```

### `groupby` — group consecutive equal elements
```python
from itertools import groupby

# NOTE: groupby groups CONSECUTIVE runs; sort first if you want all equal together.
for key, group in groupby(sorted("aaabbc")):
    print(key, list(group))
# a ['a','a','a']
# b ['b','b']
# c ['c']
```

### Infinite iterators
```python
from itertools import count, cycle, repeat

for i in count(10):           # 10, 11, 12, ...  (break out manually!)
    if i > 13: break

for c in cycle("AB"):         # A, B, A, B, ...  (infinite)
    ...

for x in repeat(0, 5):        # 0, 0, 0, 0, 0    (finite via 2nd arg)
    ...
```

### `islice`, `takewhile`, `dropwhile`
```python
from itertools import islice, takewhile, dropwhile

list(islice(range(100), 5))             # [0,1,2,3,4]  (lazy slice)
list(takewhile(lambda x: x < 3, [1,2,3,4,1]))   # [1,2]
list(dropwhile(lambda x: x < 3, [1,2,3,4,1]))   # [3,4,1]
```

---

## 9. Functions: `*args`, `**kwargs`, Lambdas, `partial`

### Argument packing/unpacking
```python
def sum_all(*args):           # args is a tuple
    return sum(args)
sum_all(1, 2, 3)              # 6

def show(**kwargs):           # kwargs is a dict
    for k, v in kwargs.items():
        print(k, v)
show(name="Al", age=10)

# Unpacking on call
nums = [1, 2, 3]
print(*nums)                  # same as print(1, 2, 3)
d = {"name": "Al", "age": 10}
show(**d)
```

### Lambdas (anonymous functions)
```python
square = lambda x: x * x
square(5)                    # 25

# Most useful as a sort key
sorted(words, key=lambda w: len(w))
```

> Lambdas are limited to a single expression. If your logic needs statements, use a `def`.

### `functools.partial` — fix some arguments
```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
square(5)                    # 25
```

### `functools.lru_cache` — memoization made trivial
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

fib(100)   # instantaneous, no recomputation
```

> ⚠️ `lru_cache` requires all arguments to be **hashable**. Don't pass lists — pass tuples.

### `functools.reduce`
```python
from functools import reduce

product = reduce(lambda x, y: x * y, [1, 2, 3, 4])   # 24
gcd_all = reduce(math.gcd, [12, 18, 24])              # 6
```

---

## 10. Strings & `str` Methods

### Slicing (same as lists)
```python
s = "hello"
s[::-1]      # "olleh"  (reverse)
s[1:4]       # "ell"
s[:3]        # "hel"
s[-2:]       # "lo"
```

### Case & whitespace
```python
"Hello".lower()             # "hello"
"hello".upper()             # "HELLO"
"  hi  ".strip()            # "hi"
"  hi  ".lstrip()           # "hi  "
"  hi  ".rstrip()           # "  hi"
"hello world".title()       # "Hello World"
"hello".capitalize()        # "Hello"
"hello world".swapcase()    # "HELLO WORLD"
```

### Splitting & joining
```python
"a,b,c".split(",")                 # ["a", "b", "c"]
"the sky is blue".split()          # ["the", "sky", "is", "blue"]
",".join(["a", "b", "c"])          # "a,b,c"
"".join(reversed("abc"))           # "cba"
"".join(c for c in s if c.isalnum())
```

### Membership & search
```python
"ell" in "hello"           # True
"hello".find("l")          # 2 (first index, -1 if not found)
"hello".rfind("l")         # 3 (last index)
"hello".count("l")         # 2
"hello".startswith("he")   # True
"hello".endswith("lo")     # True
"hello".replace("l", "L")  # "heLLo"
```

### Character classification
```python
"a".isalpha()    # True
"5".isdigit()    # True
"a1".isalnum()   # True
" ".isspace()    # True
"ABC".isupper()  # True
"abc".islower()  # True
```

### Character ↔ integer conversion
```python
ord("A")    # 65
chr(65)     # "A"

# Letter to 0..25 index
idx = ord(c) - ord("a")
```

### `str` is immutable
Every `str` method returns a **new** string. For building strings incrementally, use a list and
`"".join()`:
```python
# BAD — O(n^2) due to repeated string creation
result = ""
for c in chars:
    result += c

# GOOD — O(n)
result = "".join(chars)
```

### f-strings for formatting
```python
n = 42
print(f"{n:>5}")     # right-justify width 5 -> "   42"
print(f"{n:0>5}")    # zero-padded          -> "00042"
print(f"{n:b}")      # binary               -> "101010"
print(f"{n:o}")      # octal                -> "52"
print(f"{n:x}")      # hex lowercase        -> "2a"
```

---

## 11. Math, `math`, and Number Theory

### Built-in numeric types
```python
# Integers have arbitrary precision (no overflow!)
2 ** 100              # 1267650600228229401496703205376
10 / 3                # 3.333...  (float)
10 // 3               # 3         (floor division)
10 % 3                # 1         (modulo)
divmod(10, 3)         # (3, 1)    (quotient, remainder) in one call
```

> ⚠️ Floor division rounds toward **negative infinity**, not toward zero:
> `-7 // 2 == -4` (not `-3`). Use `int(a / b)` if you want truncation toward zero.

### The `math` module
```python
import math

math.floor(2.7)       # 2
math.ceil(2.1)        # 3
math.sqrt(16)         # 4.0
math.isqrt(16)        # 4   (integer sqrt, exact for big ints)
math.log(8, 2)        # 3.0
math.log2(8)          # 3.0
math.log10(1000)      # 3.0
math.exp(1)           # 2.718...
math.factorial(5)     # 120
math.comb(5, 2)       # 10   (binomial coefficient, 3.8+)
math.perm(5, 2)       # 20   (permutations, 3.8+)
math.gcd(12, 18)      # 6
math.lcm(4, 6)        # 12   (3.9+)
math.inf              # float infinity
math.pi, math.e       # constants
```

### Modular arithmetic (common in competitive problems)
```python
MOD = 10**9 + 7

a = (a + b) % MOD
a = (a * b) % MOD
# Negative result? Python's % always returns non-negative for positive modulus:
(-7) % 3              # 2  (not -1)

# Modular exponentiation (built-in, fast)
pow(base, exp, MOD)   # O(log exp), constant memory
```

### Primality test (trial division)
```python
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True
```

### Sieve of Eratosthenes
```python
def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, math.isqrt(n) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return [i for i, p in enumerate(is_p) if p]
```

### Fast exponentiation (binary exponentiation)
```python
def fast_pow(base, exp):
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result
```

### Random numbers
```python
import random
random.randint(1, 100)        # inclusive on both ends
random.choice([1, 2, 3])
random.shuffle(my_list)       # in-place
random.sample(population, k)  # k unique items
```

---

## 12. Bit Manipulation

### Operators
```python
5 & 3      # 1   AND
5 | 3      # 7   OR
5 ^ 3      # 6   XOR
~5         # -6  NOT (one's complement)
5 << 2     # 20  left shift  (multiply by 2^2)
5 >> 1     # 2   right shift (divide by 2, floor)
```

### Counting set bits
```python
bin(11).count("1")     # 3   (string approach, slow-ish)
11.bit_count()         # 3   (fast, Python 3.10+)

# Pre-3.10 fast version: Brian Kernighan's algorithm
def count_bits(n):
    count = 0
    while n:
        n &= n - 1      # clear lowest set bit
        count += 1
    return count
```

### Common tricks
```python
x & 1                  # check if odd (1 = odd, 0 = even)
x & (x - 1)            # clear lowest set bit  (1010 & 1001 = 1000)
x & -x                 # isolate lowest set bit (1010 & 0110 = 0010)
x | (x + 1)            # set lowest unset bit
x ^ x                  # 0  (XOR with self)
x ^ 0                  # x
x ^ y ^ y              # x  (XOR is its own inverse — basis of "single number")
```

### Power of two check
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

### Iterate over set bits
```python
n = 13  # binary 1101
while n:
    low = n & -n     # lowest set bit
    print(low)
    n ^= low         # or: n &= n - 1
# prints 1, 4, 8
```

### Subset enumeration (bitmask)
```python
# All subsets of [a, b, c]
items = ["a", "b", "c"]
n = len(items)
for mask in range(1 << n):           # 2^n masks
    subset = [items[i] for i in range(n) if mask & (1 << i)]
    print(subset)
```

### Enumerate subsets of a given mask (Gosper's hack)
```python
def subsets_of(mask):
    sub = mask
    while sub:
        yield sub
        sub = (sub - 1) & mask
    # yields all non-empty subsets of mask
```

---

## 13. Common Patterns Cheatsheet

Quick recipes for the patterns you'll see most. Each file in this folder lists the approaches
applicable to that problem.

### Two pointers (on array/string)
```python
def two_pointer(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # do something with arr[left], arr[right]
        if condition:
            left += 1
        else:
            right -= 1
```

### Sliding window (fixed size k)
```python
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]   # add new, drop old
        best = max(best, window_sum)
    return best
```

### Sliding window (variable size)
```python
def variable_window(s):
    left = 0
    counts = {}
    best = 0
    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1
        while window_invalid(counts):        # shrink while invalid
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
```

### Binary search (integer space)
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

> `mid = (lo + hi) // 2` is safe in Python (no overflow). In other languages use `lo + (hi - lo) // 2`.

### Binary search on answer (monotonic)
```python
def search_on_answer(lo, hi, feasible):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid       # look for smaller
        else:
            lo = mid + 1   # need bigger
    return lo
```

### Backtracking template
```python
def backtrack(state, choices):
    if is_goal(state):
        record(state)
        return
    for choice in choices:
        if is_valid(choice):
            apply(choice)
            backtrack(state, choices)
            undo(choice)        # backtrack
```

### DFS on a grid (with explicit in-place marking)
```python
def dfs(grid, r, c):
    if (r < 0 or r >= rows or c < 0 or c >= cols
            or grid[r][c] != "1"):
        return
    grid[r][c] = "0"            # mark visited in-place
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        dfs(grid, r + dr, c + dc)
```

### BFS (shortest path in unweighted graph)
```python
from collections import deque

def bfs(graph, start):
    q = deque([start])
    dist = {start: 0}
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in dist:
                dist[nei] = dist[node] + 1
                q.append(nei)
    return dist
```

### Topological sort (Kahn's algorithm)
```python
from collections import deque, defaultdict

def topo_sort(num_nodes, edges):
    adj = defaultdict(list)
    indeg = [0] * num_nodes
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(num_nodes) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == num_nodes else []   # [] = cycle
```

### Union-Find (Disjoint Set Union)
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        xr, yr = self.find(x), find(y)
        if xr == yr:
            return False        # already connected
        if self.rank[xr] < self.rank[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
        return True
```

### Monotonic stack (next greater element)
```python
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []                  # indices, values decreasing
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

### Trie
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.end

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
```

### Segment Tree (point update, range sum)
```python
class SegTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.tree[self.n:] = data
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        i //= 2
        while i:
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
            i //= 2

    def query(self, l, r):     # sum on [l, r)
        l += self.n
        r += self.n
        total = 0
        while l < r:
            if l & 1:
                total += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                total += self.tree[r]
            l //= 2
            r //= 2
        return total
```

### Fenwick Tree (Binary Indexed Tree)
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):     # 1-indexed
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):             # prefix sum [1..i]
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
```

---

## 14. Big-O Reference Table

### Time complexity of common Python operations

| Operation | Complexity |
|-----------|------------|
| `list[i]`, `list[i] = x` | O(1) |
| `list.append(x)`, `list.pop()` | O(1) amortized |
| `list.insert(0, x)`, `list.pop(0)` | O(n) |
| `x in list` | O(n) |
| `list.sort()` / `sorted(list)` | O(n log n) |
| `dict[k]`, `dict.get(k)` | O(1) avg |
| `dict[k] = v` | O(1) avg |
| `del dict[k]` | O(1) avg |
| `k in dict` | O(1) avg |
| `set.add(x)`, `x in set` | O(1) avg |
| `heapq.heappush/heappop` | O(log n) |
| `heapq.heapify` | O(n) |
| `str[i]` | O(1) |
| `s + t` (string concat) | O(len(s) + len(t)) |
| `"".join(list_of_strs)` | O(total length) |
| `substring in string` | O(n*m) worst, often better |

### Sorting algorithms at a glance

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| Python's Timsort (`sort`/`sorted`) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quickselect (`statistics.median`) | — | O(n) | O(n²) | O(log n) | — |
| Counting sort (small range) | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Yes |

### Common problem patterns and their complexity

| Pattern | Typical complexity |
|---------|-------------------|
| Brute force | O(n²) or O(n³) |
| Sorting + greedy | O(n log n) |
| Hashing (dict/set) | O(n) time, O(n) space |
| Two pointers | O(n) |
| Sliding window | O(n) |
| Binary search | O(log n) |
| Binary search on answer | O(n log R) where R = range |
| Monotonic stack | O(n) |
| BFS | O(V + E) |
| DFS | O(V + E) |
| Dijkstra | O((V + E) log V) |
| Topological sort | O(V + E) |
| Union-Find | O(α(n)) ≈ O(1) per op |
| Divide and conquer | O(n log n) typical |
| Backtracking | O(2^n) or O(n!) |
| 1D DP | O(n) or O(n²) |
| 2D DP | O(m·n) or O(n²) |
| Bitmask DP | O(2^n · n) |

---

## 15. Common Pitfalls & Bugs

### Mutable default arguments
```python
# BUG — default list is shared across calls
def f(items=[]):
    items.append(1)
    return items
f(); f()       # [1, 1]  — both calls share the same list!

# FIX
def f(items=None):
    if items is None:
        items = []
```

### Shallow vs deep copy
```python
a = [[1, 2], [3, 4]]
b = a.copy()              # shallow — inner lists still shared
b[0][0] = 99
print(a)                  # [[99, 2], [3, 4]]  — a was mutated!

import copy
b = copy.deepcopy(a)      # deep copy — fully independent
```

### Copying a 2D grid correctly
```python
grid = [[1,2],[3,4]]
# WRONG: copy = grid[:] or [row[:] for row in grid] is OK for read-only
# SAFE deep-ish copy of a grid (list of lists of primitives):
copy_grid = [row[:] for row in grid]

# Even safer for arbitrary nesting:
import copy
copy_grid = copy.deepcopy(grid)
```

### `is` vs `==`
```python
a = [1, 2]; b = [1, 2]
a == b     # True   (same values)
a is b     # False  (different objects)

# Use `is` only for identity (None, True, False, singletons)
if x is None: ...
if x is True: ...
```

### Integer division direction
```python
7 // 2      # 3
-7 // 2     # -4   (toward -inf, NOT toward zero!)
int(-7 / 2) # -3   (truncates toward zero — different!)
```

### `range()` excludes the end
```python
list(range(0, 5))      # [0, 1, 2, 3, 4]  — 5 is NOT included
list(range(5))         # same
list(range(2, 10, 2))  # [2, 4, 6, 8]
list(range(10, 0, -1)) # [10, 9, ..., 1]
```

### Off-by-one in slicing
```python
arr = [10, 20, 30, 40, 50]
arr[1:3]     # [20, 30]    — index 3 NOT included
arr[:2]      # [10, 20]    — first 2 elements
arr[-2:]     # [40, 50]    — last 2 elements
arr[1:-1]    # [20, 30, 40]  — drop first and last
```

### Comparing floats
```python
0.1 + 0.2 == 0.3     # False  — floating point!
# Use a tolerance:
abs(0.1 + 0.2 - 0.3) < 1e-9   # True
```

### Recursion depth
Python's default recursion limit is **1000**. Deep recursion (e.g. DFS on a 10⁵-node tree) will
raise `RecursionError`. Fix:
```python
import sys
sys.setrecursionlimit(10**6)
# Or convert to an explicit stack/queue.
```

### Mutable iteration during modification
```python
# BUG — modifying list while iterating
for x in nums:
    if x < 0:
        nums.remove(x)     # skips elements!

# FIX — iterate over a copy, or build a new list
nums = [x for x in nums if x >= 0]
```

### Dictionary size change during iteration
```python
# BUG — RuntimeError: dictionary changed size during iteration
for k in d:
    if d[k] == 0:
        del d[k]

# FIX — iterate over a copy of keys
for k in list(d.keys()):
    if d[k] == 0:
        del d[k]
```

### `heappop` from empty heap
```python
import heapq
h = []
heapq.heappop(h)   # IndexError
# Always check: while h and ...
```

### Tuple comparison surprise
```python
(1, 2) < (1, 3)     # True   — compares element by element
(1, "a") < (1, "b") # True
(1, "a") < (1, 2)   # TypeError — can't compare str and int
# In heaps/sorts, make sure tuple elements are mutually comparable.
```

### Class variables are shared (vs instance variables)
```python
class Node:
    cache = {}            # CLASS variable — shared by all instances!
    def __init__(self):
        self.data = {}    # instance variable — per instance

# Don't put per-node state in class scope.
```

---

## 16. Testing & Running Snippets

### Quick assertions
```python
assert two_sum([2, 7, 1, 15], 9) == [0, 1]
assert fib(10) == 55
```

### The `if __name__ == "__main__":` guard
```python
def two_sum(nums, target):
    ...

if __name__ == "__main__":
    # Runs only when this file is executed directly, not when imported
    print(two_sum([2, 7, 1, 15], 9))
```

### Timing a function
```python
import time
start = time.perf_counter()
result = my_function()
print(f"{time.perf_counter() - start:.4f}s")
```

### Quick brute-force comparison (to validate a fast solution)
```python
import random
def test(fast, slow, n_trials=1000):
    for _ in range(n_trials):
        case = generate_random_case()
        assert fast(case) == slow(case), f"Mismatch on {case}"
    print("All passed")
```

### Reading input (competitive style)
```python
# Single integer
n = int(input())
# List of ints
nums = list(map(int, input().split()))
# Multiple lines
lines = [input().strip() for _ in range(n)]

# Faster bulk read
import sys
data = sys.stdin.read().split()
```

---

## 17. Python vs Other Languages

Coming from another language? Here's what to unlearn.

| Concept | C++/Java | Python |
|---------|----------|--------|
| Integer overflow | Wraps / errors | **Never overflows** (arbitrary precision) |
| `swap(a, b)` | Needs temp | `a, b = b, a` |
| Pass-by-reference | Pointers/refs | Everything is an object reference; mutable objects share state |
| For loop | `for (int i=0; i<n; i++)` | `for i in range(n):` or `for x in arr:` |
| Array size | Fixed | Lists grow dynamically |
| HashMap syntax | `map[key]` with `.get()` | `dict[key]` with `.get(key, default)` |
| Sorting | `std::sort` / `Arrays.sort` | `list.sort()` (in-place) / `sorted(iter)` |
| Priority queue | `std::priority_queue` | `heapq` (min-heap by default) |
| Switch | `switch`/`case` | `match`/`case` (3.10+) or dict dispatch |
| String mutability | Mutable (`char[]`) | **Immutable** — use list of chars for in-place |
| Nullable | `null`/`nullptr` | `None` |
| Modulo on negatives | Often negative | **Always non-negative** for positive modulus |
| Recursion limit | Stack-bounded | Default 1000 — `sys.setrecursionlimit` to raise |

### Idioms unique to Python
- **List/dict/set comprehensions** — write loops as expressions.
- **`with` statement** — automatic resource cleanup (files, locks).
- **Decorators** (`@lru_cache`, `@property`) — wrap functions cleanly.
- **Duck typing** — if it walks like a stack and quacks like a stack, it's a stack.
- **First-class functions** — pass functions as arguments, return them, store in data structures.

### When Python is slower
- Tight numeric loops can be 10–100× slower than C++. For DSA problems this usually doesn't matter
  (time limits account for it), but watch out for:
  - O(n²) when O(n log n) exists (e.g. insertion sort vs. built-in sort).
  - Repeated string concatenation (use `''.join()`).
  - Recursion in deep DFS (convert to iterative or raise the limit).
- For truly hot numeric code, look at `array.array`, `bytearray`, or NumPy (not in scope for DSA).

---

## 18. Quick One-Liners

A grab-bag of expressions you'll reach for again and again.

```python
# Reverse a list/string
arr[::-1]; s[::-1]

# Sum, product, min, max, length
sum(arr); min(arr); max(arr); len(arr)
from functools import reduce; reduce(lambda a,b: a*b, arr)   # product

# Flatten one level
flat = [x for row in matrix for x in row]

# Transpose a matrix
transposed = list(zip(*matrix))

# Count frequencies
from collections import Counter
freq = Counter(arr)

# Deduplicate preserving order
seen = set(); ordered_uniq = [x for x in arr if not (x in seen or seen.add(x))]

# Sort by custom key
sorted(arr, key=lambda x: (x.priority, -x.timestamp))

# Pad a number with zeros
f"{n:05d}"          # 42 -> "00042"

# Most common element
Counter(arr).most_common(1)[0][0]

# GCD/LCM
import math; math.gcd(a, b); math.lcm(a, b)
# Or for a list: reduce(math.gcd, lst)

# Modular exponentiation
pow(base, exp, MOD)

# Check all equal
len(set(arr)) == 1

# All unique
len(set(arr)) == len(arr)

# Cartesian product
from itertools import product
list(product(a, b))
```

---

## Further Reading

- **Official docs** — `docs.python.org/3/`. The Library Reference is your friend.
- **`collections`** — `docs.python.org/3/library/collections.html`
- **`itertools`** — `docs.python.org/3/library/itertools.html`
- **`heapq`** — `docs.python.org/3/library/heapq.html`
- **PEP 8** — Python style guide.
- **"Fluent Python" by Luciano Ramalho** — deep dive into idiomatic Python.

---

## Suggested Learning Order for This Folder

The files in this folder are numbered `001`–`236` in a deliberate progression. Work through them
in order:

- **001–011**: Warm-up math & strings (palindrome, primes, Fibonacci, recursion basics)
- **012–024**: Array fundamentals (two sum, sliding max, product-except-self)
- **025–034**: Hashing & prefix sums (subarray sum k, longest consecutive, anagrams)
- **035–057**: Two pointers & sliding window (container with most water, min window substring)
- **058–062**: Matrices (spiral, rotate, game of life)
- **063–075**: Stacks, queues, deques (monotonic stack, daily temperatures, design problems)
- **076–086**: Binary search & search-on-answer (koko eating, capacity, median of two sorted)
- **087–098**: Linked lists (reverse, cycle, LRU cache)
- **099–102**: Recursion & basic backtracking (Hanoi, generate parentheses)
- **103–112**: Backtracking (subsets, permutations, N-Queens, Sudoku)
- **113–132**: Trees & traversals (DFS/BFS/iterative/Morris, LCA, serialize)
- **133–139**: BST operations
- **140–145**: Heaps & priority queues
- **146–152**: Interval problems
- **153–161**: Greedy (jump game, gas station, partition labels)
- **162–184**: Dynamic programming (1D, 2D, palindromes, regex matching)
- **185–190**: Advanced DP (stock cooldown, burst balloons, stone game)
- **191–216**: Graphs (BFS/DFS, topological sort, Union-Find, shortest paths)
- **217–221**: Tries
- **222–230**: Bit manipulation
- **231–236**: Advanced data structures (Fenwick, segment tree, RMQ)

---

### Final advice

1. **Solve first, optimize second.** Get a correct brute force, then think about the optimal
   approach the file lists.
2. **Recognize patterns.** Most problems are "two pointers", "sliding window", "BFS", "DP", or
   "Union-Find" in disguise.
3. **Use the standard library.** Python's batteries-included modules save dozens of lines per
   problem. `Counter`, `defaultdict`, `heapq`, `bisect`, `lru_cache` are the heavy lifters.
4. **Write clean code.** Future-you (and interviewers) will thank you. Name things well, keep
   functions short, and use the patterns above.
5. **Practice consistently.** 30 minutes a day beats 5 hours once a week.

Good luck with the 236 problems ahead. 🚀
