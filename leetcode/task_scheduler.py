#!/usr/bin/env python3

from collections import defaultdict, deque
import heapq
import sys
import unittest

# number: 621
# title: Task Scheduler
# url: https://leetcode.com/problems/task-scheduler/
# section: 
# difficulty: medium
# tags: hash table, array, greedy, sorting, grind 75, heap, counting, design

# constraints
# 1 <= tasks.length <= 10^4
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100

# solution: Neetcode max heap + deque
# complexity
# run-time: O(n)
# space: O(n)
# len(task_freq): O(1), 26
# len(heap): O(n)
# len(queue): O(n)
def least_interval(tasks: list[str], n: int) -> int:
    # max heap with *scheduled* tasks
    # key: task
    # value: freq
    task_freq = defaultdict(int)

    # cooldown queue:
    # (freq, time to schedule)
    queue = deque()

    time = 0

    for t in tasks:
        task_freq[t] += 1

    # tasks by count: most freq on top
    # negate to make max heap!
    max_heap = [-v for v in task_freq.values()]
    heapq.heapify(max_heap)

    # keep iterating as long as tasks scheduled or cooling down
    while max_heap or queue:
        time += 1

        if max_heap:
            # get highest freq task
            freq = -heapq.heappop(max_heap)

            # run
            freq -= 1

            # put in queue for cooldown
            if freq:
                queue.append((freq, time+n))

        # take task off queue if it can run
        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, -queue.popleft()[0])

    return time

class TestLeastInterval(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(least_interval(["A","A","A","B","B","B"], 2), 8)

    def test_example2(self):
        self.assertEqual(least_interval(["A","C","A","B","D","B"], 1), 6)

    def test_example3(self):
        self.assertEqual(least_interval(["A","A","A","B","B","B"], 0), 6)

    def test_single_task(self):
        self.assertEqual(least_interval(["A"], 2), 1)

    def test_all_same(self):
        self.assertEqual(least_interval(["A","A","A"], 2), 7)

    def test_no_cooldown(self):
        self.assertEqual(least_interval(["A","B","C","A","B","C"], 0), 6)

    def test_high_cooldown(self):
        self.assertEqual(least_interval(["A","A","A","B","B","B"], 50), 104)

if __name__ == '__main__':
    sys.exit(unittest.main())