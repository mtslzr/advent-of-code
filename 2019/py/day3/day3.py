#!/usr/bin/env python3
"""Answer for Advent of Code 2019, Day 3."""

import sys


def part1():
    """Find closest cross of two wires."""
    moves = read_input('./day3/input.txt')
    matches = parse_moves(moves)
    print(find_closest_match(matches))


def part2():
    """Find shortest steps to intersection of two wires."""
    moves = read_input('./day3/input.txt')
    matches = parse_moves(moves)
    print(find_shortest_match(matches))


def find_closest_match(matches):
    """Iterate coords and find closest to (0,0)."""
    dist = False
    for match, steps in matches.items():
        coords = match.split('/')
        x = 0
        for coord in coords:
            if coord[0] == '-':
                coords[x] = coord[1:]
            x += 1
        if not dist or (int(coords[0]) + int(coords[1]) < dist):
            dist = int(coords[0]) + int(coords[1])
    return dist


def find_shortest_match(matches):
    """Iterate coords and find fewest steps."""
    dist = False
    for match, steps in matches.items():
        total = steps['a'] + steps['b']
        if not dist or total < dist:
            dist = total
    return dist


def parse_moves(moves):
    """Iterate move sets and return list of crosses."""
    loc = {}
    cur_x = {'a': 0, 'b': 0}
    cur_y = {'a': 0, 'b': 0}
    steps = {'a': 0, 'b': 0}
    i = 0

    while i < len(moves['a']):
        for ab, move in moves.items():
            move_dir = moves[ab][i][0]
            move_len = int(moves[ab][i][1:])
            if move_dir in ['L', 'R', 'U', 'D']:
                cur_x, cur_y, loc, steps = process_move(move_dir, move_len,
                                                        loc, cur_x, cur_y, ab,
                                                        steps)
            else:
                print('Unexpected direction:', move_dir)
                sys.exit()
        i += 1

    matches = {}
    for coord, steps in loc.items():
        if len(steps) == 2:
            matches[coord] = steps

    return matches


def process_move(move_dir, move_len, loc, cur_x, cur_y, ab, steps):
    """Process a single move."""
    while move_len > 0:
        steps[ab] += 1
        if move_dir == 'L':
            cur_x[ab] -= 1
        elif move_dir == 'R':
            cur_x[ab] += 1
        elif move_dir == 'U':
            cur_y[ab] += 1
        else:
            cur_y[ab] -= 1
        coord = str(cur_x[ab]) + '/' + str(cur_y[ab])
        if coord not in loc:
            loc[coord] = {}
        loc[coord][ab] = steps[ab]
        move_len -= 1
    return cur_x, cur_y, loc, steps


def read_input(filename):
    """Parse input file and return list."""
    moves = {'a': [], 'b': []}
    with open(filename, 'r') as file:
        for line in file:
            if len(moves['a']) == 0:
                moves['a'] = line.split(',')
            else:
                moves['b'] = line.split(',')
    return moves
