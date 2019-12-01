package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("../input.txt")
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
