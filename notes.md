# Sets in Python
unordered, no duplicates, mutable(add/remove)

## Creating Sets
s = set()
s1 = set([1, 2, 3, 4])
s2 = set("hello")
s3 = set((10, 20, 30, 10))

print(s1)  # {1, 2, 3, 4}
print(s2)  # {'e', 'o', 'l', 'h'}
print(s3)  # {10, 20, 30}

## Basic Set Operations
s = {1, 2, 3}
s.add(4)               # Add single element
s.update([5, 6])       # Add multiple elements
s.remove(2)            # Remove element, raises error if not found
s.discard(10)          # Remove element, no error if not found
s.pop()                # Remove and return arbitrary element
s.clear()              # Remove all elements

## Set Mathematical Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

### Union
print(a | b)           # {1, 2, 3, 4, 5, 6}
print(a.union(b))

### Intersection
print(a & b)           # {3, 4}
print(a.intersection(b))

### Difference
print(a - b)           # {1, 2}
print(a.difference(b))

### Symmetric Difference
print(a ^ b)           # {1, 2, 5, 6}
print(a.symmetric_difference(b))

## Set Comparisons
a = {1, 2, 3}
b = {1, 2}
c = {1, 2, 3}

print(b.issubset(a))       # True
print(a.issuperset(b))     # True
print(a == c)              # True
print(a != b)              # True
print(a.isdisjoint({4}))   # True (no common elements)


## Immutable Set (frozenset)
fs = frozenset([1, 2, 3])
fs.add(4)  ❌ Not allowed (immutable)
print(fs)                 # frozenset({1, 2, 3})


## Set Comprehension
squares = {x*x for x in range(5)}
print(squares)            # {0, 1, 4, 9, 16}

## Practice Questions
1) Create a set of unique vowels in the string "hello world".
```
def unique_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return set(s.lower()) & vowels

print(unique_vowels("hello world"))  # Output: {'o', 'e'}

```
2) Given two sets A and B, return elements only in A but not in B.
```
def difference(a, b):
    return a - b

A = {1, 2, 3, 4, 5}
B = {4, 5, 6}
print(difference(A, B))  # Output: {1, 2, 3}

```
3) Remove all even numbers from a given set.
```
def remove_even(s):
    return {x for x in s if x % 2 != 0}

s = {1, 2, 3, 4, 5, 6}
print(remove_even(s))  # Output: {1, 3, 5}
```

4) Write a function to check if two sets are disjoint.
```
def are_disjoint(a, b):
    return a.isdisjoint(b)

print(are_disjoint({1, 2}, {3, 4}))  # Output: True
print(are_disjoint({1, 2}, {2, 3}))  # Output: False
```