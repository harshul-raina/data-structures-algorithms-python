# Array

> A practical reference for Python's `array.array` with examples, type codes, and common operations.

| Field | Details |
|---|---|
| **Author** | Harshul Raina |
| **Version** | 1.0.0 |
| **Language** | Python |
| **Module** | `array` |
| **Last Updated** | 05 September 2026 |

---

## 1. Definition

An **array** is a collection of elements stored in an ordered sequence, where each element can be accessed using an index.

In Python, the standard-library `array` module provides `array.array`, which stores values of a **single specified type** using a compact representation.

Python's `array.array` behaves similarly to a list in many respects, but unlike a list, the type of values stored in the array is constrained by its **type code**.

> **Important:** Arrays are fixed-size in many programming languages such as C and Java. However, Python's `array.array` is **resizable** and provides methods such as `append()`, `insert()`, and `extend()`. citeturn0search0

---

## 2. Importing `array`

```python
from array import array
```

The constructor has the following general form:

```python
array(typecode, initializer)
```

For example:

```python
from array import array

int_array = array('l', [0] * 7)

print(len(int_array))
# 7
```

Here:

- `'l'` is the **type code**.
- `[0] * 7` creates seven initial integer values.
- `len(int_array)` returns the number of elements.

---

## 3. Type Codes

A **type code** determines the C type, Python type, and minimum storage size used for each element.

The following table is based on the official Python documentation. citeturn0search0

```text
+----------+-------------------+-------------------+------------------------+-------+
| Typecode | C Type            | Python Type       | Minimum Size (bytes)   | Notes |
+----------+-------------------+-------------------+------------------------+-------+
| 'b'      | signed char       | int               | 1                      |       |
| 'B'      | unsigned char     | int               | 1                      |       |
| 'w'      | Py_UCS4           | Unicode character | 4                      | (1)   |
| 'h'      | signed short      | int               | 2                      |       |
| 'H'      | unsigned short    | int               | 2                      |       |
| 'i'      | signed int        | int               | 2                      |       |
| 'I'      | unsigned int      | int               | 2                      |       |
| 'l'      | signed long       | int               | 4                      |       |
| 'L'      | unsigned long     | int               | 4                      |       |
| 'q'      | signed long long  | int               | 8                      |       |
| 'Q'      | unsigned long long| int               | 8                      |       |
| 'e'      | _Float16          | float             | 2                      | (2)   |
| 'f'      | float             | float             | 4                      |       |
| 'd'      | double            | float             | 8                      |       |
| 'Zf'     | float complex     | complex           | 8                      | (3)   |
| 'Zd'     | double complex    | complex           | 16                     | (3)   |
+----------+-------------------+-------------------+------------------------+-------+
```

### Notes

1. `'w'` was added in Python 3.13.
2. `'e'` was added in Python 3.14/3.15-era documentation and depends on compiler support for `_Float16`.
3. `'Zf'` and `'Zd'` are complex-number type codes available in current Python documentation.

The **actual size** of an array item can depend on the machine architecture and C implementation. Use `array.itemsize` when the actual size matters.

> **Source:** [Python `array` documentation](https://docs.python.org/3/library/array.html)
---

## 4. Creating an Array

```python
from array import array

int_array = array('l', [0] * 7)

print(int_array)
# array('l', [0, 0, 0, 0, 0, 0, 0])

print(len(int_array))
# 7
```

The array contains seven elements, and each element is stored using the type specified by `'l'`.

---

# 5. Accessing and Updating Elements

Array elements can be accessed using their index, just like list elements.

```python
from array import array

int_array = array('l', [0] * 7)

int_array[0] = 20
int_array[1] = 35
int_array[2] = -15
int_array[3] = 7
int_array[4] = 55
int_array[5] = 1
int_array[6] = 1

print(int_array)
# array('l', [20, 35, -15, 7, 55, 1, 1])
```

### Indexing

```python
print(int_array[0])
# 20

print(int_array[3])
# 7

print(int_array[-1])
# 1
```

---

# 6. `itemsize`

The `itemsize` attribute returns the number of bytes used by **one element** in the array's internal representation.

```python
print(int_array.itemsize)
# 4
```

For the `'l'` type code, the Python documentation specifies a minimum size of 4 bytes. The actual size is determined by the platform.

For example:

```python
from array import array

int_array = array('l', [0] * 7)

print(int_array.itemsize)
# 4
```

If the array contains 7 elements and each element occupies 4 bytes:

```text
7 elements × 4 bytes = 28 bytes
```

This describes the size of the element storage itself and does not represent the complete memory overhead of the Python object.

---

# 7. Array Size

`len()` returns the number of elements currently stored in the array.

```python
from array import array

int_array = array('l', [0] * 7)

print(len(int_array))
# 7
```

Unlike a fixed-size array in languages such as C, Python's `array.array` can change its length.

```python
int_array.append(100)

print(len(int_array))
# 8
```

---

# 8. Append

The `append()` method adds one new element to the **end** of the array.

```python
from array import array

int_array = array('l', [0] * 7)

int_array[0] = 20
int_array[1] = 35
int_array[2] = -15
int_array[3] = 7
int_array[4] = 55
int_array[5] = 1
int_array[6] = 1

print(int_array)
# array('l', [20, 35, -15, 7, 55, 1, 1])

int_array.append(100)

print(int_array)
# array('l', [20, 35, -15, 7, 55, 1, 1, 100])
```

`append()` changes the length of the array by one. The appended value must be compatible with the array's type code. citeturn0search0

---

# 9. Insert

The `insert()` method adds an element at a specified position.

```python
from array import array

int_array = array('l', [10, 20, 30, 40])

int_array.insert(2, 25)

print(int_array)
# array('l', [10, 20, 25, 30, 40])
```

The elements after the insertion point are shifted to make room for the new element.

---

# 10. Extend

The `extend()` method adds multiple elements to the end of an array.

```python
from array import array

int_array = array('l', [10, 20, 30])

int_array.extend([40, 50, 60])

print(int_array)
# array('l', [10, 20, 30, 40, 50, 60])
```

The values added must be compatible with the array's type.

---

# 11. Common Array Operations

| Operation | Example | Purpose |
|---|---|---|
| Create | `array('l', [1, 2, 3])` | Create an array |
| Access | `arr[0]` | Read an element |
| Update | `arr[0] = 10` | Modify an element |
| Length | `len(arr)` | Get number of elements |
| Append | `arr.append(10)` | Add to the end |
| Insert | `arr.insert(1, 10)` | Add at a position |
| Extend | `arr.extend([10, 20])` | Add multiple values |
| Remove | `arr.remove(10)` | Remove first matching value |
| Pop | `arr.pop()` | Remove and return an element |
| Reverse | `arr.reverse()` | Reverse the array |
| Index | `arr.index(10)` | Find the first matching index |

---

# 12. Array vs Python List

Python's `array.array` and `list` are both mutable sequences, but they serve different purposes.

| Feature | `array.array` | `list` |
|---|---|---|
| Element type | Restricted by type code | Can contain different object types |
| Memory representation | Compact typed values | References to Python objects |
| Index access | `O(1)` | `O(1)` |
| Append | Supported | Supported |
| Insert | Supported | Supported |
| Extend | Supported | Supported |
| General-purpose use | More specialized | More common |
| Numeric storage | Compact | Higher per-element object overhead |

### Example

```python
from array import array

numbers = array('i', [10, 20, 30])

values = [10, 20, 30]
```

Use a Python `list` for general-purpose collections.

Use `array.array` when you specifically need a compact, typed array from Python's standard library.

---

# 13. Time Complexity

For common operations:

| Operation | Typical Complexity |
|---|---:|
| Access by index | `O(1)` |
| Update by index | `O(1)` |
| Search | `O(n)` |
| Append | `O(1)` amortized |
| Insert | `O(n)` |
| Delete | `O(n)` |

> Exact performance characteristics should be considered together with the operation being performed and the underlying implementation.

---

# 14. Complete Example

```python
from array import array

# Create an integer array with seven elements.
int_array = array('l', [0] * 7)

# Update elements.
int_array[0] = 20
int_array[1] = 35
int_array[2] = -15
int_array[3] = 7
int_array[4] = 55
int_array[5] = 1
int_array[6] = 1

# Display the array.
print(int_array)
# array('l', [20, 35, -15, 7, 55, 1, 1])

# Number of elements.
print(len(int_array))
# 7

# Size of one element.
print(int_array.itemsize)
# 4

# Add an element.
int_array.append(100)

print(int_array)
# array('l', [20, 35, -15, 7, 55, 1, 1, 100])
```

---

# 15. Key Points

- Python provides typed arrays through the standard-library `array` module.
- `array.array` stores values of a single specified type.
- The **type code** determines the allowed element type.
- `len()` returns the current number of elements.
- `itemsize` returns the number of bytes used by one array element.
- Python arrays are **resizable**, even though arrays in many other languages are fixed-size.
- Common modification methods include `append()`, `insert()`, and `extend()`.
- Use `array.array` when compact typed numeric storage is useful.
- For general-purpose collections, Python's `list` is usually the more appropriate choice.

---

## Reference

- [Python `array` — Efficient arrays of numeric values](https://docs.python.org/3/library/array.html)