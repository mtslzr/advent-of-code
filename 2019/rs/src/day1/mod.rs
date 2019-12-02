use std::fs::File;
use std::io::{BufRead, BufReader, Lines};

pub fn part1() {
  let file = read_input("./src/day1/input.txt");

  let mut fuel: i32 = 0;
  for line in file {
    let mass = line.expect("Unable to read input.");
    fuel += calculate_fuel(mass.parse::<i32>().unwrap());
  }

  println!("{}", fuel);
}

pub fn part2() {
  let file = read_input("./src/day1/input.txt");

  let mut total_fuel: i32 = 0;
  for line in file {
    let mass = line.expect("Unable to read input.");
    let mut module_fuel = calculate_fuel(mass.parse::<i32>().unwrap());
    while module_fuel > 0 {
      total_fuel += module_fuel;
      module_fuel = calculate_fuel(module_fuel);
    }
  }

  println!("{}", total_fuel);
}

fn calculate_fuel(mass: i32) -> i32 {
  (mass / 3) - 2
}

fn read_input(file: &str) -> Lines<BufReader<File>> {
  let f = File::open(file).unwrap();
  let f = BufReader::new(f);
  return f.lines();
}
