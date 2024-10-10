#!/usr/bin/env python3

import datetime
import sys
import unittest

# number: 1360
# section: assessments
# difficulty: easy
# tags: math, string, meta

# constraints
# The given dates are valid dates between the years 1971 and 2100.

# solution: Python datetime
# complexity
# run-time: O(1)
# space: O(1)
def days_bw_days(date1: str, date2: str) -> int:
    d1 = datetime.date.fromisoformat(date1)
    d2 = datetime.date.fromisoformat(date2)

    return abs((d1-d2).days)

# TODO: solve w/o datetime

if __name__ == '__main__':
    sys.exit(unittest.main())
