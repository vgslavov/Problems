# Algorithm Templates (Python)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Sources](#sources)
- [Imports](#imports)
- [Two Pointers](#two-pointers)
  - [One Input, Opposite Direction](#one-input-opposite-direction)
  - [One Input, Same Direction](#one-input-same-direction)
  - [Two Inputs, Exhaust Both](#two-inputs-exhaust-both)
  - [Opposite Direction (Two Sum)](#opposite-direction-two-sum)
- [Divide & Conquer](#divide--conquer)
  - [Recursive Stable Merge Sort](#recursive-stable-merge-sort)
- [Deduplication](#deduplication)
  - [Sort + Two Pointers](#sort--two-pointers)
- [Kadane's Algorithm](#kadanes-algorithm)
  - [Maximum Subarray Sum](#maximum-subarray-sum)
  - [Explicit Sliding Window](#explicit-sliding-window)
- [Sliding Window](#sliding-window)
  - [Longest](#longest)
  - [Shortest](#shortest)
  - [Fixed](#fixed)
- [Prefix Sum](#prefix-sum)
  - [Build a Diff Array](#build-a-diff-array)
  - [Build a Prefix Sum: Pythonic](#build-a-prefix-sum-pythonic)
  - [Build a Prefix Sum](#build-a-prefix-sum)
  - [Build a Prefix Sum for Range Queries](#build-a-prefix-sum-for-range-queries)
  - [Query Sum of Range Using Prefix Sum](#query-sum-of-range-using-prefix-sum)
- [Recursive vs Iterative](#recursive-vs-iterative)
  - [Recursive](#recursive)
  - [Iterative](#iterative)
  - [Iterative: Stack](#iterative-stack)
- [String Building](#string-building)
  - [Efficient String Building](#efficient-string-building)
- [Linked Lists](#linked-lists)
  - [Definition for Singly-Linked List](#definition-for-singly-linked-list)
  - [Fast & Slow Pointer](#fast--slow-pointer)
  - [Fast & Slow K Apart](#fast--slow-k-apart)
  - [Dummy Nodes](#dummy-nodes)
  - [Reversing a Linked List](#reversing-a-linked-list)
- [Subarrays](#subarrays)
  - [Find Number of Subarrays That Fit an Exact Criteria](#find-number-of-subarrays-that-fit-an-exact-criteria)
- [Monotonic Stack/Queue](#monotonic-stackqueue)
  - [Monotonic Increasing Stack/Queue](#monotonic-increasing-stackqueue)
  - [Monotonic Increasing/Decreasing Sliding Window Using Heap](#monotonic-increasingdecreasing-sliding-window-using-heap)
  - [Monotonic Increasing/Decreasing Sliding Window Using Deque](#monotonic-increasingdecreasing-sliding-window-using-deque)
- [Intervals](#intervals)
  - [Merge Intervals](#merge-intervals)
- [Binary Search Trees](#binary-search-trees)
  - [BST: Find](#bst-find)
  - [BST: Insert](#bst-insert)
- [Binary Trees](#binary-trees)
  - [Recursive DFS](#recursive-dfs)
  - [Iterative DFS](#iterative-dfs)
  - [Iterative BFS](#iterative-bfs)
- [Graphs](#graphs)
  - [Build Adjacency List/Dict](#build-adjacency-listdict)
  - [Recursive DFS](#recursive-dfs-1)
  - [Iterative DFS](#iterative-dfs-1)
  - [Iterative BFS](#iterative-bfs-1)
  - [Topological Sort (ala BFS)](#topological-sort-ala-bfs)
- [Heaps](#heaps)
  - [Find Top K Elements with Heap](#find-top-k-elements-with-heap)
- [Binary Search](#binary-search)
  - [Pythonic `bisect`, Ascending Sorted Only!](#pythonic-bisect-ascending-sorted-only)
  - [Manual](#manual)
  - [Feasible Conditions](#feasible-conditions)
  - [Duplicate Elements, Left-Most Insertion Point](#duplicate-elements-left-most-insertion-point)
  - [Duplicate Elements, Right-Most Insertion Point](#duplicate-elements-right-most-insertion-point)
  - [Find Min (For Greedy Problems)](#find-min-for-greedy-problems)
  - [Find Max](#find-max)
- [Backtracking](#backtracking)
  - [Basic Pruning](#basic-pruning)
  - [Aggregation](#aggregation)
  - [Permutations](#permutations)
  - [Combinations](#combinations)
- [Dynamic Programming](#dynamic-programming)
  - [DP: Recursive Top-Down Memoization](#dp-recursive-top-down-memoization)
  - [DP: Iterative Bottom-Up 1D](#dp-iterative-bottom-up-1d)
- [Tries](#tries)
  - [Build a Trie](#build-a-trie)
  - [Insert & Search](#insert--search)
- [Shortest Path](#shortest-path)
  - [Dijkstra's Algorithm](#dijkstras-algorithm)
- [Union-Find](#union-find)
  - [DSU (Disjoint Set Union)](#dsu-disjoint-set-union)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

## Sources

- [LeetCode: Code Templates](https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/)
- [AlgoMonster: Templates](https://algo.monster/templates)
- [NeetCode](https://neetcode.io/)

---

## Imports

```python
import bisect
from collections import defaultdict
from collections import deque
from functools import cache
from itertools import accumulate
import heapq
import math
```

---

## Two Pointers

### One Input, Opposite Direction

```python
def condition(a, b):
    # define the condition for two pointers
    return a < b

def two_pointers_opposite(arr):
    left = ans = 0
    right = len(arr) - 1

    while left < right:
        # do logic with left and right

        if condition(arr[left], arr[right]):
            left += 1
        else:
            right -= 1

    return ans
```

### One Input, Same Direction

```python
def two_pointers_same(arr):
    slow, fast = 0, 0

    while fast < len(arr):
        # do logic with slow and fast

        # Slow pointer only moves if condition is true
        if condition(arr[slow], arr[fast]):
            slow += 1

        # Fast pointer *always* moves forward
        fast += 1
```

### Two Inputs, Exhaust Both

```python
def two_pointers(arr1, arr2):
    i = j = ans = 0

    while i < len(arr1) and j < len(arr2):
        # do some logic here
        if condition(arr1[i], arr2[j]):
            i += 1
        else:
            j += 1

    while i < len(arr1):
        # do logic
        i += 1

    while j < len(arr2):
        # do logic
        j += 1

    return ans
```

### Opposite Direction (Two Sum)

**Run-time:** O(n)  
**Space:** O(1)

```python
def two_sum(nums, left, right, target):
    # assumes nums is sorted
    ans = []

    while left < right:
        cur_sum = nums[left] + nums[right]
        if cur_sum == target:
            ans.append([nums[left], nums[right]])
            # skip dupes
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            left += 1
            right -= 1
        elif cur_sum < target:
            left += 1
        else:
            right -= 1

    return ans
```

---

## Divide & Conquer

### Recursive Stable Merge Sort

```python
def merge_sort(arr):
    # base case
    if len(arr) < 2:
        return arr

    # 1. the divide step: split array into two components
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 2. the merging (conquer) step: combine two components to get the final result
    l, r, result = 0, 0, []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    
    # Add remaining elements
    while l < len(left):
        result.append(left[l])
        l += 1
    
    while r < len(right):
        result.append(right[r])
        r += 1

    return result
```

---

## Deduplication

### Sort + Two Pointers

**Run-time:** O(n*log n) + O(n^2) ~ O(n^2)  
**Space:** O(1)

```python
def three_sum(nums, target):
    nums.sort()
    ans = []
    for i in range(len(nums)):
        # skip duplicate inputs
        if i > 0 and nums[i-1] == nums[i]: continue

        # nums[i] + nums[j] + nums[k] = target
        # nums[i] is fixed, find pairs that sum to target - nums[i]
        # nums is sorted: nums[i] <= nums[j] <= nums[k]

        # restrict two_sum's search interval
        tuples = two_sum(nums, i+1, len(nums)-1, target-nums[i])
        # slicing creates new list: O(n) space
        #tuples = two_sum(nums[i+1:], target - nums[i])
        for t in tuples:
            ans.append((nums[i], t[0], t[1]))

    return ans
```

---

## Kadane's Algorithm

### Maximum Subarray Sum

```python
def max_subarray(nums):
    max_sum = -math.inf
    curr_sum = 0

    for n in nums:
        curr_sum = max(curr_sum, 0)
        curr_sum += n
        # or
        #curr_sum = max(curr_sum+n, n)

        max_sum = max(max_sum, curr_sum)

    return max_sum
```

### Explicit Sliding Window

```python
def max_subarray_sliding(nums):
    max_sum = -math.inf
    curr_sum = 0
    left = 0
    max_left, max_right = 0, 0

    for right in range(len(nums)):
        # negative sum: reset current sum & slide window
        if curr_sum < 0:
            curr_sum = 0
            left = right

        curr_sum += nums[right]

        # found new max
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_left, max_right = left, right

    return [max_left, max_right]
```

---

## Sliding Window

### Longest

```python
SOME_THRESHOLD = 10  # Example threshold, adjust as needed

def invalid_condition(curr):
    # define the condition for the sliding window to be invalid
    return curr > SOME_THRESHOLD

def sliding_window_longest(arr):
    left = ans = win_sum = 0

    for right in range(len(arr)):
        win_sum += arr[right]

        # update left until window is valid again
        while invalid_condition(win_sum):
            win_sum -= arr[left]
            left += 1

        # window is guaranteed to be valid here
        ans = max(ans, right-left+1)

    return ans
```

### Shortest

```python
SOME_THRESHOLD = 10  # Example threshold, adjust as needed

def valid_condition(curr):
    # define the condition for the sliding window to be valid
    return curr >= SOME_THRESHOLD

def sliding_window_shortest(arr):
    left = win_sum = 0
    ans = len(arr)

    for right in range(len(arr)):
        win_sum += arr[right]

        while valid_condition(win_sum):
            # window is guaranteed to be valid here
            ans = min(ans, right-left+1)

            win_sum -= arr[left]
            left += 1

    return ans
```

### Fixed

```python
def sliding_window_fixed(arr, k):
    ans = 0

    # 1st window
    # works for k > len(arr)
    #ans = sum(arr[:k])
    for i in range(min(k, len(arr))):
        ans += arr[i]

    # start at k
    for right in range(k, len(arr)):
        left = right - k
        curr -= arr[left]
        curr += arr[right]
        ans = max(ans, curr)

    return ans
```

---

## Prefix Sum

### Build a Diff Array

```python
def diff_array(arr, shifts):
    diff = [0] * len(arr)

    for start, end in shifts:
        diff[start] += 1
        # if inclusive
        if end + 1 < len(diff):
            diff[end + 1] -= 1

    return diff
```

### Build a Prefix Sum: Pythonic

```python
def prefix_sum_accumulate(arr):
    return list(accumulate(arr))
```

### Build a Prefix Sum

```python
def prefix_sum(arr):
    prefix = [arr[0]]
    # or preallocate
    #prefix = [0] * len(arr)

    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
        #prefix[i] = prefix[i-1] + arr[i]

    return prefix
```

### Build a Prefix Sum for Range Queries

```python
def prefix_sum_range(arr, left, right):
    # init first element to 0 if you need to do range sum queries
    prefix = [0, arr[0]]

    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])

    return prefix[right+1]-prefix[left]
```

### Query Sum of Range Using Prefix Sum

```python
def query_prefix_sum(prefix, left, right):
    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]
```

---

## Recursive vs Iterative

### Recursive

```python
def factorial(n):
    # base case
    if n <= 1:
        return 1

    # recursive call
    return n * factorial(n - 1)
```

### Iterative

```python
def factorial_iterative(n):
    ans = 1

    for i in range(2, n + 1):
        ans *= i

    return ans
```

### Iterative: Stack

```python
def factorial_stack(n):
    stack = []

    # push each call to a stack
    # top of the stack is base case
    while n > 0:
        stack.append(n)
        n -= 1

    ans = 1
    # pop and use return value until stack is empty
    while stack:
        ans *= stack.pop()

    return ans
```

---

## String Building

### Efficient String Building

```python
# arr is a list of characters
def string(arr):
    #return ''.join(c for c in arr)
    return ''.join(arr)
```

---

## Linked Lists

### Definition for Singly-Linked List

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Fast & Slow Pointer

**Traversing:** iteratively more common

```python
def fn(head):
    slow = head
    fast = head
    ans = 0

    while fast and fast.next:
        # do logic
        slow = slow.next
        fast = fast.next.next

    return ans
```

### Fast & Slow K Apart

```python
def fn(head, k):
    slow = head
    fast = head

    while fast and k:
        fast = fast.next
        k -= 1

    while fast:
        # do logic
        slow = slow.next
        fast = fast.next

    return slow
```

### Dummy Nodes

```python
def fn(head):
    dummy = ListNode(0, head)
    fast = slow = dummy

    # move fast pointer k ahead

    while fast.next:
        slow = slow.next
        fast = fast.next

    # do something

    return dummy.next
```

### Reversing a Linked List

```python
def reverse(head):
    prev = None

    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev
```

---

## Subarrays

### Find Number of Subarrays That Fit an Exact Criteria

```python
def fn(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1

    return ans
```

---

## Monotonic Stack/Queue

### Monotonic Increasing Stack/Queue

**Run-time:** O(n)  
**Space:** O(n)

```python
def mono_stack(arr):
    stack = []
    ans = 0

    for num in arr:
        # for monotonic decreasing, just flip the > to <
        while stack and stack[-1] > num:
            # do logic
            stack.pop()

        stack.append(num)

    return ans
```

### Monotonic Increasing/Decreasing Sliding Window Using Heap

**Run-time:** O(n*log k)  
**Space:** O(k)

```python
def mono_heap(arr, k):
    heap = []
    left = 0
    ans = []

    for right in range(len(arr)):
        # max heap: value, index
        heapq.heappush(heap, (-arr[right], right))

        # reached window size
        if right >= k - 1:
            # pop all indices outside window
            while heap[0][1] < left:
                heapq.heappop(heap)

            # window max
            ans.append(-heap[0][0])

            # slide window
            left += 1

    return ans
```

### Monotonic Increasing/Decreasing Sliding Window Using Deque

**Run-time:** O(n)  
**Space:** O(k)

```python
def mono_deque(arr, k):
    dq = deque()
    ans = []

    for i in range(len(arr)):
        # 1. remove elements not in the window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # 2. remove smaller elements:
        # monotonically decreasing
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # 3. add to deque
        dq.append(i)

        # reached window size
        if i >= k - 1:
            ans.append(arr[dq[0]])

    return ans
```

```py
# n reqs/sec
def mono_deque2(arr, size, duration):
    win = deque()
    ans = []

    for a in arr:
        # 1. shink window: evict older entries
        while win and a - win[0] >= duration:
            win.popleft()

        # 2. expand window
        if len(win) < size:
            win.append(a)

            # do stuff

            # process
            ans.append(True)
        else:
            # reject
            ans.append(False)

    return ans

```

---

## Intervals

### Merge Intervals

```python
def overlap(x, y):
    # if end/start cannot overlap
    return max(x[0], y[0]) <= min(x[1], y[1])

    # if end/start can overlap
    #return max(x[0], y[0]) < min(x[1], y[1])

    # 2nd interval starts before 1st ends and vice versa
    #return not (x[1] < y[0] or y[1] < x[0])

    # if inclusive: [1, 5], [5, 6] not considered overlapping
    #return not (x[1] <= y[0] or y[1] <= x[0])

def merge_intervals(intervals):
    # sort by start time
    intervals.sort()
    ans = []

    #for i in range(1, len(intervals)):
    for start, end in intervals:
        # merge
        #if overlap(intervals[i-1], intervals[i]):
        if ans and overlap(ans[-1], [start, end]):
            ans[-1][1] = max(ans[-1][1], end)
        else:
            ans.append([start,end])

    return ans
```

---

## Binary Search Trees

### BST: Find

```python
def bst_find(tree, val):
   if not tree:
       return False

   if tree.val == val:
       return True
   elif tree.val < val:
       return bst_find(tree.right, val)
   else:
       return bst_find(tree.left, val)
```

### BST: Insert

```python
def bst_insert(tree, val):
    if not tree:
        return TreeNode(val)

    if tree.val < val:
        tree.right = bst_insert(tree.right, val)
    elif tree.val > val:
        tree.left = bst_insert(tree.left, val)
    return tree
```

---

## Binary Trees

### Recursive DFS

**Data struct:** recursion stack (LIFO), more common

```python
def dfs_tree_recursive(root, target=None):
    # base case
    if not root:
        return None

    if root.val == target:
        return root

    # preorder: order same as recursive function calls
    #print("preorder: ".format(root.val))

    # do logic
    left = dfs_tree_recursive(root.left, target)

    if left:
        return left

    # inorder: all left subtree printed before current and then right subtree
    # on BST: traversal is in sorted order
    #print("inorder: ".format(root.val))

    return dfs_tree_recursive(root.right, target)

    # postorder: root is last to be traversed
    #print("postorder: ".format(root.val))
```

### Iterative DFS

**Data struct:** recursion stack (LIFO)

```python
def dfs_tree_iterative(root, target=None):
    stack = [root]

    while stack:
        node = stack.pop()

        # do logic
        if node.val == target:
            return node

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return None
```

### Iterative BFS

**Data struct:** queue (FIFO), more common

```python
def bfs_tree_iterative(root):
    # list of root!
    queue = deque([root])
    ans = 0

    while queue:
        n = len(queue)
        # do logic for current level

        for _ in range(n):
            # read from front
            node = queue.popleft()

            # do logic

            # add to back
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans
```

---

## Graphs

### Build Adjacency List/Dict

**Input:** array of edges  
**Output:** adjacency list/dict

```python
EDGES = [[0,1],[1,2],[2,0],[2,3]]
GRAPH = {0: [1], 1: [0, 2], 2: [1, 0, 3], 3: [2]}

def build_adjlist(edges):
    graph = defaultdict(list)

    for x,y in edges:
        graph[x].append(y)
        # if undirected graph
        graph[y].append(x)

    return graph

# basic
def get_neighbors(node):
    return GRAPH[node]
```

### Recursive DFS

**Data struct:** recursion stack (LIFO)

```python
def dfs_graph_recursive(root):
    def dfs(node):
        # do some logic
        for neighbor in get_neighbors(node):
            if neighbor in seen:
                continue

            # mark neighbor as seen
            seen.add(neighbor)
            ans += dfs(neighbor)

        return ans

    ans = 0
    seen = set([root])
    return dfs(root)
```

### Iterative DFS

**Data struct:** stack (LIFO)

```python
def dfs_graph_iterative(root):
    stack = [root]
    seen = set([root])
    ans = 0

    while stack:
        node = stack.pop()
        # do some logic

        for neighbor in get_neighbors(node):
            if neighbor in seen:
                continue

            # mark neighbor as seen
            seen.add(neighbor)
            stack.append(neighbor)

    return ans
```

### Iterative BFS

**Data struct:** queue (FIFO)  
**Input:** adjacency list/dict

```python
GRID = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 1]
]
NUM_ROWS, NUM_COLS = len(GRID), len(GRID[0])

def get_neighbors_matrix(coord):
    row, col = coord
    # go up, right, down, left:
    # previous row, same row, next row, same row
    delta_row = [-1, 0, 1, 0]
    # same col, next col, same col, previous col
    delta_col = [0, 1, 0, -1]
    #ans = []

    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]

        if 0 <= neighbor_row < NUM_ROWS and 0 <= neighbor_col < NUM_COLS:
            # generate:
            yield (neighbor_row, neighbor_col)
            # or append to list:
            #ans.append((neighbor_row, neighbor_col))

    #return ans

def bfs_graph_iterative(root):
    queue = deque([root])
    seen = set([root])
    #seen = {root}
    level = 0

    while queue:
        n = len(queue)

        # optional: if keep track of the current level
        for _ in range(n):
            node = queue.popleft()
            # do some logic

            # for matrix
            #for neighbor in get_neighbors_matrix(node):
            for neighbor in get_neighbors(node):
                if neighbor in seen:
                    continue

                # mark neighbor as seen
                seen.add(neighbor)
                queue.append(neighbor)

        level += 1

    return level
```

### Topological Sort (ala BFS)

* run-time: O(v + e)
* space: O(v)

```python
def calc_indegree(graph):
    # init
    indegree = { node:0 for node in graph }

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    return indegree

def topo_sort(graph):
    ans = []
    queue = deque()
    indegree = calc_indegree(graph)

    # enqueue all nodes with indegree 0
    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        ans.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # if unprocessed nodes, cycle exists, no topological sort
    return ans if len(graph) == len(ans) else None
```

---

## Heaps

### Find Top K Elements with Heap

```python
CRITERIA = 0

def find_topk(arr, k):
    heap = []
    for num in arr:
        # min heap
        # do some logic to push onto heap according to problem's criteria
        heapq.heappush(heap, (CRITERIA, num))

        # max heap
        #heapq.heappush(heap, (-CRITERIA, num))

        # limit size to O(k)
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for _, num in heap]
```

---

## Binary Search

### Pythonic `bisect`, Ascending Sorted Only!

```python
def binary_search_bisect_left(arr, target):
    i = bisect.bisect_left(arr, target)
    if i < len(arr) and arr[i] == target:
        return True

    return False
```

### Manual

**Complexity:**  
**Run-time:** O(log n)  
**Space:** O(1) vs O(log n) if using recursion

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    # test for = don't miss an element!
    while left <= right:
        # prevent overflowing
        #mid = left + (right - left) // 2

        # can't overflow: Python handles large integers
        mid = (left + right) // 2

        if arr[mid] == target:
            # do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # left is the insertion point
    return left
```

### Feasible Conditions

```python
def feasible(num, target):
    # not greater
    return num <= target

    # find boundary
    #return num == target

    # not smaller
    #return num >= target

def binary_search_feasible(arr, target):
    left = 0
    right = len(arr)-1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if feasible(arr[mid], target):
            # record!
            ans = mid

            # go left or go right depending on the problem
            right = mid - 1
            #left = mid + 1
        else:
            left = mid + 1
            #right = mid - 1

    return ans
```

### Duplicate Elements, Left-Most Insertion Point

```python
def binary_search_left(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left
```

### Duplicate Elements, Right-Most Insertion Point

```python
def binary_search_right(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left
```

### Find Min (For Greedy Problems)

```python
MINIMUM_POSSIBLE_ANSWER = -math.inf
MAXIMUM_POSSIBLE_ANSWER = math.inf

def binary_search_min(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left
```

### Find Max

```python
def binary_search_max(arr):
    def check(x):
        # this function is implemented depending on the problem
        return True

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right
```

---

## Backtracking

```python
def backtrack(curr, OTHER_ARGUMENTS...):
    if BASE_CASE:
        # modify the answer
        return

    ans = 0
    for ITERATE_OVER_INPUT:
        # modify the current state
        ans += backtrack(curr, OTHER_ARGUMENTS...)
        # undo the modification of the current state

    return ans
```

### Basic Pruning

```python
def is_leaf(start_index):
    # define the base case
    return start_index == len(INPUT)

def is_valid(edge):
    # define the pruning condition
    return True

def get_edges(start_index, states):
    # define how to get edges from current state
    return EDGES

def backtrack_pruning(start_index, path, [...additional states]):
    if is_leaf(start_index):
        ans.append(path[:]) # add a copy of the path to the result
        #report(path)
        return

    for edge in get_edges(start_index, [...additional states]):
        # prune if needed
        if not is_valid(edge):
            continue

        path.add(edge)
        if additional states:
            update([...additional states])

        # increment start_index
        backtrack_pruning(start_index + len(edge), path, [...additional states])
        # revert(states) if necessary e.g. permutations
        path.pop()
```

### Aggregation

```python
def backtrack_agg(start_index, [...additional states]):
    if is_leaf(start_index):
        return 1
    ans = initial_value
    for edge in get_edges(start_index, [...additional states]):
        if additional states: 
            update([...additional states])
        ans = aggregate(ans, backtrack_agg(start_index + len(edge), [...additional states]))
        if additional states: 
            revert([...additional states])
    return ans
```

### Permutations

```python
def permute(nums):
    def backtrack(path):
        # base case
        if len(path) == len(nums):
            ans.append(path[:])
            return

        for n in nums:
            if n in path:
                continue

            path.append(n)
            backtrack(path)
            path.pop()

    ans = []
    backtrack([])
    return ans
```

### Combinations

```python
def combine(n, k):
    def backtrack(start_index, path):
        # base case
        if len(path) == k:
            ans.append(path[:])
            return

        for i in range(start_index, n+1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    ans = []
    backtrack(1, [])
    return ans
```

---

## Dynamic Programming

### DP: Recursive Top-Down Memoization

```python
def fn(arr):
    #@cache
    def dp(STATE):
        if BASE_CASE:
            return 0

        if STATE in memo:
            return memo[STATE]

        memo[STATE] = RECURRENCE_RELATION(STATE)
        return memo[STATE]

        # or if using functools
        #return RECURRENCE_RELATION(STATE)

    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)
```

### DP: Iterative Bottom-Up 1D

```python
def fn(arr):
    n = len(arr)
    dp = [0] * n

    # set base case(s)
    dp[0] = arr[0]

    for i in range(2, n):
        # define recurrence relation
        dp[i] = RECURRENCE_RELATION(STATE)

    return dp[n-1]
```

**TODO:** Dynamic programming: iterative bottom-up 2D

---

## Tries

### Build a Trie

**Note:** using a class is only necessary if you want to store data at each node. Otherwise, you can implement a trie using only hash maps.

```python
class TrieNode:
    def __init__(self):
        # you can store data at nodes if you wish
        self.data = None

        # key: char, value: TrieNode
        self.children = {}

def build_trie(words):
    root = TrieNode()

    for word in words:
        node = root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        # at this point, you have a full word at node
        # you can perform more logic here to give node an attribute if you want

    return root
```

### Insert & Search

```python
class Trie:
    def __init__(self, value=None):
        self.data = value

        # key: char, value: Trie
        self.children = {}

    def insert(self, word):
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = Trie()

            node = node.children[c]

    def search(self, word):
        node = self

        for c in word:
            if c not in node.children:
                return False

            node = node.children[c]

        return True
```

---

## Shortest Path

### Dijkstra's Algorithm

**Data struct:** heap

```python
def shortest_path(graph, source):
    distances = [math.inf] * len(graph)
    distances[source] = 0
    heap = [(0, source)]

    while heap:
        curr_dist, node = heapq.heappop(heap)
        if curr_dist > distances[node]:
            continue

        for nei, weight in graph[node]:
            dist = curr_dist + weight
            if dist < distances[nei]:
                distances[nei] = dist
                heapq.heappush(heap, (dist, nei))
```

---

## Union-Find

### DSU (Disjoint Set Union)

```python
class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)
```

