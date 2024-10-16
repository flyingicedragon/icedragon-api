#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from icedragon_api import holidays


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/holidays/{year}/{month}/{day}")
def is_working(year: int, month: int, day: int) -> dict:
    """Reture true if is a workday.

    example: https://api.example.com/2024/1/1
    """
    return {"is_work": holidays.is_working(year, month, day)}
