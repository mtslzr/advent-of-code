package day2

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

// Part1 processes intcode and returns first value.
func Part1() {
	nums := runIntcode(readInput("day2/input.txt"), 12, 2)
	fmt.Println(nums[0])
}

// Part2 processes combinations of intcodes and finds a specific first value.
func Part2() {
	x := 0
	y := 0
	for x < 99 {
		for y < 99 {
			nums := runIntcode(readInput("day2/input.txt"), x, y)
			if nums[0] == 19690720 {
				fmt.Println((100*x + y))
				os.Exit(1)
			}
			y++
		}
		x++
		y = 0
	}
}

func main() {
	Part1()
	Part2()
}

func readInput(file string) []int {
	buf, err := ioutil.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}

	data := strings.Split(string(buf), ",")
	out := make([]int, len(data))
	for i := range data {
		out[i], _ = strconv.Atoi(data[i])
	}

	return out
}

func runIntcode(nums []int, noun int, verb int) []int {
	nums[1] = noun
	nums[2] = verb

	x := 0
	for x < len(nums) {
		if nums[x] == 99 {
			break
		}

		a := nums[x+1]
		b := nums[x+2]
		c := nums[x+3]

		if nums[x] == 1 {
			nums[c] = nums[a] + nums[b]
		} else if nums[x] == 2 {
			nums[c] = nums[a] * nums[b]
		} else {
			fmt.Printf("Unexpected optcode: %d", nums[x])
		}

		x += 4
	}

	return nums
}
