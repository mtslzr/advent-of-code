package main

import (
	"fmt"
	"os"

	"github.com/mtslzr/advent-of-code/2019/go/day1"
	"github.com/mtslzr/advent-of-code/2019/go/day2"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Day not found.")
	} else {
		switch os.Args[1] {
		case "day1":
			day1.Part1()
			day1.Part2()
		case "day2":
			day2.Part1()
			day2.Part2()
		default:
			fmt.Println("Day not found.")
		}
	}
}
