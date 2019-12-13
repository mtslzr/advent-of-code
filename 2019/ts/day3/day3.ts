import * as fs from 'fs';
import { POINT_CONVERSION_COMPRESSED } from 'constants';

interface Current {
  steps: CurrentAB,
  x: CurrentAB,
  y: CurrentAB
}

interface CurrentAB {
  a: number,
  b: number
}

interface Moves {
  a: string[],
  b: string[]
}

const part1 = () => {
  let matches = parseMoves(readInput('day3/input.txt'));
  console.log(findClosestMatch(matches));
}

const part2 = () => {
  let matches = parseMoves(readInput('day3/input.txt'));
  console.log(findShortestMatch(matches));
}

const findClosestMatch = (matches: { [key: string]: { [key: string]: number } }) => {
  let shortDist = 1000000;
  for (let coord in matches) {
    let newDist = coord.split('/')
      .map(Number)
      .reduce((a, b) => Math.abs(a) + Math.abs(b));
    shortDist = newDist < shortDist ? newDist : shortDist;
  }
  return shortDist;
}

const findShortestMatch = (matches: { [key: string]: { [key: string]: number } }) => {
  let shortDist = 1000000;
  for (let x in matches) {
    let newDist = matches[x]['a'] + matches[x]['b'];
    shortDist = newDist < shortDist ? newDist : shortDist;
  }
  return shortDist;
}

const parseMoves = (moves: Moves): { [key: string]: { [key: string]: number } } => {
  let stops = {};
  let current: Current = {
    steps: { a: 0, b: 0 },
    x: { a: 0, b: 0 },
    y: { a: 0, b: 0 }
  }
  let i = 0;

  while (i < Object.keys(moves['a']).length) {
    for (let ab in moves) {
      let moveDir = moves[ab][i].substr(0, 1);
      let moveLen = +moves[ab][i].substr(1);
      while (moveLen > 0) {
        current['steps'][ab]++;
        switch (moveDir) {
          case 'U':
            current['y'][ab]++;
            break;
          case 'D':
            current['y'][ab]--;
            break;
          case 'L':
            current['x'][ab]--;
            break;
          case 'R':
            current['x'][ab]++;
            break;
        }
        let coord = current['x'][ab] + '/' + current['y'][ab];
        if (!(coord in stops)) {
          stops[coord] = {};
        }
        stops[coord][ab] = current['steps'][ab];
        moveLen--;
      }
    }
    i++;
  }

  for (let coord in stops) {
    if (Object.keys(stops[coord]).length < 2) {
      delete stops[coord];
    }
  }

  return stops;
}

const readInput = (file: string): Moves => {
  let data = fs.readFileSync(file)
    .toString()
    .split('\n')
  return {
    'a': data[0].split(','),
    'b': data[1].split(',')
  }
}

export { part1, part2 };