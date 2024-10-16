#!/usr/bin/env python3

import holidays


def is_working(year: int, month: int, day: int) -> bool:
    cn_holidays = holidays.country_holidays('CN')
    if cn_holidays.is_working_day(f"{year}-{month}-{day}"):
        return True
    else:
        return False
