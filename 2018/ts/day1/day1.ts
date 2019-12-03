import * as fs from "fs";

const part1 = () => {
  let total = 0;
  for (let freq of readInput("day1/input.txt")) {
    total += freq;
  }
  console.log(total);
}

const part2 = () => {
  let hits: number[] = [];
  let total = 0;
  let x = 0;
  let freqs = readInput("day1/input.txt");

  while (x < freqs.length) {
    total += freqs[x];
    if (hits.includes(total)) {
      console.log(total);
      process.exit();
    }

    hits.push(total);
    if ((x + 1) == freqs.length) {
      x = 0;
    } else {
      x++;
    }
  }
}

const readInput = (file: string): number[] => {
  return fs.readFileSync(file)
    .toString()
    .trim()
    .split("\n")
    .map(Number);
}

export { part1, part2 };