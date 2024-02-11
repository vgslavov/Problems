#!/usr/bin/env python3

import sys
import unittest

# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
def strstr(haystack, needle):
    if not haystack or not needle:
        return -1
    elif haystack == needle:
        return 0

    start = i = j = 0

    while i < len(haystack) and j < len(needle):
        # needle is matching
        if haystack[i] == needle[j]:
            if j == 0:
                start = i
            j += 1
        # needle is not matching: reset
        else:
            j = 0

        # continue going through haystack
        i += 1

    # needle found
    if j == len(needle):
        return start

    return -1

if __name__ == '__main__':
    sys.exit(unittest.main())
