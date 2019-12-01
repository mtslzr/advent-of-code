const fs = require('fs');

module.exports = {
  part1: function () {
    let input = fs.readFileSync('day1/input.txt')
      .toString()
      .trim()
      .split("\n");

    let fuel = 0;
    input.forEach(function (mass) {
      fuel += Math.floor(mass / 3) - 2;
    });

    console.log(fuel);
  },

  part2: function () {
    let input = fs.readFileSync('day1/input.txt')
      .toString()
      .trim()
      .split("\n");

    let fuel = 0;
    input.forEach(function (mass) {
      let modFuel = Math.floor(mass / 3) - 2;
      while (modFuel > 0) {
        fuel += modFuel;
        modFuel = Math.floor(modFuel / 3) - 2;
      }
    });

    console.log(fuel);
  }
}