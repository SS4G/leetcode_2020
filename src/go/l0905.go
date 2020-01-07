package main
import "fmt"

func sortArrayByParity(A []int) []int {
	newSlice := make([]int, len(A), len(A))
	oddIdx := len(A) - 1
	evenIdx := 0 
	for _, val := range A {
		if val % 2 == 0 {
			newSlice[evenIdx] = val
			evenIdx++
		} else {
			newSlice[oddIdx] = val
			oddIdx--
		}
	} 
	return newSlice
}

func main() {
    
}