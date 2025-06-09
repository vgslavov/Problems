from collections import defaultdict

# number: 362
# title: Design Hit Counter
# url: https://leetcode.com/problems/design-hit-counter/
# difficulty: medium
# tags: array, binary search, design, queue, data stream

# constraints:
# 1 <= timestamp <= 2 * 10^9
# All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
# At most 300 calls will be made to hit and getHits.

# solution: dict
# complexity:
# run-time: O(n)
# space: O(n)
class HitCounter:

    def __init__(self):
        self.__timestamps = defaultdict(int)

    # TODO: drop older timestamps
    def hit(self, timestamp: int) -> None:
        self.__timestamps[timestamp] += 1
        
    def getHits(self, timestamp: int) -> int:
        from_time = timestamp-300+1 if timestamp > 300 else 0
        ans = 0

        # like C++ map
        for key in sorted(self.__timestamps.keys()):
            # TODO: start from this key
            if key < from_time:
                continue
            elif key > timestamp:
                break

            ans += self.__timestamps[key]

        return ans

# Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
timestamp = 1
obj.hit(timestamp)
param_2 = obj.getHits(timestamp)