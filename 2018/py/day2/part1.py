#!/usr/bin/env python3
"""Answer for Advent of Code, Day 2.1."""


def run():
    """Process input and find doubles and triples."""
    doubles = 0
    triples = 0
    with open('input.txt', 'r') as file:
        for box in file:
            letters = {}
            for letter in box:
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1
            for letter in letters:
                if letters[letter] == 2:
                    doubles += 1
                break
            for letter in letters:
                if letters[letter] == 3:
                    triples += 1
                break

    print(doubles * triples)


if __name__ == '__main__':
    run()
