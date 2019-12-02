package day1

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

// Part1 does the first part.
func Part1() {
	total := 0
	freqs := readInput("day1/input.txt")

	for x := range freqs {
		total += freqs[x]
	}

	fmt.Println(total)
}

// Part2 does the second part.
func Part2() {
	fmt.Println("Part 2")
}

func readInput(file string) []int {
	buf, err := ioutil.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}
	data := strings.Split(string(buf), "\n")
	out := make([]int, len(data))
	for i := range data {
		out[i], _ = strconv.Atoi(data[i])
	}

	return out
}
