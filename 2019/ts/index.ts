import * as day1 from './day1/day1';
import * as day2 from './day2/day2';
import * as day3 from './day3/day3';
import * as day4 from './day4/day4';
import * as day5 from './day5/day5';
import * as day6 from './day6/day6';
import * as day7 from './day7/day7';
import * as day8 from './day8/day8';
import * as day9 from './day9/day9';
import * as day10 from './day10/day10';
import * as day11 from './day11/day11';
import * as day12 from './day12/day12';
import { exists } from 'fs';

let day: any;
switch (process.argv[2]) {
  case "day1":
    day = day1;
    break;
  case "day2":
    day = day2;
    break;
  case "day3":
    day = day3;
    break;
  case "day4":
    day = day4;
    break;
  case "day5":
    day = day5;
    break;
  case "day6":
    day = day6;
    break;
  case "day7":
    day = day7;
    break;
  case "day8":
    day = day8;
    break;
  case "day9":
    day = day9;
    break;
  case "day10":
    day = day10;
    break;
  case "day11":
    day = day11;
    break;
  case "day12":
    day = day12;
    break;
  case "day13":
  case "day14":
  case "day15":
  case "day16":
  case "day17":
  case "day18":
  case "day19":
  case "day20":
  case "day21":
  case "day22":
  case "day23":
  case "day24":
  case "day25":
  default:
    console.log('Day not found.');
    process.exit();
}

day.part1();
day.part2();