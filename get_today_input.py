import os

import datetime
import requests
from dotenv import load_dotenv

load_dotenv()
AOC_INPUT_URL = "https://adventofcode.com/{year}/day/{day}/input"


def get_aoc_cookie():
    return os.getenv("AOC_SESSION_KEY")


def get_input(day, year=2023):
    session_cookie = {"session": os.getenv("AOC_SESSION_KEY")}
    r = requests.get(AOC_INPUT_URL.format(year=year, day=day), cookies=session_cookie)
    with open(f"./y{year}/day{day}/input.txt", "w") as f:
        f.write(r.text)
    print(f"Input for day {day} saved to ./y{year}/day{day}/input.txt")


if __name__ == "__main__":
    now = datetime.datetime.now()
    # get_input(now.day, now.year)
    get_input(1, now.year)
