#!/usr/bin/env python3
"""Answer for Advent of Code, Day 2.2."""


def setup():
    """Return two lists of boxes."""
    boxes = []
    with open('input.txt', 'r') as file:
        for box in file:
            boxes.append(box)
        return boxes


def run():
    """Process boxes and return closest match."""
    source_boxes = setup()
    match_boxes = setup()
    for source in source_boxes:
        for match in match_boxes:
            common = mismatch = position = 0
            for letter in source:
                if letter == match[position]:
                    common += 1
                else:
                    mismatch = position
                    position += 1

        if common == (len(source) - 1):
            return source[:mismatch] + source[mismatch+1:]


if __name__ == '__main__':
    print(run())
