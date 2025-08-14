#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: linked list

# solution: fast & slow pointers
# complexity:
# run-time: O(n)
# space: O(1)
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def has_cycle(nodes: Node) -> bool:
    slow = fast = nodes

    while fast and fast.next:
        # compare to next!
        if slow == fast.next:
            return True

        slow = slow.next
        fast = fast.next.next

    return False

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
    res = has_cycle(nodes)
    print("true" if res else "false")