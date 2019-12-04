#!/usr/bin/env python3
"""Answer for Advent of Code 2019, Day 4."""

PASS_MIN = 235741
PASS_MAX = 706948


def part1():
    """Test for valid passwords based on given criteria."""
    passwords = []
    for x in range(PASS_MIN, PASS_MAX + 1):
        if not is_six_digits(x):
            continue
        if not in_pw_range(x):
            continue
        if not has_double([i for i in str(x)]):
            continue
        if not is_ascending([i for i in str(x)]):
            continue
        passwords.append(x)
    print(len(passwords))


def part2():
    """."""
    print('Part 2')


def has_double(pw, y=1):
    """Check that password has a double-digit."""
    while y < len(pw):
        if pw[y] == pw[y-1]:
            return True
        y += 1
    return False


def in_pw_range(pw):
    """Check that password is in MIN-MAX range."""
    if pw < PASS_MAX or pw > PASS_MIN:
        return True
    return False


def is_ascending(pw, y=1):
    """Check that password is in ascending order."""
    while y < len(pw):
        if pw[y] < pw[y-1]:
            return False
        y += 1
    return True


def is_six_digits(pw):
    """Check that password is six digits."""
    if len(str(pw)) == 6:
        return True
    return False
