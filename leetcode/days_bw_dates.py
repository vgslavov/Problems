#!/usr/bin/env python3

import datetime

# section: assessments
# difficulty: easy
# tags: meta

# constraints
# The given dates are valid dates between the years 1971 and 2100.

def days_bw_days(date1: str, date2: str) -> int:
    d1 = datetime.date.fromisoformat(date1)
    d2 = datetime.date.fromisoformat(date2)

    return abs((d1-d2).days)
