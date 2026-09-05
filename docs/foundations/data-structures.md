# Data Structures

> A structured reference for Data Structures and Algorithms using Python.

| Field | Details |
|---|---|
| **Author** | Harshul Raina |
| **Version** | 1.0.0 |
| **Language** | Python |
| **Category** | Data Structures & Algorithms |
| **Status** | Active |
| **Last Updated** | 05 September 2026 |

---

## Version History

| Version | Date | Changes |
|---|---|---|
| **1.0.0** | 05 September 2026 | Initial documentation covering fundamental data structures. |

---

# 1. Introduction

## 1.1 What is a Data Structure?

A **data structure** is a way of organizing and storing data so that it can be accessed, modified, and processed efficiently.

Different data structures are designed around different operations. For example, an array provides fast index-based access, a hash table provides fast average-case key lookup, and a queue provides efficient first-in-first-out processing.

The choice of data structure directly affects the **time complexity**, **space complexity**, and overall design of an algorithm.

### Common Operations

| Operation | Description |
|---|---|
| **Access** | Retrieve an element from a known position or key. |
| **Search** | Find an element with a particular value or property. |
| **Insertion** | Add a new element. |
| **Deletion** | Remove an existing element. |
| **Update** | Modify an existing element. |
| **Traversal** | Visit elements according to a defined order. |
| **Sorting** | Arrange elements according to a defined order. |

---

# 2. Complexity Basics

Big-O notation describes how the resource requirements of an algorithm or operation grow as the input size `n` increases.

From generally more efficient to less efficient growth:

```text
O(1)
  ↓
O(log n)
  ↓
O(n)
  ↓
O(n log n)
  ↓
O(n²)
  ↓
O(2ⁿ)
  ↓
O(n!)
```

> Big-O describes an asymptotic upper bound. Actual performance also depends on implementation details, constants, memory access patterns, and the input.

---

# 3. Classification

```text
Data Structures
│
├── Linear
│   ├── Array / Dynamic Array
│   ├── Linked List
│   ├── Stack
│   ├── Queue
│   └── Deque
│
├── Hash-Based
│   ├── Hash Table
│   └── Set
│
├── Tree-Based
│   ├── General Tree
│   ├── Binary Tree
│   ├── Binary Search Tree
│   ├── Balanced Search Tree
│   ├── Heap
│   ├── Trie
│   └── B-Tree / B+ Tree
│
├── Graph-Based
│   └── Graph
│
└── Specialized
    ├── Disjoint Set / Union-Find
    ├── Segment Tree
    ├── Fenwick Tree
    └── Sparse Matrix
```

### Linear Data Structures

Elements are organized in a sequential manner. Each element generally has a well-defined predecessor or successor relationship.

### Non-Linear Data Structures

Elements can have hierarchical or many-to-many relationships rather than a single sequential order.

---

# 4. Linear Data Structures

## 4.1 Array / Dynamic Array

### Definition

An **array** stores elements in an ordered sequence and supports direct access using an index.

In Python, `list` is a **dynamic array**. It automatically manages its underlying storage as elements are added or removed.

```text
Index:    0      1      2      3
          ↓      ↓      ↓      ↓
        ┌────┬────┬────┬────┐
List:   │ 10 │ 20 │ 30 │ 40 │
        └────┴────┴────┴────┘
```

```python
numbers = [10, 20, 30, 40]

print(numbers[2])  # 30
```

### Complexity

| Operation | Typical | Worst |
|---|---:|---:|
| Access by index | `O(1)` | `O(1)` |
| Search | `O(n)` | `O(n)` |
| Append | `O(1)` amortized | `O(n)` |
| Insert | `O(n)` | `O(n)` |
| Delete | `O(n)` | `O(n)` |

### Strengths

- Fast index-based access.
- Simple and versatile.
- Good memory locality.
- Python lists are highly optimized.

### Weaknesses

- Middle insertion/deletion requires shifting elements.
- Searching an unsorted list is `O(n)`.
- Resizing can occasionally require moving elements.

### Best Use Cases

- Indexed collections
- Sequential data
- Dynamic programming
- Sorting
- Two-pointer and sliding-window problems

---

## 4.2 Linked List

### Definition

A **linked list** is a sequence of nodes where each node stores data and one or more references to other nodes.

Unlike an array, nodes do not need to occupy contiguous memory.

```text
┌───────┐      ┌───────┐      ┌───────┐
│ Data  │ ───→ │ Data  │ ───→ │ Data  │ ───→ None
└───────┘      └───────┘      └───────┘
   Node 1         Node 2         Node 3
```

### Types

- Singly Linked List
- Doubly Linked List
- Circular Linked List

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Complexity

| Operation | Complexity |
|---|---:|
| Access by index | `O(n)` |
| Search | `O(n)` |
| Insert at head | `O(1)` |
| Delete at head | `O(1)` |
| Insert after known node | `O(1)` |
| Delete with required predecessor/node reference | `O(1)`* |

> `*` The exact deletion complexity depends on the linked-list type and what references are already available.

### Strengths

- Efficient local insertion and deletion.
- Dynamic size.
- Does not require contiguous storage.

### Weaknesses

- No direct index access.
- Additional memory is required for links.
- Poorer cache locality than arrays.
- More pointer/reference management.

### Best Use Cases

- Frequent local insertions/deletions.
- Implementing linked structures.
- Learning pointer/reference-based techniques.

---

## 4.3 Stack

### Definition

A **stack** is a linear data structure that follows **LIFO (Last In, First Out)**.

The most recently inserted element is the first element removed.

```text
        ┌─────┐
        │ 30  │ ← Top
        ├─────┤
        │ 20  │
        ├─────┤
        │ 10  │
        └─────┘
           ↑
       Push / Pop
```

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

top = stack.pop()  # 30
```

### Complexity

| Operation | Complexity |
|---|---:|
| Push | `O(1)` amortized |
| Pop | `O(1)` |
| Peek | `O(1)` |
| Search | `O(n)` |

### Strengths

- Fast push and pop.
- Simple implementation.
- Natural fit for nested and backtracking problems.

### Weaknesses

- Access is restricted to the top.
- Random access is not its intended use.
- Searching requires traversal.

### Best Use Cases

- DFS
- Backtracking
- Undo/redo
- Parentheses matching
- Expression evaluation
- Call-stack concepts

---

## 4.4 Queue

### Definition

A **queue** is a linear data structure that follows **FIFO (First In, First Out)**.

The first element inserted is the first element removed.

```text
Enqueue →  ┌────┬────┬────┬────┐  → Dequeue
           │ 10 │ 20 │ 30 │ 40 │
           └────┴────┴────┴────┘
             Front          Rear
```

In Python, `collections.deque` is the standard choice for efficient insertion and removal from both ends.

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)

first = queue.popleft()  # 10
```

### Complexity

| Operation | Complexity |
|---|---:|
| Enqueue | `O(1)` |
| Dequeue | `O(1)` |
| Peek | `O(1)` |
| Search | `O(n)` |

### Strengths

- Efficient FIFO processing.
- Constant-time operations at the appropriate ends.
- Natural fit for level-order processing.

### Weaknesses

- Restricted access.
- Random access is not the primary use case.
- Searching is `O(n)`.

### Best Use Cases

- BFS
- Task scheduling
- Request processing
- Buffers
- Producer-consumer systems

---

## 4.5 Deque

### Definition

A **deque (double-ended queue)** allows elements to be inserted and removed efficiently from **both the front and the rear**.

```text
        Front                    Rear
          ↓                       ↓
      ┌────┬────┬────┬────┐
      │ 10 │ 20 │ 30 │ 40 │
      └────┴────┴────┴────┘
       ↕                       ↕
     appendleft()          append()
     popleft()             pop()
```

Python provides `collections.deque`.

### Complexity

| Operation | Complexity |
|---|---:|
| Append right | `O(1)` |
| Append left | `O(1)` |
| Pop right | `O(1)` |
| Pop left | `O(1)` |
| Search | `O(n)` |

### Strengths

- Efficient operations at both ends.
- More flexible than a traditional queue.
- Useful for sliding-window algorithms.

### Weaknesses

- Not designed for fast arbitrary indexing.
- Uses more structure than a simple list for some use cases.

### Best Use Cases

- Sliding window
- BFS
- Queues
- Monotonic queue patterns

---

# 5. Hash-Based Data Structures

## 5.1 Hash Table

### Definition

A **hash table** stores data using keys and maps each key to an associated value.

A hash function converts a key into a hash value, which is used to determine where the entry is stored.

```text
Key
 ↓
Hash Function
 ↓
Hash Value
 ↓
Table Location
 ↓
Value
```

Python's `dict` is a hash-table-based mapping.

```python
student = {
    "name": "Harshul",
    "age": 26
}

print(student["name"])
```

### Complexity

| Operation | Average | Worst |
|---|---:|---:|
| Search | `O(1)` | `O(n)` |
| Insert | `O(1)` | `O(n)` |
| Delete | `O(1)` | `O(n)` |

### Strengths

- Fast average-case lookup.
- Fast insertion and deletion.
- Excellent for key-value relationships.
- Useful for counting, caching, and membership checks.

### Weaknesses

- Requires additional memory.
- Does not provide sorted-order operations.
- Worst-case behavior can degrade to `O(n)`.

### Python Note

Modern Python dictionaries preserve **insertion order**, but they should still be chosen primarily for their mapping semantics rather than as a replacement for an ordered search tree.

### Best Use Cases

- Frequency counting
- Caching
- Duplicate detection
- Lookup tables
- Two-sum and similar problems

---

## 5.2 Set

### Definition

A **set** is a collection of unique elements designed for efficient membership testing and set operations.

```python
numbers = {10, 20, 30}

print(20 in numbers)  # True
```

### Complexity

| Operation | Average | Worst |
|---|---:|---:|
| Search / Membership | `O(1)` | `O(n)` |
| Insert | `O(1)` | `O(n)` |
| Delete | `O(1)` | `O(n)` |

### Strengths

- Automatically enforces uniqueness.
- Fast average-case membership testing.
- Supports union, intersection, and difference.

### Weaknesses

- No index-based access.
- Uses additional memory.
- Elements must be hashable.

### Best Use Cases

- Duplicate detection
- Membership checks
- Removing duplicates
- Set operations

---

# 6. Tree-Based Data Structures

## 6.1 Tree

### Definition

A **tree** is a hierarchical, non-linear data structure made of nodes connected by edges.

A tree has a root and contains no cycles.

```text
             A
           /   \
          B     C
         / \     \
        D   E     F
```

### Important Terms

| Term | Meaning |
|---|---|
| **Root** | The top-most node. |
| **Parent** | A node directly above another node. |
| **Child** | A node directly below another node. |
| **Leaf** | A node with no children. |
| **Edge** | A connection between two nodes. |
| **Depth** | Number of edges from the root to a node. |
| **Height** | Number of edges on the longest downward path from a node to a leaf. |
| **Subtree** | A node and all of its descendants. |

### Strengths

- Naturally represents hierarchical data.
- Foundation for many specialized structures.
- Works well with recursive algorithms.

### Weaknesses

- Can become unbalanced depending on the tree type.
- Requires additional references between nodes.
- Traversal and modification can be more complex than arrays.

### Best Use Cases

- File systems
- Hierarchical data
- DOM structures
- Decision structures

---

## 6.2 Binary Tree

### Definition

A **binary tree** is a tree in which each node has **at most two children**, commonly called the left and right child.

A binary tree does not require its values to be sorted.

```text
          10
         /  \
        5    20
       / \
      2   7
```

### Common Traversals

- Preorder: Root → Left → Right
- Inorder: Left → Root → Right
- Postorder: Left → Right → Root
- Level Order: Level by level

### Strengths

- Simple hierarchical structure.
- Foundation for BSTs and many tree algorithms.
- Supports several useful traversal strategies.

### Weaknesses

- Searching is not automatically efficient.
- Can become highly skewed.
- Requires node references.

---

## 6.3 Binary Search Tree

### Definition

A **Binary Search Tree (BST)** is a binary tree that maintains an ordering relationship between each node and its subtrees.

For a standard BST:

```text
All values in Left Subtree < Node < All values in Right Subtree
```

Example:

```text
             50
            /  \
          30    70
         / \    / \
       20  40  60  80
```

This ordering allows search to eliminate one subtree at each comparison when the tree is reasonably balanced.

### Complexity

| Operation | Average | Worst |
|---|---:|---:|
| Search | `O(log n)` | `O(n)` |
| Insert | `O(log n)` | `O(n)` |
| Delete | `O(log n)` | `O(n)` |

### Strengths

- Maintains sorted structure.
- Inorder traversal produces sorted values.
- Efficient when the tree remains balanced.

### Weaknesses

- Can degrade to `O(n)` when skewed.
- Requires balancing for guaranteed logarithmic performance.
- More complex than arrays and hash tables.

---

## 6.4 Balanced Search Tree

### Definition

A **balanced search tree** maintains its height at `O(log n)` so that search, insertion, and deletion remain efficient.

Common examples include:

- AVL Tree
- Red-Black Tree

```text
Balanced                    Skewed

      4                         1
     / \                         \
    2   6                         2
   / \ / \                         \
  1  3 5  7                         3
```

### Complexity

| Operation | Complexity |
|---|---:|
| Search | `O(log n)` |
| Insert | `O(log n)` |
| Delete | `O(log n)` |

### Strengths

- Guaranteed logarithmic operations.
- Maintains sorted order.
- Suitable when ordered operations are important.

### Weaknesses

- More complex implementation.
- Rebalancing introduces overhead.
- Often unnecessary for simple key-based lookup.

---

## 6.5 Heap

### Definition

A **heap** is a specialized tree-based structure that maintains a priority relationship between a parent and its children.

In a **min-heap**, every parent is less than or equal to its children. The minimum element is therefore at the root.

```text
        10
       /  \
     20    30
    /  \
   40   50
```

A heap is not fully sorted.

Python's `heapq` module provides a min-heap implementation.

### Complexity

| Operation | Complexity |
|---|---:|
| Get minimum | `O(1)` |
| Insert | `O(log n)` |
| Remove minimum | `O(log n)` |
| Search arbitrary value | `O(n)` |

### Strengths

- Efficient priority-based access.
- Efficient insertion and root removal.
- Natural implementation for priority queues.

### Weaknesses

- Does not maintain a fully sorted sequence.
- Arbitrary search is `O(n)`.
- Less suitable for general ordered lookup.

### Best Use Cases

- Priority queues
- Dijkstra's algorithm
- Top-K problems
- Scheduling
- Repeated minimum/maximum selection

---

## 6.6 Trie

### Definition

A **Trie** is a tree-like structure designed to store strings by their characters.

Each path from the root represents a sequence of characters.

For example:

```text
Words:
cat
car
care

        root
          |
          c
          |
          a
         / \
        t   r
            |
            e
```

The main advantage of a Trie is efficient prefix-based operations.

### Complexity

For a string of length `L`:

| Operation | Complexity |
|---|---:|
| Search | `O(L)` |
| Insert | `O(L)` |
| Delete | `O(L)` |

### Strengths

- Excellent for prefix searches.
- Performance depends primarily on key length.
- Well suited to autocomplete.

### Weaknesses

- Can use significant memory.
- More complex than a hash table.
- Primarily useful for string-based data.

### Best Use Cases

- Autocomplete
- Spell checking
- Prefix matching
- Dictionaries
- Word-search problems

---

## 6.7 B-Tree / B+ Tree

### Definition

A **B-Tree** is a balanced multi-way search tree designed to minimize the number of storage accesses required when working with large datasets.

A **B+ Tree** stores records primarily at the leaf level and links leaf nodes, making it particularly useful for ordered range scans.

These structures are widely associated with database indexes and storage systems.

### Strengths

- Remains balanced.
- Efficient for large datasets.
- Designed for storage systems and block-based access.
- Supports efficient range queries.

### Weaknesses

- More complex than binary search trees.
- Usually unnecessary for in-memory DSA problems.
- Implementation requires careful node splitting and balancing.

### Best Use Cases

- Database indexes
- File systems
- Large on-disk datasets

---

# 7. Graph

## 7.1 Graph

### Definition

A **graph** is a collection of vertices (nodes) connected by edges.

Graphs are used when relationships between entities are more important than a strict hierarchy.

```text
       A
      / \
     B   C
     |   |
     D---E
```

Unlike a tree, a graph may contain cycles, multiple paths, directed relationships, and weighted edges.

### Types

- Directed
- Undirected
- Weighted
- Unweighted
- Cyclic
- Acyclic
- Connected
- Disconnected

### Common Representations

#### Adjacency List

Stores the neighbors of each vertex.

```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
```

Space complexity: **`O(V + E)`**

#### Adjacency Matrix

Uses a 2D matrix where each cell represents an edge relationship.

```text
    1  2  3
1   0  1  1
2   1  0  0
3   1  0  0
```

Space complexity: **`O(V²)`**

### Strengths

- Models complex relationships naturally.
- Supports many types of real-world problems.
- Flexible representation.

### Weaknesses

- Algorithms can become complex.
- Adjacency matrices can consume substantial memory.
- Performance depends heavily on representation.

### Best Use Cases

- Social networks
- Maps and navigation
- Dependencies
- Network routing
- Recommendation systems

---

# 8. Specialized Data Structures

## 8.1 Disjoint Set / Union-Find

### Definition

A **Disjoint Set Union (DSU)** maintains a collection of non-overlapping sets and supports two core operations:

- **Find** — determine which set an element belongs to.
- **Union** — merge two sets.

With **path compression** and **union by rank/size**, operations are effectively constant time in practice.

### Best Use Cases

- Connected components
- Kruskal's algorithm
- Dynamic connectivity
- Cycle detection in undirected graphs

---

## 8.2 Segment Tree

### Definition

A **Segment Tree** is a tree-based structure used to answer range queries and perform updates efficiently.

For example, instead of scanning an entire range to calculate a sum, a Segment Tree can combine precomputed information from relevant segments.

### Complexity

| Operation | Complexity |
|---|---:|
| Build | `O(n)` |
| Range Query | `O(log n)` |
| Point Update | `O(log n)` |
| Space | `O(n)` |

### Best Use Cases

- Range sum queries
- Range minimum/maximum queries
- Dynamic range updates

---

## 8.3 Fenwick Tree

### Definition

A **Fenwick Tree**, also called a **Binary Indexed Tree**, maintains cumulative information over an array while supporting efficient point updates and prefix queries.

### Complexity

| Operation | Complexity |
|---|---:|
| Build | `O(n)` |
| Prefix Query | `O(log n)` |
| Point Update | `O(log n)` |
| Space | `O(n)` |

### Best Use Cases

- Prefix sums
- Frequency counting
- Dynamic cumulative queries

---

## 8.4 Sparse Matrix

### Definition

A **sparse matrix** contains mostly zero or empty values.

Instead of storing every cell, a sparse representation stores only meaningful/non-zero entries.

```text
Dense:

0 0 5 0
0 0 0 0
2 0 0 0
0 7 0 0
```

A sparse representation stores the non-zero values and their positions.

### Strengths

- Saves memory when most values are empty.
- Can make operations on non-zero entries more efficient.

### Weaknesses

- More complex representation.
- Random access may be slower than a dense matrix.
- Not beneficial when most cells contain data.

### Best Use Cases

- Large sparse graphs
- Scientific computing
- Large grid datasets
- Machine learning workloads

---

# 9. Data Structure Comparison

| Data Structure | Access | Search | Insert | Delete | Main Strength |
|---|---:|---:|---:|---:|---|
| **Array / List** | `O(1)` | `O(n)` | `O(n)` | `O(n)` | Fast indexed access |
| **Linked List** | `O(n)` | `O(n)` | `O(1)`* | `O(1)`* | Local modifications |
| **Stack** | `O(1)`** | `O(n)` | `O(1)` | `O(1)` | LIFO |
| **Queue** | `O(1)`** | `O(n)` | `O(1)` | `O(1)` | FIFO |
| **Deque** | `O(n)`*** | `O(n)` | `O(1)` | `O(1)` | Both-end operations |
| **Hash Table** | — | `O(1)`**** | `O(1)`**** | `O(1)`**** | Fast lookup |
| **Set** | — | `O(1)`**** | `O(1)`**** | `O(1)`**** | Uniqueness |
| **Heap** | — | `O(n)` | `O(log n)` | `O(log n)` | Priority access |
| **BST** | `O(log n)`**** | `O(log n)`**** | `O(log n)`**** | `O(log n)`**** | Ordered data |
| **Balanced BST** | `O(log n)` | `O(log n)` | `O(log n)` | `O(log n)` | Guaranteed balance |
| **Trie** | — | `O(L)` | `O(L)` | `O(L)` | Prefix search |
| **Graph** | Depends | Depends | Depends | Depends | Relationships |
| **Matrix** | `O(1)` | `O(n²)` | Depends | Depends | 2D data |

> `*` Assumes the relevant node/position reference is already available.  
> `**` Refers to the primary stack/queue endpoint rather than arbitrary access.  
> `***` Deque indexing is not its primary operation; middle access can be `O(n)`.  
> `****` Average-case for hash tables; balanced/average-case assumption for BSTs.  
> `L` = length of the string/key.

---

# 10. Python Data Structure Mapping

| Concept | Common Python Implementation |
|---|---|
| Dynamic Array | `list` |
| Stack | `list` |
| Queue | `collections.deque` |
| Deque | `collections.deque` |
| Hash Table | `dict` |
| Set | `set` |
| Heap / Priority Queue | `heapq` |
| Linked List | Custom class |
| Binary Tree | Custom class |
| BST | Custom class |
| Trie | Custom class |
| Graph | `dict`, `list`, or custom class |
| Matrix | Nested `list` |
| DSU | Custom class |
| Segment Tree | Custom class |
| Fenwick Tree | Custom class |

---

# 11. Choosing the Right Data Structure

The right data structure depends primarily on the operations the problem performs most frequently.

```text
                       What do you need?
                              │
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
        Fast lookup      Ordered data      Sequential data
             │                │                │
             ↓                ↓                ↓
        Hash Table       BST / Heap       Array / List
             │
       ┌─────┴─────┐
       ↓           ↓
   Unique?      Key → Value?
       │           │
       ↓           ↓
      Set         Dict
```

### Quick Decision Guide

| Requirement | Recommended Structure |
|---|---|
| Fast index access | Array / List |
| LIFO processing | Stack |
| FIFO processing | Queue |
| Efficient operations at both ends | Deque |
| Fast key lookup | Dictionary |
| Unique elements | Set |
| Repeated minimum/maximum retrieval | Heap |
| Sorted searchable data | BST / Balanced BST |
| Prefix-based string search | Trie |
| Hierarchical data | Tree |
| Complex relationships | Graph |
| Two-dimensional data | Matrix |
| Dynamic connectivity | DSU |
| Range queries | Segment Tree |
| Prefix sums with updates | Fenwick Tree |
| Large sparse 2D data | Sparse Matrix |
| Large on-disk indexed data | B-Tree / B+ Tree |

---

# 12. Practical Selection Rules

When solving a DSA problem, ask:

1. **Do I need index-based access?**  
   → Use a list/array.

2. **Do I need fast lookup by a key?**  
   → Use a dictionary.

3. **Do I only care whether something exists?**  
   → Use a set.

4. **Do I need last-in-first-out behavior?**  
   → Use a stack.

5. **Do I need first-in-first-out behavior?**  
   → Use a queue.

6. **Do I need efficient operations at both ends?**  
   → Use a deque.

7. **Do I repeatedly need the smallest or largest element?**  
   → Use a heap.

8. **Do I need sorted data with ordered operations?**  
   → Consider a BST or balanced search tree.

9. **Do I need prefix matching?**  
   → Use a Trie.

10. **Do I need to model relationships?**  
    → Use a graph.

11. **Do I need dynamic range queries?**  
    → Consider a Segment Tree or Fenwick Tree.

12. **Do I need to maintain connected components?**  
    → Use DSU / Union-Find.

---

# 13. Key Takeaway

There is no universally best data structure.

Every structure makes certain operations efficient while introducing trade-offs elsewhere.

A strong DSA solution therefore starts with the required operations:

```text
Problem
   ↓
Identify required operations
   ↓
Estimate constraints
   ↓
Choose appropriate data structure
   ↓
Design algorithm
   ↓
Analyze Time + Space Complexity
```
