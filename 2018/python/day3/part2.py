#!/usr/bin/env python3
"""Answer for Advent of Code, Day 3.2."""


def build_grid():
    """Build initial grid of claims."""
    grid = {}
    with open('input.txt', 'r') as file:
        for claim in file:
            data = split_claim(claim)
            xstart = (int(data['xpos']) + 1)
            xend = (xstart + int(data['xsize']))
            for x in range(xstart, xend):
                if x not in grid:
                    grid[x] = {}
                ystart = (int(data['ypos']) + 1)
                yend = (ystart + int(data['ysize']))
                for y in range(ystart, yend):
                    if y not in grid[x]:
                        grid[x][y] = 1
                    else:
                        grid[x][y] += 1
    return grid


def split_claim(claim):
    """Split claim string and return useful parts."""
    parts = claim.split(' ')

    coords = parts[2].split(',')
    coords[1] = coords[1][:-1]

    size = parts[3].split('x')
    size[1] = size[1].rstrip()

    return {
        'id': parts[0][1:],
        'xpos': coords[0],
        'ypos': coords[1],
        'xsize': size[0],
        'ysize': size[1]
    }


def run():
    """Process Elf claims and return overlap."""
    grid = build_grid()
    with open('input.txt', 'r') as file:
        found_it = False
        for claim in file:
            data = split_claim(claim)
            if not found_it:
                found_it = True
                xstart = (int(data['xpos']) + 1)
                xend = (xstart + int(data['xsize']))
                for x in range(xstart, xend):
                    ystart = (int(data['ypos']) + 1)
                    yend = (ystart + int(data['ysize']))
                    for y in range(ystart, yend):
                        if grid[x][y] != 1:
                            found_it = False
            else:
                return (int(data['id']) - 1)


if __name__ == '__main__':
    print(run())
