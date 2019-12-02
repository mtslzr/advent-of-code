#!/usr/bin/env python3
"""Answer for Advent of Code 2019, Day 2.1."""


def part1():
    """Rebuild intcode from list."""
    numbers = read_input('./day2/input.txt')

    x = 0
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

    print(numbers[0])


def part2():
    """Do part two."""
    print("Part 2!")


def read_input(filename):
    """Parse input file and return list."""
    with open(filename, 'r') as file:
        for line in file:
            nums = line.split(',')
    x = 0
    for num in nums:
        nums[x] = int(num)
        x += 1

    nums[1] = 12
    nums[2] = 2
    return nums
