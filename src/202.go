package main
import (
	"fmt"
)
func toDigits(x int) []int {
	digits := []int{}
	for x > 0 {
		digits = append(digits, x % 10)
		x /= 10
	}
	return digits
}

func isHappy(n int) bool {
	exists := make(map[int]bool)
	currentVal := n
	for currentVal != 1 {
		digits := toDigits(currentVal)
		currentVal = 0
		for _, val := range digits {
			currentVal += val * val
		}
		if _, ok := exists[currentVal]; ok {
			return false
		} else {
			exists[currentVal] = true
		}
	}
	return true
}

func main() {
	var a = 12345
	fmt.Println(isHappy(a))
}