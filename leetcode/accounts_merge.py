#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 721
# title: Accounts Merge
# url: https://leetcode.com/problems/accounts-merge/
# section: graph
# difficulty: medium
# tags: dfs, bfs, union find, graph, hash table, grind 75, sorting, string

# constraints:
# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j].length <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.

# solution: recursive dfs
# complexity:
# run-time: O(a * e log e) where a is number of accounts, e
#          is average number of emails per account (for sorting)
# space: O(a * e)
def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    def dfs(node, cur):
        for neighbor in graph[node]:
            if neighbor in seen:
                continue

            cur.append(neighbor)
            seen.add(neighbor)
            dfs(neighbor, cur)

    # build graph
    graph = defaultdict(list)

    for a in accounts:
        for i in range(1, len(a)):
            for j in range (i+1, len(a)):
                graph[a[i]].append(a[j])
                graph[a[j]].append(a[i])

    #print(f"graph:{graph}")
    seen = set()
    ans = []

    for a in accounts:
        cur = []
        for i in range(1, len(a)):
            if a[i] in seen:
                continue

            cur.append(a[i])
            seen.add(a[i])
            dfs(a[i], cur)

        if cur:
            ans.append([a[0]])
            cur.sort()
            ans[-1].extend(cur)

    return ans

class TestAccountsMerge(unittest.TestCase):
    def test_accounts_merge(self):
        self.assertEqual(
            accounts_merge([["John", "johnsmith@mail.com", "john00@mail.com"],
                             ["John", "johnnybravo@mail.com"],
                             ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                             ["Mary", "mary@mail.com"]]),
            [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
             ["John", "johnnybravo@mail.com"],
             ["Mary", "mary@mail.com"]]
        )

if __name__ == "__main__":
    sys.exit(unittest.main())