#!/usr/bin/env python3
"""Answer for Advent of Code, Day 1.2."""


def run(freq, vals, done):
    """Process input and return frequency."""
    with open('input.txt', 'r') as file:
        for num in file:
            freq += int(num)
            if freq not in vals:
                vals.append(freq)
            else:
                return freq, vals, True
    return freq, vals, False


if __name__ == '__main__':
    done = False
    freq = 0
    vals = []
    while not done:
        freq, vals, done = run(freq, vals, done)
    print(freq)
