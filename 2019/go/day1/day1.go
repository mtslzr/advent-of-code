package day1

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

// Part1 calculates total fuel for provided data.
func Part1() {
	file, err := os.Open("day1/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	fuel := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		mass, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}

		fuel += mass/3 - 2
	}

	fmt.Println(fuel)
}

// Part2 calculates total fuel, including fuel modules.
func Part2() {
	file, err := os.Open("day1/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	totalFuel := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		mass, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}

		moduleFuel := mass/3 - 2
		for moduleFuel > 0 {
			totalFuel += moduleFuel
			moduleFuel = moduleFuel/3 - 2
		}
	}

	fmt.Println(totalFuel)
}

func main() {
	Part1()
	Part2()
}
