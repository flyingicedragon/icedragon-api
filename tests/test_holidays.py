#!/usr/bin/env python3

import icedragon_api.holidays as holidays


def test_holiday_is() -> None:
    year = 2024
    month = 10
    day = 1
    is_holiday = holidays.is_holiday(year, month, day)
    assert is_holiday is False


def test_holiday_not() -> None:
    year = 2024
    month = 10
    day = 12
    is_holiday = holidays.is_holiday(year, month, day)
    assert is_holiday is True
