#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: two pointers
# leetcode: 876

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# solution: two pointers, slow & fast, same direction
# complexity:
# run-time: O(n)
# space: O(1)
def middle_node(head: Node) -> int:
    slow, fast = head, head

    # check both fast & fast.next to avoid NoneType errors
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow.val

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

class TestMiddleOfLinkedList(unittest.TestCase):
    def test_example_1(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        self.assertEqual(middle_node(head), 3)
        
    def test_example_2(self):
        head = Node(1, Node(2, Node(3, Node(4))))
        self.assertEqual(middle_node(head), 3)

    def test_example_3(self):
        head = Node(1)
        self.assertEqual(middle_node(head), 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    head = build_list(iter(input().split()), int)
    res = middle_node(head)
    print(res)