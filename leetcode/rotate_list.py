#!/usr/bin/env python3

import sys
import unittest

# number: 61
# section: linked list
# difficulty: medium
# tags: linked list, two pointers, top 150

# constraints
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9

# solution: manual
# complexity
# run-time: O(n)
# space: O(1)
# TODO: fix bugs
def roteate_right(head, k):

    if not k or not head:
        return head

    curr = new_head = head
    start_set = end_reached = False

    while curr:
        # old end reached
        if not curr.next:
            # link up
            curr.next = head
            end_reached = True

        if k:
            k -= 1
        # new end reached
        elif not start_set:
            prev = curr
            new_head = curr.next
            curr = new_head

            # break link
            prev.next = None
            start_set = True

        # done
        if start_set and end_reached:
            break

        # keep going
        curr = curr.next

    return new_head

# solution: fast & slow pointers
# complexity
# run-time: O(n)
# space: O(1)
# TODO: fix bugs
def roteate_right2(head, k):
    dummy = ListNode(-1)
    dummy.next = head
    fast = slow = dummy
    end_reached = False

    if not k or not head:
        return head

    # fast: k ahead of slow
    while fast.next and k:
        fast = fast.next
        k -= 1

    print(f"after 1st while: slow.val:{slow.val},fast.val:{fast.val},k:{k}")

    # list ended: create loop
    if not fast.next:
        fast.next = head
        end_reached = True

    while fast.next:
        slow = slow.next
        fast = fast.next

        if end_reached and not k:
            break
        elif k:
            k -= 1

    print(f"after 2nd while: slow.val:{slow.val},fast.val:{fast.val}")

    # list ended: create loop
    if not fast.next:
        fast.next = head
        end_reached = True

    print(f"k:{k},end_reached:{end_reached}")

    new_head = slow.next
    slow.next = None

    return new_head

# TODO: add unit tests
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Input: head = [1,2], k = 1
# Output: [2,1]

# TODO: bug fix
# Input: head = [1,2], k = 2
# Output: [1,2]

if __name__ == '__main__':
    sys.exit(unittest.main())
