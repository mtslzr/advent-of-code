import * as fs from "fs";

const part1 = () => {
  let nums = runIntcode(readInput('day2/input.txt'));
  console.log(nums[0]);
}

const part2 = () => {
  console.log("Part 2");
}

const readInput = (file: string): number[] => {
  return fs.readFileSync(file)
    .toString()
    .trim()
    .split(",")
    .map(Number);
}

const runIntcode = (nums: number[], noun: number = 12, verb: number = 2): number[] => {
  let x = 0;
  nums[1] = noun;
  nums[2] = verb;

  while (x < nums.length) {
    if (nums[x] == 99) {
      break;
    }

    let a = nums[x + 1];
    let b = nums[x + 2];
    let c = nums[x + 3];

    if (nums[x] == 1) {
      nums[c] = nums[a] + nums[b];
    } else if (nums[x] == 2) {
      nums[c] = nums[a] * nums[b];
    } else {
      console.log("Unexpected optcode", nums[x]);
    }
    x += 4;
  }

  return nums;
}

export { part1, part2 };