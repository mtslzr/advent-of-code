#!/usr/bin/env python3
"""Answer for Advent of Code, Day 3.1."""


def prune_grid(grid):
    """Count all entries in grid and return answer."""
    answer = 0
    for x, data in grid.items():
        for y, count in data.items():
            if count > 1:
                answer += 1

    return answer


def split_claim(claim):
    """Split claim string and return useful parts."""
    parts = claim.split(' ')

    coords = parts[2].split(',')
    coords[1] = coords[1][:-1]

    size = parts[3].split('x')
    size[1] = size[1].rstrip()

    return {
        'xpos': coords[0],
        'ypos': coords[1],
        'xsize': size[0],
        'ysize': size[1]
    }


def run():
    """Process Elf claims and return overlap."""
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
        print(prune_grid(grid))


if __name__ == '__main__':
    run()
