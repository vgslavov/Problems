#!/usr/bin/env python3

import bisect
from collections import defaultdict
from collections import deque
from functools import cache
import heapq
from math import inf

# Sources:
# - https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/
# - https://algo.monster/templates

# Two pointers: one input, opposite direction
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

# Two pointers: one input, same direction
def two_pointers_same(arr):
    slow, fast = 0, 0

    while fast < len(arr):
        # do logic with slow and fast

        # Update pointers based on condition
        if condition(arr[slow], arr[fast]):
            slow += 1

        # Fast pointer *always* moves forward
        fast += 1

# Two pointers: two inputs, exhaust both
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

# Sliding window
SOME_THRESHOLD = 10  # Example threshold, adjust as needed

def invalid_condition(curr):
    # define the condition for the sliding window to be invalid
    return curr > SOME_THRESHOLD

def sliding_window(arr):
    left = ans = curr = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while invalid_condition(curr):
            # remove arr[left] from curr
            left += 1

        # update ans: window guaranteed to be valid
        ans = max(ans, right - left + 1)

    return ans

# Sliding *fixed* window
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

# Build a diff array, calculate prefix sum on it
def diff_array(arr, shifts):
    diff = [0] * len(arr)

    for start, end in shifts:
        diff[start] += 1
        # if inclusive
        if end + 1 < len(diff):
            diff[end + 1] -= 1

    return diff

# Build a prefix sum
def prefix_sum(arr):
    # or preallocate
    #prefix = [0] * len(arr)
    prefix = [arr[0]]

    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
        #prefix[i] = prefix[i-1] + arr[i]

    return prefix

# Query sum of range using prefix sum
def query_prefix_sum(prefix, left, right):
    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]

# Efficient string building
# arr is a list of characters
def string(arr):
    #return ''.join(c for c in arr)
    return ''.join(arr)

# Linked list: fast and slow pointer
# traversing: iteratively more common
def fn(head):
    slow = head
    fast = head
    ans = 0

    while fast and fast.next:
        # do logic
        slow = slow.next
        fast = fast.next.next

    return ans

# Linked list: fast & slow k apart
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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Linked list: dummy nodes
def fn(head):
    dummy = ListNode(0, head)
    fast = slow = dummy

    # move fast pointer k ahead

    while fast.next:
        slow = slow.next
        fast = fast.next

    # do something

    return dummy.next

# Reversing a linked list
def reverse(head):
    prev = None

    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev

# Find number of subarrays that fit an exact criteria
def fn(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

# Monotonic increasing stack/queue
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

# Merge intervals
def merge_intervals(intervals):
    intervals.sort()
    ans = []

    for start, end in intervals:
        # merge
        if ans and start <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], end)
        else:
            ans.append([start,end])

    return ans

# Binary tree: recursive DFS (more common)
# data struct: recursion stack (LIFO)
def dfs(root, target=None):
    # base case
    if not root:
        return None

    if root.val == target:
        return root

    # preorder: order same as function calls
    #print("preorder: ".format(root.val))

    # do logic
    left = dfs(root.left, target)

    if left:
        return left

    # inorder: all left subtree printed before current and then right subtree
    # on BST: traversal is in sorted order
    #print("inorder: ".format(root.val))

    return dfs(root.right, target)

    # postorder: root is last to be traversed
    #print("postorder: ".format(root.val))

# Binary tree: iterative DFS (less common)
# data struct: recursion stack (LIFO)
def dfs(root, target=None):
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

# Binary tree: iterative BFS (more common)
# data struct: queue (FIFO)
def bfs(root):
    # list of root!
    queue = deque([root])
    ans = 0

    while queue:
        current_length = len(queue)
        # do logic for current level

        for _ in range(current_length):
            # read from front
            node = queue.popleft()

            # do logic

            # add to back
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

# Graph: build adjacency list/dict
# input: array of edges, [[0,1],[1,2],[2,0],[2,3]]
# output: adjacency list/dict, {0: [1], 1: [0, 2], 2: [1, 0, 3], 3: [2]}
def build_adjlist(edges):
    graph = defaultdict(list)

    for x,y in edges:
        graph[x].append(y)
        # if undirected graph
        graph[y].append(x)

    return graph

# Graph: DFS (recursive)
# data struct: recursion stack (LIFO)
def dfs(graph):
    def dfs(node):
        ans = 0
        # do some logic
        for neighbor in graph[node]:
            if neighbor in seen:
                continue

            # mark neighbor as seen
            seen.add(neighbor)
            ans += dfs(neighbor)

        return ans

    seen = {START_NODE}
    return dfs(START_NODE)

# Graph: DFS (iterative)
# data struct: stack (LIFO)
def dfs(graph):
    stack = [START_NODE]
    seen = {START_NODE}
    ans = 0

    while stack:
        node = stack.pop()
        # do some logic

        for neighbor in graph[node]:
            if neighbor in seen:
                continue

            # mark neighbor as seen
            seen.add(neighbor)
            stack.append(neighbor)

    return ans

# Graph: BFS
# data struct: queue (FIFO)
def bfs(graph):
    queue = deque([START_NODE])
    seen = {START_NODE}
    ans = 0

    while queue:
        node = queue.popleft()
        # do some logic

        for neighbor in graph[node]:
            if neighbor in seen:
                continue

            # mark neighbor as seen
            seen.add(neighbor)
            queue.append(neighbor)

    return ans

# Find top k elements with heap
def find_topk(arr, k):
    heap = []
    for num in arr:
        # do some logic to push onto heap according to problem's criteria
        heapq.heappush(heap, (CRITERIA, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for num in heap]

# Binary search: using bisect, ascending sorted only!
def binary_search_bisect_left(arr, target):
    i = bisect.bisect_left(arr, target)
    if i < len(arr) and arr[i] == target:
        return True

    return False

# Binary search
# complexity:
# run-time: O(log n)
# space: O(1) vs O(log n) if using recursion
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

# Binary search: duplicate elements, left-most insertion point
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

# Binary search: duplicate elements, right-most insertion point
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

# Binary search: find min (for greedy problems)
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

# Binary search: find max
def binary_search_max(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right

# Backtracking
def backtrack(curr, OTHER_ARGUMENTS...):
    if (BASE_CASE):
        # modify the answer
        return

    ans = 0
    for ITERATE_OVER_INPUT:
        # modify the current state
        ans += backtrack(curr, OTHER_ARGUMENTS...)
        # undo the modification of the current state

    return ans

# Backtracking: permutations
def permute(nums):
    def backtrack(curr):
        # base case
        if len(curr) == len(nums):
            ans.append(curr[:])
            return

        for n in nums:
            if n in curr:
                continue

            curr.append(n)
            backtrack(curr)
            curr.pop()

    ans = []
    backtrack([])
    return ans

# Backtracking: combinations
def combine(n, k):
    def backtrack(curr, i):
        # base case
        if len(curr) == k:
            ans.append(curr[:])
            return

        for num in range(i, n+1):
            curr.append(num)
            backtrack(curr, num + 1)
            curr.pop()

    ans = []
    backtrack([], 1)
    return ans

# Dynamic programming: recursive top-down memoization
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

# Dynamic programming: iterative bottom-up 1D
def fn(arr):
    n = len(arr)
    dp = [0] * n

    # set base case(s)
    dp[0] = arr[0]

    for i in range(2, n):
        # define recurrence relation
        dp[i] = RECURRENCE_RELATION(STATE)

    return dp[n-1]

# TODO: Dynamic programming: iterative bottom-up 2D

# Build a trie
# note: using a class is only necessary if you want to store data at each node.
# otherwise, you can implement a trie using only hash maps.
class TrieNode:
    def __init__(self):
        # you can store data at nodes if you wish
        self.data = None
        self.children = {}

def build_trie(words):
    root = TrieNode()
    for word in words:
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        # at this point, you have a full word at curr
        # you can perform more logic here to give curr an attribute if you want

    return root

# Build a trie: insert & search
class Trie:
    def __init__(self, value=None):
        self.data = value
        self.children = {}

    def insert(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()

            curr = curr.children[c]

    def search(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return True

# Dijkstra's algorithm
# data struct: heap
def shortest_path(graph, source):
    distances = [inf] * len(graph)
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

# Union-Find: DSU (Disjoint Set Union)
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

