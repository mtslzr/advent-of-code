#!/usr/bin/env python3
"""Starter script for Advent of Code, 2019."""

from day1 import day1
from day2 import day2
import sys


def run():
    """Parse input and call daily script."""
    days = []
    for x in range(1, 1):
        days.append('day' + x)

    if len(sys.argv) < 2:
        print('Day not found.')
        sys.exit()

    if sys.argv[1] == 'day1':
        day1.part1()
        day1.part2()
    elif sys.argv[1] == 'day2':
        day2.part1()
        day2.part2()
    else:
        print('Day not found.')
        sys.exit()


if __name__ == '__main__':
    run()
