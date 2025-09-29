#!/usr/bin/env python3

import argparse
import heapq
import sys
import unittest

# tags: heap

# solution: min heap
# complexity:
# run-time: O(n*log k)
# space: O(k)
def find_kth_largest(nums: list[int], k: int) -> int:
    if not nums:
        return 0

    heap = []

    for n in nums:
        heapq.heappush(heap, n)

        if len(heap) > k:
            heapq.heappop(heap)
    
    # kth largest will be on top of min heap
    return heap[0]

# solution: AlgoMonster max heap
# complexity:
# run-time: O(n + k*log n), heapify + pop
# space: O(1), using existing nums space
def find_kth_largest2(nums: list[int], k: int) -> int:
    if not nums:
        return 0

    # max heap: O(n)
    nums = [-x for x in nums]
    heapq.heapify(nums)

    # O(k*log n)
    for _ in range(k - 1):
        heapq.heappop(nums)

    return -nums[0]

# solution: AlgoMonster Quick Select
# complexity:
# run-time: O(n^2) worst case, O(n) average case
# space: O(1), using nums space
# TODO: understand better
def find_kth_largest3(nums: list[int], k: int) -> int:
    if not nums:
        return 0

    min_ptr = 0
    max_ptr = len(nums) - 1

    while min_ptr < max_ptr:
        pivot = nums[max_ptr]
        swap_left = min_ptr
        swap_right = max_ptr

        while swap_left < swap_right:
            while swap_left < swap_right and nums[swap_left] > pivot:
                swap_left += 1
            while swap_left < swap_right and nums[swap_right] <= pivot:
                swap_right -= 1
            if swap_left < swap_right:
                nums[swap_left], nums[swap_right] = nums[swap_right], nums[swap_left]

        nums[swap_left], nums[max_ptr] = nums[max_ptr], nums[swap_left]

        if swap_left == k - 1:
            return nums[swap_left]
        elif swap_left < k - 1:
            min_ptr = swap_left + 1
        else:
            max_ptr = swap_left - 1

    return nums[min_ptr]

class TestFindKthLargest(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(find_kth_largest2([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(find_kth_largest3([3, 2, 1, 5, 6, 4], 2), 5)

        self.assertEqual(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
        self.assertEqual(find_kth_largest2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
        self.assertEqual(find_kth_largest3([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

        self.assertEqual(find_kth_largest([], 1), 0)
        self.assertEqual(find_kth_largest2([], 1), 0)
        self.assertEqual(find_kth_largest3([], 1), 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    k = int(input())
    res = find_kth_largest(nums, k)
    print(res)