package day1

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

type Elf struct {
	Calories     []int // All data by all elfs
	TotalCal     []int // All caloires by one Elf
	TotalMaxCal  []int // All max calories by elf
	BiggestValue int   // Biggest Calorie value
}

func (e Elf) calculateMaxCal() int {
	for _, v := range e.Calories {
		e.TotalCal = append(e.TotalCal, v)
		if v == 0 {
			var m int
			for i := 0; i < len(e.TotalCal); i++ {
				m = m + e.TotalCal[i]
			}
			e.TotalMaxCal = append(e.TotalMaxCal, m)
			e.TotalCal = nil
		}
	}
	maxValue := e.calculateMaxValue()
	return maxValue
}

func (e Elf) calculateMaxValue() int {
	m := e.TotalMaxCal[0]
	for _, cal := range e.TotalMaxCal {
		if cal > m {
			m = cal
		}
	}
	return m
}

func main() {
	var e Elf
	//var cal []byte
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	r := bufio.NewScanner(f)
	//read := true
	for r.Scan() {
		if r.Text() != "" || r.Text() != "\n" {
			cal, _ := strconv.Atoi(r.Text())
			e.Calories = append(e.Calories, cal)
		}
	} // End of loop

	v := e.calculateMaxCal()
	fmt.Println(v)
}
