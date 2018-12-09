#!/usr/bin/env python3
"""Answer for Advent of Code, Day 6.1."""

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

    for x, spots in grid.items():
        for y, spot in spots.items():
            if grid[x][y] is None:
                closest = [None, None]
                for alpha, coord in coords.items():
                    parts = coord.split(', ')
                    cx = int(parts[0])
                    cy = int(parts[1])
                    if closest[0] is None or \
                       (abs(x-cx) + abs(y-cy)) < sum(closest):
                        closest = [abs(x-cx), abs(y-cy)]
                        grid[x][y] = alpha.lower()
                    elif (abs(x-cx) + abs(y-cy)) == sum(closest):
                        grid[x][y] = '.'

    scoreboard = {}
    for letter in alphabet:
        scoreboard[letter] = 0

    for x, spots in grid.items():
        for y, spot in spots.items():
            if grid[x][y] != '.':
                key = grid[x][y].upper()
                scoreboard[key] += 1

    cheaters = []
    for y, spot in grid[1].items():
        if spot.upper() not in cheaters:
            cheaters.append(spot.upper())
    for y, spot in grid[len(grid)].items():
        if spot.upper() not in cheaters:
            cheaters.append(spot.upper())
    for x, spot in grid.items():
        if spot[1].upper() not in cheaters:
            cheaters.append(spot[1].upper())
        if spot[len(spot)].upper() not in cheaters:
            cheaters.append(spot[len(spot)].upper())

    hiscore = [None, 0]
    for letter, score in scoreboard.items():
        if letter not in cheaters and score > hiscore[1]:
            hiscore = [letter, score]

    print(hiscore)


if __name__ == '__main__':
    run()
