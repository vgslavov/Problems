#!/usr/bin/env python3

import datetime
import sys
import unittest

# number: 1360
# title: Number of Days Between Two Dates
# url: https://leetcode.com/problems/number-of-days-between-two-dates/
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

# consts
START_DATE = [1900,1,1]
DAYS_PER_MONTH = {
    1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31
}

def str2int(s):
    return [int(i) for i in s.split('-')]

def isleap(year):
    # not a multiple of 4
    if year % 4:
        return False

    # multiple of 4
    # and divisible by 100
    # but not by 400
    if not year % 100 and year % 400:
        return False

    # it is a leap year!
    return True

def days_since_start(date):
    #print(f"date:{date}")

    (year, month, day) = str2int(date)
    (start_year, start_month, start_day) = START_DATE
    days = 0

    # years
    for y in range(start_year, year):
        if isleap(y):
            days += 366
        else:
            days += 365

    # months
    for m in range(1, month):
        if m == 2 and isleap(year):
            days += 1

        days += DAYS_PER_MONTH[m]

    # days
    days += day

    #print(f"days:{days}")

    return days

# solution: manual
# complexity
# run-time: O(n)
# space: O(1)
def days_bw_days2(date1: str, date2: str) -> int:
    return abs(days_since_start(date1)-days_since_start(date2))

class TestDaysBw(unittest.TestCase):
    def test1(self):
        date1 = "2019-06-29"
        date2 = "2019-06-30"
        expected = 1
        self.assertEqual(days_bw_days(date1, date2), expected)
        self.assertEqual(days_bw_days2(date1, date2), expected)

    def test2(self):
        date1 = "2020-01-15"
        date2 = "2019-12-31"
        expected = 15
        self.assertEqual(days_bw_days(date1, date2), expected)
        self.assertEqual(days_bw_days2(date1, date2), expected)

    def test3(self):
        date1 = "1971-06-29"
        date2 = "2010-09-23"
        expected = 14331
        self.assertEqual(days_bw_days(date1, date2), expected)
        self.assertEqual(days_bw_days2(date1, date2), expected)

    def test4(self):
        date1 = "2100-09-22"
        date2 = "1991-03-12"
        expected = 40006
        self.assertEqual(days_bw_days(date1, date2), expected)
        self.assertEqual(days_bw_days2(date1, date2), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
