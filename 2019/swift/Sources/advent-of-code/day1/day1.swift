import Foundation

class Day1 {
  public func part1() {
    var fuel = 0
    let list = read_input(file: "day1/input.txt")
    for mass in list {
      fuel += Int((Double(mass) / 3).rounded(.down) - 2)
    }
    print(fuel)
  }

  public func part2() {
    var total_fuel = 0
    let list = read_input(file: "day1/input.txt")
    for mass in list {
      var module_fuel = Int((Double(mass) / 3).rounded(.down) - 2)
      while module_fuel > 0 {
        total_fuel += module_fuel
        module_fuel = Int((Double(module_fuel) / 3).rounded(.down) - 2)
      }
    }
    print(total_fuel)
  }

  private func read_input(file: String) -> [Int] {
    return try! String(contentsOfFile: file, encoding: .utf8)
                      .components(separatedBy: "\n")
                      .map { Int($0) ?? 0 }
  }
}