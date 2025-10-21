#!/usr/bin/env python3

from collections import defaultdict, deque
import sys
import unittest

# number: 207
# title: Course Schedule
# url: https://leetcode.com/problems/course-schedule/
# difficulty: medium
# tags: topological sort, kahn's algorithm, bfs, grind 75

# constraints:
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= a_i, b_i < numCourses
# a_i != b_i
# all the pairs [a_i, b_i] are unique

def build_adjlist(edges, n):
    graph = defaultdict(list)

    # initialize all courses
    for i in range(n):
        graph[i] = []

    # create edge from prerequisite to course
    for x,y in edges:
        graph[x].append(y)

    return graph

def calc_indegree(graph):
    indegree = { node: 0 for node in graph }

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    return indegree

def topo_sort(graph, n):
    indegree = calc_indegree(graph)
    queue = deque()
    ans = []

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

    return len(ans) == n

# solution: Kahn's algorithm using BFS
# complexity:
# run-time: O(V + E)
# space: O(V)
def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = build_adjlist(prerequisites, numCourses)

    return topo_sort(graph, numCourses)

class TestCourseSchedule(unittest.TestCase):
    
    def test_can_finish(self):
        self.assertTrue(can_finish(2, [[1,0]]))
        self.assertFalse(can_finish(2, [[1,0],[0,1]]))
        self.assertTrue(can_finish(5, [[1,4],[2,4],[3,1],[3,2]]))
        self.assertFalse(can_finish(3, [[0,1],[1,2],[2,0]]))

if __name__ == "__main__":
    unittest.main()