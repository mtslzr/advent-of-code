#!/usr/bin/env python3
"""Answer for Advent of Code 2019, Day 1.1."""

from math import floor


def run():
    """Process list of masses and return total fuel required."""
    fuel = 0
    with open('input.txt', 'r') as file:
        for mass in file:
            fuel += floor(int(mass)/3) - 2
    print(fuel)


if __name__ == '__main__':
    run()
