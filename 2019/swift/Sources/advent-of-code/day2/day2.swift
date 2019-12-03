import Foundation

class Day2 {
  public func part1() {
    var nums = read_input(file: "Sources/advent-of-code/day2/input.txt")
    nums = run_intcode(nums: &nums)
    print(nums[0])
  }

  public func part2() {
    var x = 0
    var y = 0
    while x < 99 {
      while y < 99 {
        var nums = read_input(file: "Sources/advent-of-code/day2/input.txt")
        nums = run_intcode(nums: &nums, noun: x, verb: y)
        if nums[0] == 19690720 {
          print(100 * x + y)
          exit(0)
        }
        y += 1
      }
      x += 1
      y = 0
    }
  }

  private func read_input(file: String) -> [Int] {
    return try! String(contentsOfFile: file, encoding: .utf8)
                      .components(separatedBy: ",")
                      .map { Int($0) ?? 0 }
  }

  private func run_intcode(nums: inout [Int], noun: Int = 12, verb: Int = 2) -> [Int] {
    var x = 0
    nums[1] = noun
    nums[2] = verb

    while x < nums.count {
      if nums[x] == 99 {
        break
      }

      let a = nums[x+1]
      let b = nums[x+2]
      let c = nums[x+3]

      if nums[x] == 1 {
        nums[c] = nums[a] + nums[b]
      } else if nums[x] == 2 {
        nums[c] = nums[a] * nums[b]
      } else {
        print("Unexpected optcode: \(nums[x])")
      }
      x += 4
    }

    return nums
  }
}