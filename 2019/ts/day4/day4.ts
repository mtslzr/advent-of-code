const passMin = 235741;
const passMax = 706948;

const part1 = () => {
  let validPWs: number[] = [];
  for (let x = passMin; x <= passMax; x++) {
    hasDouble(x) && isAscending(x) && validPWs.push(x);
  }
  console.log(validPWs.length);
}

const part2 = () => {
  let validPWs: number[] = [];
  for (let x = passMin; x <= passMax; x++) {
    hasDouble(x) && hasStrictDouble(x) && isAscending(x) && validPWs.push(x);
  }
  console.log(validPWs.length);
}

const hasDouble = (pw: number): boolean => {
  let digits = pw.toString().split('');
  let y: any;
  for (y in digits) {
    if (digits[y] == digits[y - 1]) {
      return true;
    }
  }
  return false;
}

const hasStrictDouble = (pw: number): boolean => {
  let digits = pw.toString().split('');
  let y: any;
  let double = false;
  for (y in digits) {
    if (double && digits[y] != digits[y - 1]) { return true; }
    if (digits[y] == digits[y - 1]) { double = true; }
    if (digits[y] == digits[y - 1] && digits[y] == digits[y - 2]) { double = false; }
  }
  return double;
}

const isAscending = (pw: number): boolean => {
  let digits = pw.toString().split('');
  let y: any;
  for (y in digits) {
    if (digits[y] < digits[y - 1]) {
      return false;
    }
  }
  return true;
}

export { part1, part2 };