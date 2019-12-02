<?php

include "day1/day1.php";
include "day2/day2.php";

switch($argv[1]) {
  case "day1":
    $day = new day1;
  break;
  case "day2":
    $day = new day2;
  break;
  case "day3":
  case "day4":
  case "day5":
  case "day6":
  case "day7":
  case "day8":
  case "day9":
  case "day10":
  case "day11":
  case "day12":
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
    echo "Day not found.";
    exit();
}

$day->part1();
$day->part2();

?>