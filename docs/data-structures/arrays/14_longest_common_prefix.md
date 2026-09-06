# Longest Common Prefix

**Author:** Harshul Raina  
**Problem:** LeetCode 14 - Longest Common Prefix  
**Topic:** Strings / Arrays  
**Difficulty:** Easy

---

## Problem

Given an array of strings, find the longest prefix that is common to
every string.

If the strings do not share a common prefix, return an empty string
`""`.

A **prefix** is a sequence of characters that appears at the beginning
of a string.

For example:

```text
"flower" → "f", "fl", "flo", "flow", ...
```

### Example

```text
Input:
strs = ["flower", "flow", "flight"]

Output:
"fl"
```

All three strings begin with:

```text
f → l
```

At the next position:

```text
flower → o
flow   → o
flight → i
```

The characters are different, so the common prefix ends at `"fl"`.

---

# Understanding the Problem

The easiest way to think about this problem is to compare the strings
**character by character at the same position**.

Take:

```text
flower
flow
flight
```

Line them up:

```text
Position:  0  1  2  3  4  5

flower:    f  l  o  w  e  r
flow:      f  l  o  w
flight:    f  l  i  g  h  t
```

At position `0`, every string contains `f`.

At position `1`, every string contains `l`.

At position `2`, the strings contain:

```text
flower → o
flow   → o
flight → i
```

There is a mismatch.

Once a mismatch occurs, no longer prefix can exist. Therefore,
everything before that position is the answer.

This is called **vertical scanning** because we compare the same
character position across all strings before moving to the next
position.

---

# Optimized Approach

We use the first string as our reference string.

For every character in the first string:

1. Compare that character with the same position in every other string.
2. If another string is too short, the prefix cannot continue.
3. If a character is different, return everything before that position.
4. If the entire first string matches, return the first string.

The key idea is:

> **The first mismatch tells us exactly where the common prefix ends.**

There is no reason to continue checking after that point.

---

# Optimized Solution — Example

Consider:

```text
strs = ["flower", "flow", "flight"]
```

We use:

```text
first_string = "flower"
```

### Position 0

Reference character:

```text
f
```

Comparison:

```text
flower → f
flow   → f
flight → f
```

Everything matches.

---

### Position 1

Reference character:

```text
l
```

Comparison:

```text
flower → l
flow   → l
flight → l
```

Everything still matches.

So far, the common prefix is:

```text
"fl"
```

---

### Position 2

Reference character:

```text
o
```

Comparison:

```text
flower → o
flow   → o
flight → i
```

`i` does not match `o`.

The first mismatch is at index `2`, so we return:

```python
first_string[:2]
```

which gives:

```text
"fl"
```

Therefore:

```text
Output:
"fl"
```

Because the first mismatch occurs at index `2`, no prefix longer than
`"fl"` can be common to all three strings.

---

# Python Implementation

```python
def longest_common_prefix(strs: list[str]) -> str:
    first_string = strs[0]

    for index, character in enumerate(first_string):
        for string in strs[1:]:
            if index >= len(string) or string[index] != character:
                return first_string[:index]

    return first_string
```

---

# Code Flow

The algorithm follows this flow:

```text
Start
  ↓
Take the first string as the reference
  ↓
Check each character in the reference
  ↓
Compare that character with the same position
in every other string
  ↓
Is a string too short OR is there a mismatch?
  │
  ├── YES → Return the prefix before this position
  │
  └── NO  → Move to the next character
              ↓
        Finished the reference string?
              │
              └── YES → Return the first string
```

The important stopping condition is:

```python
if index >= len(string) or string[index] != character:
```

There are two reasons to stop:

1. Another string has no character at this position.
2. The character is different from the reference character.

---

# Code Walkthrough

### 1. Store the first string

```python
first_string = strs[0]
```

We use the first string as our reference.

We do not need to find the shortest string beforehand because the
algorithm automatically stops if another string ends first.

---

### 2. Iterate through the reference string

```python
for index, character in enumerate(first_string):
```

`enumerate()` gives us both the position and the character.

For `"flower"`:

```text
index = 0, character = 'f'
index = 1, character = 'l'
index = 2, character = 'o'
index = 3, character = 'w'
...
```

---

### 3. Compare with every other string

```python
for string in strs[1:]:
```

`strs[1:]` skips the first string because it is already our reference.

For:

```text
["flower", "flow", "flight"]
```

we compare against:

```text
"flow"
"flight"
```

---

### 4. Detect a mismatch

```python
if index >= len(string) or string[index] != character:
```

The first condition:

```python
index >= len(string)
```

checks whether the current string is too short.

The second:

```python
string[index] != character
```

checks whether the characters differ.

If either condition is true, the common prefix cannot continue.

---

### 5. Return the prefix

```python
return first_string[:index]
```

Python slicing returns characters from the beginning up to, but not
including, `index`.

For:

```text
first_string = "flower"
index = 2
```

we get:

```text
first_string[:2] = "fl"
```

This is exactly what we want because index `2` is the first position
where the strings disagree.

---

### 6. Return the complete first string

```python
return first_string
```

If we reach this line, every character of the first string matched
every other string.

Therefore, the entire first string is the common prefix.

---

# Complexity Analysis

Let:

- `n` = number of strings
- `m` = length of the shortest string

At most `m` character positions can be common, and at each position we
may compare against all `n` strings.

### Time Complexity

```text
O(n × m)
```

The algorithm may stop earlier when it finds a mismatch.

### Space Complexity

```text
O(1)
```

The algorithm uses only a few variables and no additional data
structure that grows with the input.

---

# Key Takeaway

The main lesson is to **stop as soon as the answer is determined**.

For a common prefix, every string must agree at every position:

```text
Match      → continue
Mismatch   → stop
String ends → stop
```

The first position where the strings disagree tells us exactly where
the longest common prefix ends.

The DSA pattern to remember is:

> **Compare the same position across all strings and stop at the first
> mismatch.**
