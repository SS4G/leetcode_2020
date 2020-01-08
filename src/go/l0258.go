package main

import (
	"strconv"
	"fmt")

func sumDigits(x int) int {
	sumVal := 0
    for _, c := range strconv.Itoa(x) {
		sumVal += int(c - '0')
	}
	//fmt.Println(sumVal)
	return sumVal
}

func addDigits(num int) int {
	n := num
	for n >= 10 {
		n = sumDigits(n)
	}
	return n
}

func main() {
    fmt.Println(addDigits(38))
}