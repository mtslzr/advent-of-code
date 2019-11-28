#!/usr/bin/env python3
"""Answer for Advent of Code, Day 4.1."""

import re


def setup():
    """Process guard logs and return organized list."""
    logs = []
    with open('input.txt', 'r') as file:
        for entry in file:
            logs.append(entry.rstrip())
    return sorted(logs)


def run():
    """Process Elf claims and return overlap."""
    guards = {}
    guard = minute = None
    fell_asleep = 0
    logs = setup()

    for log in logs:
        if re.search('Guard', log):
            parts = log.split('#')
            parts = parts[1].split(' ')
            guard = parts[0]
            if guard not in guards:
                guards[guard] = {'total': 0, 'mins': {}}
        else:
            parts = log.split(':')
            minute = parts[1][:2]
            if re.search('asleep', log):
                fell_asleep = minute
            else:
                guards[guard]['total'] += (int(minute) - int(fell_asleep))
                for x in range(int(fell_asleep), int(minute)):
                    if x not in guards[guard]['mins']:
                        guards[guard]['mins'][x] = 1
                    else:
                        guards[guard]['mins'][x] += 1

    sleepy_guard = False
    for guard_id, guard in guards.items():
        if not sleepy_guard:
            sleepy_guard = guard_id
        if guard['total'] > guards[sleepy_guard]['total']:
            sleepy_guard = guard_id

    sleepy_minute = False
    for minute, count in guards[sleepy_guard]['mins'].items():
        if not sleepy_minute:
            sleepy_minute = minute
        if count > guards[sleepy_guard]['mins'][sleepy_minute]:
            sleepy_minute = minute

    return (int(sleepy_guard) * int(sleepy_minute))


if __name__ == '__main__':
    print(run())
