#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: linked list
# leetcode: 141

# solution: fast & slow pointers
# complexity:
# run-time: O(n)
# space: O(1)
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def hascycle(nodes: Node) -> bool:
    slow = fast = nodes

    while fast and fast.next:
        # compare to next!
        if slow == fast.next:
            return True

        slow = slow.next
        fast = fast.next.next

    return False

class TestHasCycle(unittest.TestCase):
    def test_hascycle(self):
        # Test case 1: No cycle
        nodes = Node(1)
        nodes.next = Node(2)
        nodes.next.next = Node(3)
        self.assertFalse(hascycle(nodes))

        # Test case 2: Cycle
        nodes = Node(1)
        nodes.next = Node(2)
        nodes.next.next = Node(3)
        nodes.next.next.next = nodes.next  # Create cycle
        self.assertTrue(hascycle(nodes))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    raw_input = [int(x) for x in input().split()]
    nodes_list = []
    for i in range(len(raw_input)):
        nodes_list.append(Node(i))
    for i, entry in enumerate(raw_input):
        if entry != -1:
            nodes_list[i].next = nodes_list[entry]
    nodes = nodes_list[0]
    res = hascycle(nodes)
    print("true" if res else "false")