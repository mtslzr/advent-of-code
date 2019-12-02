import * as fs from "fs";

export function part1() {
  let input = fs.readFileSync('day1/input.txt')
    .toString()
    .trim()
    .split("\n");

  let fuel = 0;
  input.forEach(function (mass) {
    fuel += calculate_fuel(+mass);
  });

  console.log(fuel);
}

export function part2() {
  let input = fs.readFileSync('day1/input.txt')
    .toString()
    .trim()
    .split("\n");

  let fuel = 0;
  input.forEach(function (mass) {
    let modFuel = calculate_fuel(+mass);
    while (modFuel > 0) {
      fuel += modFuel;
      modFuel = calculate_fuel(modFuel);
    }
  });

  console.log(fuel);
}

function calculate_fuel(mass: number): number {
  return Math.floor(mass / 3) - 2;
}