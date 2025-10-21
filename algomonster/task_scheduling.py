#!/usr/bin/env python3

import argparse
from collections import defaultdict, deque
import sys
import unittest

# tags: topological sort, kahn's algorithm

def build_adjlist(edges, tasks):
    graph = defaultdict(list)

    for t in tasks:
        graph[t] = []

    for x,y in edges:
        graph[x].append(y)

    return graph

def calc_indegree(graph):
    indegree = { node: 0 for node in graph }

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    return indegree
    
# solution: Kahn's algorithm
# complexity:
# run-time: O(V + E)
# space: O(V)
def topo_sort(graph):
    indegree = calc_indegree(graph)
    queue = deque()
    ans = []

    # add all nodes with indegree 0 to queue
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

    return ans if len(graph) == len(ans) else None

def task_scheduling(tasks: list[str], requirements: list[list[str]]) -> list[str]:
    graph = build_adjlist(requirements, tasks)
    
    return topo_sort(graph)

class TestTaskScheduling(unittest.TestCase):
    
    def test_task_scheduling(self):
        self.assertEqual(
            task_scheduling(
                ["A", "B", "C", "D"],
                [["A", "B"], ["B", "C"], ["A", "C"], ["D", "C"]]
            ),
            ["A", "D", "B", "C"]
        )
        self.assertEqual(
            task_scheduling(
                ["A", "B", "C"],
                [["A", "B"], ["B", "C"], ["C", "A"]]
            ),
            None
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    tasks = input().split()
    requirements = [input().split() for _ in range(int(input()))]
    res = task_scheduling(tasks, requirements)
    if len(res) != len(tasks):
        print(f"output size {len(res)} does not match input size {len(tasks)}")
        sys.exit()
    indices = {task: i for i, task in enumerate(res)}
    for req in requirements:
        for task in req:
            if task not in indices:
                print(f"'{task}' is not in output")
                sys.exit()
        a, b = req
        if indices[a] >= indices[b]:
            print(f"'{a}' is not before '{b}'")
            sys.exit()
    print("ok")