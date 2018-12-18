#!/usr/bin/env python3
"""Answer for Advent of Code, Day 7.1."""

from string import ascii_uppercase


def setup():
    """Build list from steps in input."""
    steps = {}
    with open('input.txt', 'r') as file:
        x = 0
        for step in file:
            parts = step.split(' ')
            steps[x] = [parts[1], parts[7]]
            x += 1

    alpha = []
    for letter in ascii_uppercase:
        alpha.append(letter)

    return steps, alpha


def run():
    """Process steps and return build order."""
    steps, alpha = setup()
    order = []

    while len(order) < 26:
        for letter in alpha:
            can_run = True
            for num, step in steps.items():
                if letter == step[1]:
                    can_run = False
                    break

            if can_run:
                break

        order.append(letter)
        alpha.remove(letter)
        for num, step in steps.items():
            if letter == step[0]:
                steps[num] = ['', '']

    print(''.join(order))


if __name__ == '__main__':
    run()
