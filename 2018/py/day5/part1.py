#!/usr/bin/env python3
"""Answer for Advent of Code, Day 5.1."""


def setup():
    """Write input polymer to a variable."""
    with open('input.txt', 'r') as file:
        for line in file:
            return line


def run():
    """Process polymer and print remaining units."""
    polymer = setup()
    position = 0
    while position < len(polymer):
        if position <= 0:
            position = 1
            continue
        else:
            if (polymer[position - 1] != polymer[position]) and \
               (polymer[position - 1].upper() == polymer[position].upper()):
                polymer = polymer[:position - 1] + polymer[position + 1:]
                position -= 2
            else:
                position += 1
    print(len(polymer))


if __name__ == '__main__':
    run()
