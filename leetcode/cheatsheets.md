# Cheatsheets

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Sources](#sources)
- [Theory](#theory)
  - [Trees](#trees)
  - [Graphs](#graphs)
  - [Binary](#binary)
  - [Substr/seq/set](#substrseqset)
  - [Divide & Conquer](#divide--conquer)
  - [Greedy](#greedy)
  - [Recursion](#recursion)
  - [DP](#dp)
  - [Backtracking](#backtracking)
  - [Combinations & Permutations](#combinations--permutations)
- [Patterns](#patterns)
- [Time Complexity](#time-complexity)
  - [Arrays (dynamic array/list)](#arrays-dynamic-arraylist)
  - [Strings (immutable)](#strings-immutable)
  - [Linked Lists](#linked-lists)
  - [Hash table/dictionary](#hash-tabledictionary)
  - [Set](#set)
  - [Stack](#stack)
  - [Queue](#queue)
  - [Binary tree problems (DFS/BFS)](#binary-tree-problems-dfsbfs)
  - [Binary search tree](#binary-search-tree)
  - [Heap/Priority Queue](#heappriority-queue)
  - [Binary search](#binary-search)
  - [Miscellaneous](#miscellaneous)
- [Input Sizes vs Time Complexity](#input-sizes-vs-time-complexity)
  - [n <= 10](#n--10)
  - [10 < n <= 20](#10--n--20)
  - [20 < n <= 100](#20--n--100)
  - [100 < n <= 1,000](#100--n--1000)
  - [1,000 < n < 100,000](#1000--n--100000)
  - [100,000 < n < 1,000,000](#100000--n--1000000)
  - [1,000,000 < n](#1000000--n)
- [Sorting Algorithms](#sorting-algorithms)
- [Interview Stages](#interview-stages)
  - [Stage 1: Introductions](#stage-1-introductions)
  - [Stage 2: Problem statement](#stage-2-problem-statement)
  - [Stage 3: Brainstorming DS&A](#stage-3-brainstorming-dsa)
  - [Stage 4: Implementation](#stage-4-implementation)
  - [Stage 5: Testing & debugging](#stage-5-testing--debugging)
  - [Stage 6: Explanations and follow-ups](#stage-6-explanations-and-follow-ups)
  - [Stage 7: Outro](#stage-7-outro)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Sources

* [AlgoMonster: Runtime Overview](https://algo.monster/problems/runtime_summary)
* [AlgoMonster: Templates](https://algo.monster/templates)
* [LeetCode: Code Templates](https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/)

## Theory

### Math

* bases
    * digits: `10^0 = 1`, `10^1 = 10`, `10^2 = 100`
    * twos: `2^0 = 1`, `2^1 = 2`, `2^2 = 4`
* `log`s: inverse of an exponential function
* `sum` of
    * arithmetic sequence: `(first + last) * len() / 2`
    * geometrics sequence: `first * (1-ratio^len()) / (1-ratio)`
* `mod`
```py
def mod(x, y):
    while x >= y:
        x -= y

    return x
```

### Trees

* properties
    * acyclic
    * a path exists from the root to any node
    * `n - 1` edges, where `n` is the number of nodes in the tree
    * each node has exactly one parent node with the exception of the root node
* DFS
    * recursive: using stack
    * **pre-order** traversal
    * order: LIFO
    * best for: finding nodes far away from root
    * traverse and find/create/modify/delete node
    * traverse with return value (finding max subtree, detect balanced tree)
    * two options
        * return value: passing value up from child to parent
        * identify state(s): passing value down from parent to child
* preorder traversal
    * order: root, left, right
    * the first element is always the root of the tree
* inorder traversal
    * order: left, root, right
    * elements to the left of the root are in the left subtree
    * elements to the right are in the right subtree
* postorder traversal
    * order: left, right, root
* BFS
    * iterative: using queue/deque
    * order: FIFO
    * best for: finding nodes close/closest to the root
* perfect binary tree
    * DFS: O(log n) space
    * BFS: O(n) space
* BST: no dupes allowed

### Graphs

* binary trees are directed acyclic graphs
* a graph with `n` nodes and `n-1` edges is a tree
* representations/inputs
    * array of edges
        * `[[0,1],[1,2],[2,0],[2,3]]`
        * least efficient: iterate over entire array to find neighbors
    * adjacency lists
        * directed (list): `[[1],[2],[0, 3],[]]`
        * undirected (list): `[[1],[0, 2],[1, 0, 3],[2]]`
        * undirected (dict): `{0: [1], 1: [0, 2], 2: [1, 0, 3], 3: [2]}`
        * list of outgoing edges from `i`th node
        * most convenient: convert other inputs to it
    * adjacency matrix
        * `[[0,1,0,0],[0,0,1,0],[1,0,0,1],[0,0,0,0]]`
        * 2D matrix n rows x n columns
        * if `graph[i][j] == 1`, edge from `i` to `j`
        * traversal: O(n^2)
    * matrix
        * `(row, col)` is node
        * neighbors: `(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)`
* DFS
    * recursive more common
    * O(n + e)
    * easier to implement
    * can use to detect cycles
* BFS
    * iterative more common
    * use to find shortest path from a node

### Binary

* if you don't know how to start, start by computing XOR (`^`) of input data
* OR is an operation that only adds bits, never removes them
* bitmasking
    * setting bits: use OR & shift left
    * reading bits: use AND & shift left

### Substr/seq/set

* substring/subarray
    * order matters
    * consecutive chars
    * no repetition
* subsequence
    * order matters
    * non-consecutive chars
    * a common subsequence is a sequence of letters that appears in both strings
* subset
    * order doesn't matter

### Divide & Conquer

* characteristics
    * non-overlapping subproblems
* steps
    * partition
    * merge

### Greedy

* characteristics
    * optimal substructure
    * non-overlapping subproblems

### Recursion

* base cases
* recurrence relation

### DP

* optimized recursion
```
Dynamic Programming = Recursion + Memoization
```
* if you don't know where to start: use DFS + memoization
* characteristics
    * optimal substructure
    * overlapping subproblems
* methods
    * bottom-up
        * tabulation
        * iterative
        * faster
        * less memory
        * nested loops: 1 per state variable
        * *start after* base case
    * top-down
        * optimized backtracking
        * memoization
        * recursive
        * easier to write
        * start from `n`, end at base case
* when to use
    * min cost
    * max profit
    * number of ways
    * longest possible
    * possible to reach
* state: a set of variables to sufficiently describe a scenario
* memoization
    * hash map
        * use for top-down
        * if no `functools.cache` or equivalent
    * vector
        * use for bottom-up
        * faster than hash map
        * but more memory: may not need every state
    * built-in: `functools.cache`
        * use for top-down
* multidimensional DP
    * 1: index along input (same as 1DP), `d(i)` or `d[i]`
    * 2: 2nd index state variable to track subseq of same input, `d(i, j)` or `d[i][j]`
    * 3: numerical constraint, e.g. `k` transactions
    * 4: `true`/`false` status in given state
    * 5: tuple/bitmask to indicate visited/seen
* time complexity: `O(n*F)`
    * `n`: possible states
    * `F`: computing each state
* space complexity: usually equal to time complexity
* strategy
  1. Start with the recursive backtracking solution
  2. Optimize by using a memoization table (top-down dynamic programming)
  3. Remove the need for recursion (bottom-up dynamic programming)
  4. Apply final tricks to reduce the time / memory complexity

### Backtracking

* brute-force
* optimization on exhaustive search
    * exhaustive search: generate all possibilities, then check for solutions
    * backtracking: prune paths that cannot lead to solution, generating fewer possibilities
* usually `O(2^n)`
* implemented using recursion (almost always)
* `backtracking = dfs(tree)`
* `backtracking + memoization = DP`
* construct tree
* complexity
    * run-time: `O(total nodes) ~ O(# of children^h)`
    * space: `O(h)`

### Combinations & Permutations

TODO

## Patterns

* **Prefix Sum**: Ideal for quick range sum queries on static arrays
* **Sliding Window**: Better for problems involving contiguous subarrays with specific conditions or sizes (e.g., maximum sum of subarrays of size 'k')

|Keyword|Algorithm|
|-------|---------|
|Top K|Heap|
|How many ways|DFS, DP|
|Substring|Sliding window|
|Palindrome|Two pointers, DFS, DP|
|Tree|BFS (shortest, level), DFS|
|Parentheses|Stack|
|Subarray|Sliding window, Prefix sum, Hashmap|
|Max subarray|Greedy|
|[N]Sum|Two pointers|
|Max/longest seq|DP, DFS, mono stack|
|Min/shortest|DP, DFS, BFS|
|Partition/split array/string|DFS|
|Subseq|DP, DFS, Sliding window|
|Matrix|BFS, DFS, DP|
|Jump|Greedy, DP|
|Game|DP|
|Connected component, Cut/remove, Regions/groups/connections|Union Find|
|Transitive relationship|BFS, Union Find|
|Interval|Greedy|

## Time Complexity

* in-place != `O(1)`: if using recursion, space can be `O(n)` or `O(log n)`
* `O(1)`: constant
    * Hashmap lookup
    * Array access and update
    * Pushing and popping elements from a stack
    * Finding and applying math formula
    * Typically for `n > 10^9`
* `O(log n)`: logarithmic
    * assumed `log_2(n)`: log base 2 of n
    * Binary search or variant
    * Balanced binary search tree lookup
    * Processing the digits of a number
    * Typically for `n > 10^8`
* `O(n)`: linear
    * Going through array/linked list
    * Two pointers
    * Some types of greedy
    * Tree/graph traversal
    * Stack/Queue
    * Typically for `n <= 10^6`
* `O(k*log n)`
    * Heap push/pop K times
    * "top K elements"
    * Binary search K times
    * Typically for `n <= 10^6`
* `O(n*log n)`
    * Sorting
    * Divide and conquer with a linear time merge operation
        * divide is normally `O(log n)`
        * merge is `O(n)`
    * Typically for `n <= 10^6`
* `O(n^2)`: quadratic
    * Nested loops, e.g., visiting each matrix entry
    * Many brute force solutions
    * Typically for `n <= 3000`
* `O(2^n)`: exponential
    * grows very rapidly
    * requires memoization
    * Combinatorial problems, backtracking, e.g. subsets
    * Often involves recursion and is harder to analyze time complexity
    * Typically for `n <= 20`
* `O(n!)`: factorial
    * Combinatorial problems, backtracking, e.g. permutations
    * Often involves recursion and is harder to analyze time complexity
    * Typically for `n <= 12`

### Arrays (dynamic array/list)

Given `n = len(arr)`

* Add or remove element at the end: `O(1)` amortized
* Add or remove element from arbitrary index: `O(n)`
* Access or modify element at arbitrary index: `O(1)`
* Check if element exists: `O(n)`
* Two pointers: `O(n*k)`, where `k` is the work done at each iteration, includes
  sliding window
* Building a prefix sum: `O(n)`
* Finding the sum of a subarray given a prefix sum: `O(1)`

### Strings (immutable)

Given `n = len(s)`

* Add or remove character: `O(n)`
* Access element at arbitrary index: `O(1)`
* Concatenation between two strings: `O(n+m)`, where `m` is the length of the
  other string
* Create substring: `O(m)`, where `m` is the length of the substring
* Two pointers: `O(n*k)`, where `k` is the work done at each iteration, includes
  sliding window
* Building a string from joining an array, stringbuilder, etc.: `O(n)`

### Linked Lists

Given `n` as the number of nodes in the linked list,

* Add or remove element given pointer before add/removal location: `O(1)`
* Add or remove element given pointer at add/removal location: `O(1)` if doubly
  linked
* Add or remove element at arbitrary position without pointer: `O(n)`
* Access element at arbitrary position without pointer: `O(n)`
* Check if element exists: `O(n)`
* Reverse between position `i` and `j`: `O(j−i)`
* Detect a cycle: `O(n)` using fast-slow pointers or hash map

### Hash table/dictionary

Given `n = len(dict)`

* Add or remove key-value pair: `O(1)`
* Check if key exists: `O(1)`
* Check if value exists: `O(n)`
* Access or modify value associated with key: `O(1)`
* Iterate over all keys, values, or both: `O(n)`

> Note: the `O(1)` operations are constant relative to `n`. In reality, the
> hashing algorithm might be expensive. For example, if your keys are strings,
> then it will cost `O(m)` where `m` is the length of the string. The operations
> only take constant time relative to the size of the hash map.

### Set

Given `n = len(set)`

* Add or remove element: `O(1)`
* Check if element exists: `O(1)`

> The above note applies here as well.

### Stack

Stack operations are dependent on their implementation. A stack is only required
to support pop and push. If implemented with a dynamic array:

Given `n = len(stack)`

* Push element: `O(1)`
* Pop element: `O(1)`
* Peek (see element at top of stack): `O(1)`
* Access or modify element at arbitrary index: `O(1)`
* Check if element exists: `O(n)`

### Queue

Queue operations are dependent on their implementation. A queue is only required
to support dequeue and enqueue. If implemented with a doubly linked list:

Given `n = len(queue)`

* Enqueue element: `O(1)`
* Dequeue element: `O(1)`
* Peek (see element at front of queue): `O(1)`
* Access or modify element at arbitrary index: `O(n)`
* Check if element exists: `O(n)`

> Note: most programming languages implement queues in a more sophisticated
> manner than a simple doubly linked list. Depending on implementation, accessing
> elements by index may be faster than `O(n)`, or `O(n)` but with a significant
> constant divisor.

### Binary tree problems (DFS/BFS)

Given `n` as the number of nodes in the tree,

Most algorithms will run in `O(n*k)` time, where `k` is the work done at each
node, usually `O(1)`. This is just a general rule and not always the case. We
are assuming here that BFS is implemented with an efficient queue.

### Binary search tree

Given `n` as the number of nodes in the tree,

* Add or remove element: `O(n)` worst case, `O(log n)` average case
* Check if element exists: `O(n)` worst case, `O(log n)` average case

The average case is when the tree is well balanced - each depth is close to
full. The worst case is when the tree is just a straight line.

### Heap/Priority Queue

Given `n = len(heap)` and talking about min heaps,

* Add an element: `O(log n)`
* Delete the minimum element: `O(log n)`
* Find the minimum element: `O(1)`
* Check if element exists: `O(n)`

### Binary search

Binary search runs in `O(log n)` in the worst case, where `n` is the size of
your initial search space.

### Miscellaneous

* Sorting: `O(n*log n)`, where `n` is the size of the data being sorted
* DFS and BFS on a graph: `O(n*k+e)`, where `n` is the number of nodes, `e` is
  the number of edges, if each node is handled in `O(1)` other than iterating
  over edges
* DFS and BFS space complexity: typically `O(n)`, but if it's in a graph, might
  be `O(n+e)` to store the graph
* Dynamic programming time complexity: `O(n*k)`, where `n` is the number of
  states and `k` is the work done at each state
* Dynamic programming space complexity: `O(n)`, where `n` is the number of states

## Input Sizes vs Time Complexity

The constraints of a problem can be considered as hints because they indicate an
upper bound on what your solution's time complexity should be. Being able to
figure out the expected time complexity of a solution given the input size is a
valuable skill to have. In all LeetCode problems and most online assessments
(OA), you will be given the problem's constraints. Unfortunately, you will
usually not be explicitly told the constraints of a problem in an interview, but
it's still good for practicing on LeetCode and completing OAs. Still, in an
interview, it usually doesn't hurt to ask about the expected input sizes.

### n <= 10

The expected time complexity likely has a factorial or an exponential with a
base larger than `2`: `O(n^2 ⋅n!)` or `O(4^n)` for example.

You should think about *backtracking* or any *brute-force-esque recursive
algorithm*. `n <= 10` is extremely small and usually any algorithm that correctly
finds the answer will be fast enough.

### 10 < n <= 20

The expected time complexity likely involves `O(2^n)`. Any higher base or a
factorial will be too slow (`3^20 = ~3.5 billion`, and `20!` is much larger). A
`2^n` usually implies that given a collection of elements, you are considering
all subsets/subsequences - for each element, there are two choices: take it or
don't take it.

Again, this bound is very small, so most algorithms that are correct will
probably be fast enough. Consider *backtracking* and *recursion*.

### 20 < n <= 100

At this point, exponentials will be too slow. The upper bound will likely
involve `O(n^3)`.

Problems marked as "easy" on LeetCode usually have this bound, which can be
deceiving. There may be solutions that run in `O(n)`, but the small bound allows
brute force solutions to pass (finding the linear time solution might not be
considered as "easy").

Consider *brute force* solutions that involve nested loops. If you come up with a
brute force solution, try analyzing the algorithm to find what steps are "slow",
and try to improve on those steps using tools like hash maps or heaps.

### 100 < n <= 1,000

In this range, a quadratic time complexity `O(n^2)` should be sufficient, as long
as the constant factor isn't too large.

Similar to the previous range, you should consider *nested loops*. The difference
between this range and the previous one is that `O(n^2)` is usually the
expected/optimal time complexity in this range, and it might not be possible to
improve.

### 1,000 < n < 100,000

`n <= 10^5` is the most common constraint you will see on LeetCode. In this
range, the slowest acceptable common time complexity is `O(n*log n)`, although a
linear time approach `O(n)` is commonly the goal.

In this range, ask yourself if *sorting* the input or using a *heap* can be helpful.
If not, then aim for an `O(n)` algorithm. Nested loops that run in `O(n^2)` are
unacceptable - you will probably need to make use of a technique learned in this
course to simulate a nested loop's behavior in `O(1)` or `O(log n)`:

* Hash map
* A two pointers implementation like sliding window
* Monotonic stack
* Binary search
* Heap
* A combination of any of the above

If you have an `O(n)` algorithm, the constant factor can be reasonably large
(around 40). One common theme for string problems involves looping over the
characters of the alphabet at each iteration resulting in a time complexity of
`O(26*n)`.

### 100,000 < n < 1,000,000

`n <= 10^6` is a rare constraint, and will likely require a time complexity of
`O(n)`.  In this range, `O(n*log n)` is usually safe as long as it has a small
constant factor. You will very likely need to incorporate a *hash map* in some
way.

### 1,000,000 < n

With huge inputs, typically in the range of `10^9` or more, the most common
acceptable time complexity will be logarithmic `O(log n)` or constant `O(1)`. In
these problems, you must either significantly reduce your search space at each
iteration (usually *binary search*) or use clever tricks to find information in
constant time (like with math or a clever use of hash maps).

Other time complexities are possible like `O(sqrt(n))`, but this is very rare
and will usually only be seen in very advanced problems.

## Sorting Algorithms

All major programming languages have a built-in method for sorting. It is
usually correct to assume and say sorting costs `O(n*log n)`, where n is the
number of elements being sorted. For completeness, here is a chart that lists
many common sorting algorithms and their completeness. The algorithm implemented
by a programming language varies; for example, Python uses Timsort but in C++,
the specific algorithm is not mandated and varies.

Definition of a stable sort from Wikipedia: "Stable sorting algorithms maintain
the relative order of records with equal keys (i.e. values). That is, a sorting
algorithm is stable if whenever there are two records R and S with the same key
and with R appearing before S in the original list, R will appear before S in
the sorted list."

## Interview Stages

The following will be a summary of the "Stages of an interview" article. If you
have a remote interview, you can print this condensed version and keep it in
front of you during the interview.

### Stage 1: Introductions

* Have a rehearsed 30-60 second introduction regarding your education, work
  experience, and interests prepared.
* Smile and speak with confidence.
* Pay attention when the interviewer talks about themselves and incorporate
  their work into your questions later.

### Stage 2: Problem statement

* Paraphrase the problem back to the interviewer after they have read it to you.
* Ask clarifying questions about the input such as the expected input size, edge
  cases, and invalid inputs.
* Quickly walk through an example test case to confirm you understand the
  problem.

### Stage 3: Brainstorming DS&A

* Always be thinking out loud.
* Break the problem down: figure out what you need to do, and think about what
  data structure or algorithm can accomplish it with a good time complexity.
* Be receptive to any comments or feedback from the interviewer, they are
  probably trying to hint you towards the correct solution.
* Once you have an idea, before coding, explain your idea to the interviewer and
  make sure they understand and agree that it is a reasonable approach.

### Stage 4: Implementation

* Explain your decision-making as you implement. When you declare things like
  sets, explain what the purpose is.
* Write clean code that conforms to your programming language's conventions.
* Avoid writing duplicate code - use a helper function or for loop if you are
  writing similar code multiple times.
* If you are stuck, don't panic - communicate your concerns with your
  interviewer.
* Don't be scared to start with a brute force solution (while acknowledging that
  it is brute force), then improve it by optimizing the "slow" parts.
* Keep thinking out loud and talk with your interviewer. It makes it easier for
  them to give you hints.

### Stage 5: Testing & debugging

* When walking through test cases, keep track of the variables by writing at the
  bottom of the file, and continuously update them. Condense trivial parts like
  creating a prefix sum to save time.
* If there are errors and the environment supports running code, put print
  statements in your algorithm and walk through a small test case, comparing the
  expected value of variables and the actual values.
* Be vocal and keep talking with your interviewer if you run into any problems.

### Stage 6: Explanations and follow-ups

Questions you should be prepared to answer:

* Time and space complexity, average and worst case.
* Why did you choose this data structure, algorithm, or logic?
* Do you think the algorithm could be improved in terms of complexity? If they
  ask you this, then the answer is usually yes, especially if your algorithm is
  slower than O(n).

### Stage 7: Outro

* Have questions regarding the company prepared.
* Be interested, smile, and ask follow-up questions to your interviewer's
  responses.
