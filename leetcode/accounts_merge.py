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
# run-time: O(a * e^2 + a * e log e) where a is number of accounts, e
#          is average number of emails per account
#          - O(a * e^2) for graph building (all pairs within each account)
#          - O(a * e log e) for DFS traversal and sorting
# space: O(a * e^2) for graph adjacency list + O(a * e) for seen set and DFS
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

    def test_single_email_accounts(self):
        result = accounts_merge([["John", "e1@mail.com"],
                                 ["Jane", "e2@mail.com"]])
        # Should return both accounts separately
        self.assertEqual(len(result), 2)
        self.assertIn(["John", "e1@mail.com"], result)
        self.assertIn(["Jane", "e2@mail.com"], result)

    def test_chained_emails(self):
        # e1 connects to e2, e2 connects to e3, so all should merge
        result = accounts_merge([["John", "e1@mail.com", "e2@mail.com"],
                                 ["John", "e2@mail.com", "e3@mail.com"],
                                 ["John", "e3@mail.com", "e4@mail.com"]])
        # All emails should be in one merged account
        self.assertEqual(len(result), 1)
        merged_emails = set(result[0][1:])  # Skip name
        self.assertEqual(merged_emails, {"e1@mail.com", "e2@mail.com", "e3@mail.com", "e4@mail.com"})

    def test_no_merging(self):
        result = accounts_merge([["John", "e1@mail.com"],
                                 ["Jane", "e2@mail.com"],
                                 ["Bob", "e3@mail.com"]])
        self.assertEqual(len(result), 3)

if __name__ == "__main__":
    sys.exit(unittest.main())