#!/usr/bin/env python3
"""Answer for Advent of Code, Day 5.1."""

from string import ascii_lowercase


def setup():
    """Write input polymer to a variable."""
    with open('input.txt', 'r') as file:
        for line in file:
            return line


def react_polymer(polymer):
    """Process polymer and return length."""
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
    return len(polymer)


def run():
    """Process polymer and print remaining units."""
    low_score = None
    for letter in ascii_lowercase:
        polymer = setup()
        polymer = polymer.replace(letter, '')
        polymer = polymer.replace(letter.upper(), '')

        new_score = react_polymer(polymer)
        if not low_score or new_score < low_score:
            low_score = new_score
    print(low_score)


if __name__ == '__main__':
    run()
