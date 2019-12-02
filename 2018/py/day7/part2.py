#!/usr/bin/env python3
"""Answer for Advent of Code, Day 7.2."""

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

    alpha = {}
    points = 1
    for letter in ascii_uppercase:
        alpha[letter] = (60 + points)
        points += 1

    workers = {}
    for x in range(1, 6):
        workers[x] = {
            'job': None,
            'ends': None
        }

    return steps, alpha, workers


def next_step(alpha, steps):
    """Iterate letters and return next available step."""
    for letter, points in alpha.items():
        can_run = True
        for num, step in steps.items():
            if letter == step[1]:
                can_run = False
                break

        if can_run:
            return letter

    return False


def run():
    """Process steps and return build order."""
    steps, alpha, workers = setup()
    seconds = 0
    done = []

    while len(done) < 26:
        for wid, worker in workers.items():
            if worker['ends'] == seconds:
                last_job = worker['job']
                done.append(last_job)
                for num, step in steps.items():
                    if last_job == step[0]:
                        steps[num] = ['', '']
                workers[wid] = {
                    'job': None,
                    'ends': None
                }

        letter = next_step(alpha, steps)
        if letter:
            for wid, worker in workers.items():
                if worker['job'] is None:
                    workers[wid] = {
                        'job': letter,
                        'ends': (seconds + alpha[letter])
                    }
                    del alpha[letter]
                    break
        else:
            if len(done) < 26:
                seconds += 1
            else:
                break

    print(seconds)


if __name__ == '__main__':
    run()
