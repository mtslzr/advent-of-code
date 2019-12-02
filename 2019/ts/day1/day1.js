"use strict";
exports.__esModule = true;
var fs = require("fs");
function part1() {
    var input = fs.readFileSync('day1/input.txt')
        .toString()
        .trim()
        .split("\n");
    var fuel = 0;
    input.forEach(function (mass) {
        fuel += calculate_fuel(+mass);
    });
    console.log(fuel);
}
exports.part1 = part1;
function part2() {
    var input = fs.readFileSync('day1/input.txt')
        .toString()
        .trim()
        .split("\n");
    var fuel = 0;
    input.forEach(function (mass) {
        var modFuel = calculate_fuel(+mass);
        while (modFuel > 0) {
            fuel += modFuel;
            modFuel = calculate_fuel(modFuel);
        }
    });
    console.log(fuel);
}
exports.part2 = part2;
function calculate_fuel(mass) {
    return Math.floor(mass / 3) - 2;
}
