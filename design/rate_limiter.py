#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# section: queue
# difficulty: easy
# tags: queue, limiter

class Request:
    def __init__(self, timestamp):
        self.timestamp = timestamp

# solution: sliding window w/ deque
# complexity:
# run-time: O(n) amortized
# space: O(size)
class RateLimiter:
    def __init__(self, max_reqs: int, win_sec: float):
        # max reqs inside window 
        self.__max_reqs = max_reqs
        # window size in seconds
        self.__win_sec = win_sec

    def process(self, requests: list[Request]) -> list[bool]:
        ans = []
        # store processed reqs only
        win = deque()

        for req in requests:
            # 1. Evict requests that have fallen outside the window
            while win and req.timestamp - win[0].timestamp >= self.__win_sec:
                win.popleft()

            # 2. Allow if under the limit, deny otherwise
            if len(win) < self.__max_reqs:
                win.append(req)
                ans.append(True)
            else:
                ans.append(False)

        return ans


def reqs(*timestamps):
    return [Request(t) for t in timestamps]


class TestRateLimiter(unittest.TestCase):

    def test_all_allowed_under_limit(self):
        # 3 requests well within window, limit never reached
        rl = RateLimiter(max_reqs=3, win_sec=10)
        result = rl.process(reqs(0, 1, 2))
        self.assertEqual(result, [True, True, True])

    def test_deny_when_window_full(self):
        # 4th request within same window should be denied
        rl = RateLimiter(max_reqs=3, win_sec=10)
        result = rl.process(reqs(0, 1, 2, 3))
        self.assertEqual(result, [True, True, True, False])

    def test_allow_after_window_expires(self):
        # After oldest request falls out of the window, a new one is allowed
        rl = RateLimiter(max_reqs=3, win_sec=10)
        result = rl.process(reqs(0, 1, 2, 10))
        self.assertEqual(result, [True, True, True, True])

    def test_boundary_exactly_at_win_sec(self):
        # t=10 is exactly win_sec=10 away from t=0, so t=0 is evicted
        rl = RateLimiter(max_reqs=2, win_sec=10)
        result = rl.process(reqs(0, 5, 10))
        self.assertEqual(result, [True, True, True])

    def test_boundary_one_inside_win_sec(self):
        # t=9 is within the window [0,9), t=0 is NOT evicted
        rl = RateLimiter(max_reqs=2, win_sec=10)
        result = rl.process(reqs(0, 5, 9))
        self.assertEqual(result, [True, True, False])

    def test_single_request_always_allowed(self):
        rl = RateLimiter(max_reqs=1, win_sec=10)
        result = rl.process(reqs(0))
        self.assertEqual(result, [True])

    def test_size_one_allows_one_per_window(self):
        rl = RateLimiter(max_reqs=1, win_sec=10)
        result = rl.process(reqs(0, 5, 10, 15))
        self.assertEqual(result, [True, False, True, False])

    def test_denied_requests_dont_consume_quota(self):
        # Denied requests should not enter the window or block future requests
        rl = RateLimiter(max_reqs=2, win_sec=10)
        #   t=0 allowed, t=1 allowed, t=2 denied (full), t=11 allowed (0,1 evicted)
        result = rl.process(reqs(0, 1, 2, 11))
        self.assertEqual(result, [True, True, False, True])

    def test_empty_input(self):
        rl = RateLimiter(max_reqs=3, win_sec=10)
        result = rl.process([])
        self.assertEqual(result, [])

    def test_large_gap_resets_window(self):
        rl = RateLimiter(max_reqs=2, win_sec=5)
        result = rl.process(reqs(0, 1, 100, 101))
        self.assertEqual(result, [True, True, True, True])


if __name__ == '__main__':
    sys.exit(unittest.main())
