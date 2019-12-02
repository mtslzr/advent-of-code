package main

import (
	"fmt"
	"os"

	"github.com/mtslzr/advent-of-code/2018/go/day1"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Day not found.")
	} else {
		switch os.Args[1] {
		case "day1":
			day1.Part1()
			day1.Part2()
		default:
			fmt.Println("Day not found.")
		}
	}
}
