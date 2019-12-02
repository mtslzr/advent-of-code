#!/usr/bin/env python3
"""Answer for Advent of Code 2019, Day 1.1."""

from math import floor


def part1():
    """Process list of masses and return total fuel required."""
    fuel = 0
    with open('./day1/input.txt', 'r') as file:
        for mass in file:
            fuel += floor(int(mass)/3) - 2
    print(fuel)


def part2():
    """Process list of masses and return total fuel required."""
    total_fuel = 0
    with open('./day1/input.txt', 'r') as file:
        for mass in file:
            module_fuel = floor(int(mass)/3) - 2
            while module_fuel > 0:
                total_fuel += module_fuel
                module_fuel = floor(int(module_fuel)/3) - 2
    print(total_fuel)
