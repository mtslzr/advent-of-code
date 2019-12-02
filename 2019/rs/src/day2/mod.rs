use std::fs::File;
use std::io::prelude::*;
use std::process;

pub fn part1() {
  let nums: Vec<i32> = run_intcode(read_input("./src/day2/input.txt"), 12, 2);
  println!("{}", nums[0]);
}

pub fn part2() {
  let mut x: i32 = 0;
  let mut y: i32 = 0;

  while x <= 99 {
    while y <= 99 {
      let nums: Vec<i32> = run_intcode(read_input("./src/day2/input.txt"), x, y);
      if nums[0] == 19690720 {
        println!("{}", 100 * x + y);
        process::exit(0);
      }
      y += 1;
    }
    x += 1;
    y = 0;
  }
}

fn read_input(file: &str) -> Vec<i32> {
  let mut f = File::open(file).expect("Unable to open input file.");
  let mut contents = String::new();

  f.read_to_string(&mut contents)
    .expect("Unable to read input.");

  let data: Vec<&str> = contents.split_terminator(",").collect();
  data.iter().map(|num| num.parse::<i32>().unwrap()).collect()
}

fn run_intcode(mut nums: Vec<i32>, noun: i32, verb: i32) -> Vec<i32> {
  let mut x: usize = 0;
  nums[1] = noun;
  nums[2] = verb;
  while x < nums.len() {
    if nums[x] == 99 {
      break;
    }

    let a = nums[x + 1] as usize;
    let b = nums[x + 2] as usize;
    let c = nums[x + 3] as usize;

    if nums[x] == 1 {
      nums[c] = nums[a] + nums[b];
    } else if nums[x] == 2 {
      nums[c] = nums[a] * nums[b];
    } else {
      println!("Unexpected optcode: {}", nums[x]);
    }
    x += 4;
  }
  nums
}
