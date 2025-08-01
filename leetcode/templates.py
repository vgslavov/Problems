#!/usr/bin/env python3

import bisect
from collections import defaultdict
from collections import deque
from functools import cache
import heapq
from math import inf

# Two pointers: one input, opposite ends
def fn(arr):
    left = ans = 0
    right = len(arr) - 1

    while left < right:
        # do some logic here with left and right
        if CONDITION:
            left += 1
        else:
            right -= 1

    return ans

# Two pointers: two inputs, exhaust both
def fn(arr1, arr2):
    i = j = ans = 0

    while i < len(arr1) and j < len(arr2):
        # do some logic here
        if CONDITION:
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
def fn(arr):
    left = ans = curr = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans

    return ans

# Sliding *fixed* window
def fn(arr, k):
    ans = curr = 0

    # 1st window
    # if k <= n!
    for i in range(k):
        # do logic here to add arr[i] to curr
        pass

    # update ans

    for i in range(min(k, len(arr))):
        pass
        # add arr[i] & remove arr[i-k] from curr

        # update ans

    return ans

# Build a prefix sum
def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])

    return prefix

# Build a diff array
def fn(arr, shifts):
    diff = [0] * len(arr)

    for start, end in shifts:
        diff[start] += 1
        # if inclusive
        if end + 1 < len(diff):
            diff[end + 1] -= 1

    return diff

# Efficient string building
# arr is a list of characters
def fn(arr):
    ans = []
    for c in arr:
        ans.append(c)

    return "".join(ans)

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
def fn(head):
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
def fn(arr):
    stack = []
    ans = 0

    for num in arr:
        # for monotonic decreasing, just flip the > to <
        while stack and stack[-1] > num:
            # do logic
            stack.pop()
        stack.append(num)

    return ans

# intervals
def fn(intervals):
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
def dfs(root):
    if not root:
        return

    ans = 0

    # preorder: order same as function calls
    print("preorder: ".format(root.val))

    # do logic
    dfs(root.left)

    # inorder: all left subtree printed before current and then right subtree
    # on BST: traversal is in sorted order
    print("inorder: ".format(root.val))

    dfs(root.right)

    # postorder: root is last to be traversed
    print("postorder: ".format(root.val))

    return ans

# Binary tree: iterative DFS (less common)
def dfs(root):
    stack = [root]
    ans = 0

    while stack:
        node = stack.pop()
        # do logic
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return ans

# Binary tree: iterative BFS (more common)
def fn(root):
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
def fn(edges):
    graph = defaultdict(list)

    for x,y in edges:
        graph[x].append(y)
        # if undirected graph
        graph[y].append(x)

    return graph

# Graph: DFS (recursive)
def fn(graph):
    def dfs(node):
        ans = 0
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans += dfs(neighbor)

        return ans

    seen = {START_NODE}
    return dfs(START_NODE)

# Graph: DFS (iterative)
# data struct: stack
def fn(graph):
    stack = [START_NODE]
    seen = {START_NODE}
    ans = 0

    while stack:
        node = stack.pop()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)

    return ans

# Graph: BFS
# data struct: queue
def fn(graph):
    queue = deque([START_NODE])
    seen = {START_NODE}
    ans = 0

    while queue:
        node = queue.popleft()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return ans

# Find top k elements with heap
def fn(arr, k):
    heap = []
    for num in arr:
        # do some logic to push onto heap according to problem's criteria
        heapq.heappush(heap, (CRITERIA, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for num in heap]

# Binary search: using bisect, ascending sorted only!
def fn(arr, target):
    i = bisect.bisect_left(arr, target)
    if i < len(arr) and arr[i] == target:
        return True

    return False

# Binary search
def fn(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        # prevent overflowing
        mid = left + (right - left) // 2
        #mid = (left + right) // 2
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
def fn(arr, target):
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
def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left

# Binary search: for greedy problems
# find min
def fn(arr):
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

# find max
def fn(arr):
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
            if n not in curr:
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

def fn(words):
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
    def __init__(self):
        self.data = None
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
distances = [inf] * n
distances[source] = 0
heap = [(0, source)]

while heap:
    curr_dist, node = heappop(heap)
    if curr_dist > distances[node]:
        continue

    for nei, weight in graph[node]:
        dist = curr_dist + weight
        if dist < distances[nei]:
            distances[nei] = dist
            heappush(heap, (dist, nei))
