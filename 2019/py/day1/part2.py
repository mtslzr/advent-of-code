#!/usr/bin/env python3
"""Answer for Advent of Code 2019, Day 1.2."""

from math import floor


def run():
    """Process list of masses and return total fuel required."""
    total_fuel = 0
    with open('input.txt', 'r') as file:
        for mass in file:
            module_fuel = floor(int(mass)/3) - 2
            while module_fuel > 0:
                total_fuel += module_fuel
                module_fuel = floor(int(module_fuel)/3) - 2
    print(total_fuel)


if __name__ == '__main__':
    run()
