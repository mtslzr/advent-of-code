#!/usr/bin/env python3
"""Answer for Advent of Code, Day 6.2."""

from string import ascii_uppercase


def setup():
    """Build grid from input coordinates."""
    alphabet = []
    for letter in ascii_uppercase:
        alphabet.append(letter)
    for letter in ascii_uppercase:
        alphabet.append(letter + letter)

    coords = {}
    with open('input.txt', 'r') as file:
        x = 0
        for line in file:
            coords[alphabet[x]] = line.rstrip()
            x += 1

    x = 0
    y = 0
    for alpha, coord in coords.items():
        parts = coord.split(', ')
        if int(parts[0]) > x:
            x = int(parts[0])
        if int(parts[1]) > y:
            y = int(parts[1])

    grid = {}
    for xx in range(1, (x + 1)):
        grid[xx] = {}
        for yy in range(1, (y + 1)):
            grid[xx][yy] = None

    return coords, grid, alphabet


def run():
    """Process coordinates and find largest non-infinite zone."""
    coords, grid, alphabet = setup()

    for alpha, coord in coords.items():
        parts = coord.split(', ')
        x = int(parts[0])
        y = int(parts[1])

        grid[x][y] = alpha

    region = 0
    for x, spots in grid.items():
        for y, spot in spots.items():
            distance = 0
            for alpha, coord in coords.items():
                parts = coord.split(', ')
                cx = int(parts[0])
                cy = int(parts[1])
                distance += abs(x-cx) + abs(y-cy)
                if distance >= 10000:
                    break
            if distance < 10000:
                region += 1

    print(region)


if __name__ == '__main__':
    run()
