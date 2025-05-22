#!/usr/bin/env python3

import sys
import unittest

# number: 157
# title: Read N Characters Given Read4
# url: https://leetcode.com/problems/read-n-characters-given-read4/
# section: meta
# difficulty: easy
# tags: meta, array, simulation, interactive

# constraints
# 1 <= file.length <= 500
# file consist of English letters and digits.
# 1 <= n <= 1000

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

# solution: use tmp buf of 4
# complexity
# run-time: O(n)
# space: O(1)
def read(buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Number of characters to read (int)
    :rtype: The number of actual characters read (int)
    """

    # local buf
    buf4 = [' '] * 4
    total_read = nread = 0

    # TODO: refactor ugly code
    while n:
        print(f"n:{n},nread:{nread},total_read:{total_read}")
        nread = read4(buf4)

        if nread > n:
            buf[total_read:] = buf4[:n+1]
            return total_read + n
        else:
            buf[total_read:] = buf4

        n -= nread
        total_read += nread

        if not nread or nread < 4:
            break

    return total_read

# TODO: solve w/o buf4

if __name__ == '__main__':
    sys.exit(unittest.main())
