#!/usr/bin/env python3

# section: assessments
# difficulty: easy
# tags: google

# constraints
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100

def height_checker(heights):
    expected = sorted(heights)
    ans = 0

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            ans += 1

    return ans
