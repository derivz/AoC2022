import os

import datetime
import requests
from dotenv import load_dotenv

load_dotenv()
AOC_INPUT_URL = "https://adventofcode.com/2022/day/{day}/input"


def get_aoc_cookie():
    return os.getenv("AOC_SESSION_KEY")


def get_input(day):
    session_cookie = {"session": os.getenv("AOC_SESSION_KEY")}
    r = requests.get(AOC_INPUT_URL.format(day=day), cookies=session_cookie)
    with open(f"./day{day}/input.txt", "w") as f:
        f.write(r.text)
    print(f"Input for day {day} saved to ./day{day}/input.txt")


if __name__ == "__main__":
    current_day = datetime.datetime.now().day
    get_input(current_day)
