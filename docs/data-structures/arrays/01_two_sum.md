# Two Sum

**Author:** Harshul Raina
**Topic:** Arrays / Hash Map
**Leet Code:** 01-Two Sum
**Difficulty:** Easy

---

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers whose sum is equal to `target`.

You may assume that:

* There is exactly one valid solution.
* The same element cannot be used twice.
* The answer can be returned in any order.

### Example

```text
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
```

Because:

```text
nums[0] + nums[1]
= 2 + 7
= 9
```

---

# Brute-Force Approach

The simplest approach is to compare every number with every other number until we find a pair whose sum equals the target.

For example:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

The problem is that for every element, we may need to check many other
elements.

If the array contains `n` elements, the number of comparisons can grow
quadratically.

### Complexity

```text
Time:  O(n²)
Space: O(1)
```

The solution works, but the follow-up asks us to find an algorithm that
is faster than `O(n²)`.

---

# Optimized Approach — Hash Map

Instead of repeatedly searching the array, we can remember the numbers
we have already visited.

Suppose the current number is `x`.

We need another number that satisfies:

```text
x + complement = target
```

Rearranging the equation gives:

```text
complement = target - x
```

So for every number we encounter, we can calculate exactly which number
we need.

The question then becomes:

> **Have we already seen this complement?**

A Python dictionary is useful here because it provides average `O(1)`
lookup time.

We store each number along with its index:

```text
number → index
```

For example:

```text
2 → 0
7 → 1
```

This means that if we later need the number `2`, we immediately know
that it was located at index `0`.

---

# Optimized Solution — Example

Let's walk through one complete example:

```text
nums = [2, 7, 11, 15]
target = 9
```

Initially, our dictionary is empty:

```text
seen = {}
```

### First iteration

We are looking at:

```text
index  = 0
number = 2
```

Calculate the complement:

```text
complement = target - number
           = 9 - 2
           = 7
```

We need `7`, but `7` is not in `seen`.

So we store the current number and its index:

```text
seen = {
    2: 0
}
```

---

### Second iteration

Now:

```text
index  = 1
number = 7
```

Calculate:

```text
complement = 9 - 7
           = 2
```

Now we check `seen`.

The dictionary contains:

```text
2 → 0
```

So we have found the required pair.

The previous number `2` is at index `0`, and the current number `7` is
at index `1`.

Therefore:

```text
return [0, 1]
```

We do not need to examine `11` or `15` because the solution has already
been found.

---

# Code

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

    for index, number in enumerate(nums):
        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    raise ValueError("No valid solution exists.")
```

---

# Code Flow

The entire algorithm can be understood as this flow:

```text
Start
  ↓
Create empty dictionary
  ↓
Take the next number
  ↓
Calculate its complement
  ↓
Is complement already in dictionary?
  │
  ├── YES → Return previous index + current index
  │
  └── NO  → Store current number and index
               ↓
          Move to next number
```

The important part is that we **check first and store second**.

```python
if complement in seen:
    return [seen[complement], index]

seen[number] = index
```

This ensures that the current element is never matched with itself.

---

# Code Walkthrough

Let's connect each line of the code to the algorithm.

### 1. Create the dictionary

```python
seen: dict[int, int] = {}
```

`seen` keeps track of numbers that we have already visited.

The key is the number and the value is its index.

For example:

```text
seen = {
    2: 0,
    7: 1
}
```

means:

```text
2 was found at index 0
7 was found at index 1
```

---

### 2. Iterate through the array

```python
for index, number in enumerate(nums):
```

`enumerate()` gives us both:

* `index` — where the number is located
* `number` — the actual value

For:

```text
nums = [2, 7, 11, 15]
```

the iterations are:

```text
index = 0, number = 2
index = 1, number = 7
index = 2, number = 11
index = 3, number = 15
```

---

### 3. Calculate the complement

```python
complement = target - number
```

This tells us exactly what value is needed to reach the target.

For example:

```text
target = 9
number = 7

complement = 9 - 7
           = 2
```

So we need to know whether we have already encountered `2`.

---

### 4. Check the dictionary

```python
if complement in seen:
```

This asks:

> "Have we already seen the number that completes the target?"

If the answer is yes, we already know its index.

---

### 5. Return the two indices

```python
return [seen[complement], index]
```

`seen[complement]` gives us the index of the previously encountered
number.

`index` is the position of the current number.

Together they form the answer.

For our example:

```text
seen[2] = 0
index   = 1
```

Therefore:

```text
[0, 1]
```

---

### 6. Store the current number

If the complement wasn't found, we haven't found a pair yet.

So we save the current number:

```python
seen[number] = index
```

For example:

```text
number = 2
index = 0
```

becomes:

```text
seen = {
    2: 0
}
```

This information may be needed by a future element.

---

### 7. Handle an impossible case

```python
raise ValueError("No valid solution exists.")
```

The problem guarantees that a solution exists, so normally this line
will never execute.

It is still good practice for the function to explicitly handle the
case where no pair is found instead of silently returning `None`.

---

# Complexity Analysis

Let `n` be the number of elements in `nums`.

### Time: `O(n)`

We traverse the array only once.

Each dictionary lookup and insertion takes `O(1)` average time.

Therefore:

```text
O(n)
```

### Space: `O(n)`

In the worst case, we may store almost every element in the dictionary
before finding the answer.

Therefore:

```text
O(n)
```

### Final Complexity

```text
Time:  O(n) average
Space: O(n)
```

---

# Key Takeaway

The main lesson from Two Sum is the **complement pattern**.

Instead of searching for a pair directly, calculate what is missing:

```text
complement = target - current
```

Then use a hash map to check whether that value has already appeared.

The thought process changes from:

```text
"Which number should I compare this with?"
```

to:

```text
"What number do I need, and have I already seen it?"
```

That change allows us to replace the repeated searching of the
brute-force solution with a fast hash-map lookup:

```text
Brute Force:  O(n²)
Hash Map:     O(n) average
```

This **hash-map + complement** pattern is worth remembering because the
same idea appears in many array and lookup-based DSA problems.
