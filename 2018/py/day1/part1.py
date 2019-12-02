#!/usr/bin/env python3
"""Answer for Advent of Code, Day 1.1."""


def run():
    """Process input and return frequency."""
    freq = 0
    with open('input.txt', 'r') as file:
        for num in file:
            freq += int(num)
    print(freq)


if __name__ == '__main__':
    run()
