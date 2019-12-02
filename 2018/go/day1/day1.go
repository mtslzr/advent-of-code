package day1

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
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
	hits := make(map[int]int)
	total := 0
	x := 0
	freqs := readInput("day1/input.txt")

	for x < len(freqs) {
		total += freqs[x]
		if hits[total] == 1 {
			fmt.Println(total)
			os.Exit(0)
		}

		hits[total] = 1

		if (x + 1) == len(freqs) {
			x = 0
		} else {
			x++
		}
	}
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
