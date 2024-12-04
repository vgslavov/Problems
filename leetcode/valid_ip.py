#!/usr/bin/env python3

from ipaddress import ip_address, IPv4Address
import re
import sys
import unittest

# number: 468
# section: meta
# difficulty: medium
# tags: string, meta

# constraints
# queryIP consists only of English letters, digits and the characters '.' and ':'.

# complexity
# run-time: O(n)
# space: O(1)
def valid_ipv4(tokens):
    # need exactly 4 tokens
    if not tokens or len(tokens) != 4:
        return "Neither"

    for i in range(len(tokens)):
        #print(f"tokens[{i}]:{tokens[i]}")

        # not necessary if try/except
        #if not tokens[i].isdecimal():
        #    return "Neither"

        try:
            num = int(tokens[i])
        except (ValueError):
            return "Neither"

        if num < 0 or num > 255:
            return "Neither"

        # number can't start with 0
        if len(tokens[i]) > 1 and int(tokens[i][0]) == 0:
            return "Neither"

    return "IPv4"

# complexity
# run-time: O(n)
# space: O(1)
def valid_ipv6(tokens):
    # need exactly 8 tokens
    if not tokens or len(tokens) != 8:
        return "Neither"

    for t in tokens:
        if len(t) > 4:
            return "Neither"

        try:
            num = int(t, 16)
        except (ValueError):
            return "Neither"

    return "IPv6"

# solution: Pythonic split + divide & conquer + try/except
# complexity
# run-time: O(n)
# space: O(1)
def valid_ip(query: str) -> str:
    if not query:
        return "Neither"

    # check if IPv4
    tokens = query.split(".")

    if len(tokens) > 1:
        return valid_ipv4(tokens)

    # check if IPv6
    tokens = query.split(":")

    if len(tokens) > 1:
        return valid_ipv6(tokens)

    return "Neither"

# solution: re
# complexity
# run-time: O(n)
# space: O(1)
# TODO: finish solving using re
def valid_ip2(query: str) -> str:
    r = "( 25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]? )"
    r2 = [r]*4

    split = re.split('\.'.join(r2), query)

    if len(split) == 4:
        return "IPv4"

    return "Neither"

# solution: Pythonic, non-interview
def valid_ip3(query):
    try:
        return "IPv4" if type(ip_address(query)) is IPv4Address else "IPv6"
    except ValueError:
        return "Neither"

class TestValidIP(unittest.TestCase):
    def test_empty(self):
        query = ""
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)
        self.assertEqual(valid_ip3(query), expected)

    def test_ipv4_valid(self):
        query = "172.16.254.1"
        expected = "IPv4"
        self.assertEqual(valid_ip(query), expected)
        #self.assertEqual(valid_ip2(query), expected)
        self.assertEqual(valid_ip3(query), expected)

    def test_ipv4_invalid(self):
        query = "256.256.256.256"
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)
        self.assertEqual(valid_ip3(query), expected)

    def test_ipv4_invalid2(self):
        query = "01.01.01.01"
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)
        self.assertEqual(valid_ip3(query), expected)

    def test_ipv4_invalid3(self):
        query = "0db8.01.01.01"
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)
        self.assertEqual(valid_ip3(query), expected)

    def test_ipv4_invalid4(self):
        query = "1e1.4.5.6"
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)
        self.assertEqual(valid_ip3(query), expected)

    def test_ipv6_valid(self):
        query = "2001:0db8:85a3:0:0:8A2E:0370:7334"
        expected = "IPv6"
        self.assertEqual(valid_ip(query), expected)
        self.assertEqual(valid_ip3(query), expected)

    def test_ipv6_invalid(self):
        query = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)
        self.assertEqual(valid_ip3(query), expected)

    def test_ipv6_invalid2(self):
        query = "20EE:FGb8:85a3:0:0:8A2E:0370:7334"
        expected = "Neither"
        self.assertEqual(valid_ip(query), expected)
        self.assertEqual(valid_ip3(query), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
