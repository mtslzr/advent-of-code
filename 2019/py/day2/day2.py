#!/usr/bin/env python3
"""Answer for Advent of Code 2019, Day 2."""

import sys


def part1():
    """Rebuild intcode from list."""
    numbers = run_intcode(read_input('./day2/input.txt'))
    print(numbers[0])


def part2():
    """Rebuild intcode from list."""
    x = y = 0
    while x <= 99:
        while y <= 99:
            out = run_intcode(read_input('./day2/input.txt'), x, y)
            if out[0] == 19690720:
                print((100 * x + y))
                sys.exit()
            y += 1
        x += 1
        y = 0


def read_input(filename):
    """Parse input file and return list."""
    with open(filename, 'r') as file:
        for line in file:
            nums = line.split(',')
    x = 0
    for num in nums:
        nums[x] = int(num)
        x += 1

    return nums


def run_intcode(numbers, noun=12, verb=2):
    """Process intcode and return result."""
    x = 0
    numbers[1] = noun
    numbers[2] = verb

    for num in numbers:
        if numbers[x] == 99:
            break

        a = numbers[x+1]
        b = numbers[x+2]
        c = numbers[x+3]

        if numbers[x] == 1:
            numbers[c] = numbers[a] + numbers[b]
        elif numbers[x] == 2:
            numbers[c] = numbers[a] * numbers[b]
        else:
            print('Something went wrong; got opcode {}'.format(numbers[x]))
        x += 4

    return numbers
