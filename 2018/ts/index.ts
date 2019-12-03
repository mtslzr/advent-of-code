import * as day1 from './day1/day1';

switch (process.argv[2]) {
  case "day1":
    day1.part1();
    day1.part2();
    break;
  default:
    console.log('Day not found.');
}