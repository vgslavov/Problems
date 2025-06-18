#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 339
# title: Nested List Weight Sum
# url: https://leetcode.com/problems/nested-list-weight-sum/
# section: meta
# difficulty: medium
# tags: dfs, bfs

# constraints
# 1 <= nestedList.length <= 50
# The values of the integers in the nested list is in the range [-100, 100].
# The maximum depth of any integer is less than or equal to 50.

class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        The result is undefined if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        The result is undefined if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

# solution: recursive dfs
# complexity:
# run-time: O(n)
# space: O(n)
def depth_sum(nestedList: list[NestedInteger]) -> int:
    def dfs(nested_list, depth):
        ans = 0
        for nested in nested_list:
            if nested.isInteger():
                ans += nested.getInteger() * depth
            else:
                ans += dfs(nested.getList(), depth+1)

        return ans

    return dfs(nestedList, 1)

# solution: Leetcode iterative bfs using deque
# complexity:
# run-time: O(n)
# space: O(n)
def depth_sum2(nestedList: list[NestedInteger]) -> int:
    queue = deque(nestedList)
    ans = 0
    depth = 1

    while queue:
        current_len = len(queue)

        for _ in range(current_len):
            # read from front
            nested = queue.popleft()

            if nested.isInteger():
                ans += nested.getInteger() * depth
            else:
                # extend/append from back!
                queue.extend(nested.getList())
                # or
                #for elem in nested.getList():
                #    queue.append(elem)

        depth += 1

    return ans

if __name__ == "__main__":
    sys.exit(unittest.main())