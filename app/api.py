#!/usr/bin/env python3

from fastapi import FastAPI

from icedragon_api import holidays


app = FastAPI()


@app.get("/holidays/{year}/{month}/{day}")
def is_working(year: int, month: int, day: int) -> dict:
    """Reture true if is a workday.

    example: https://api.example.com/2024/1/1
    """
    return {"is_work": holidays.is_working(year, month, day)}
