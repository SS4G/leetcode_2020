package main 

import (
	"fmt"
	"sort"
)

func sortedSquares(A []int) []int {
	array := []int{}
	for _, val := range A {
		array = append(array, val * val)
	}
	sort.Ints(array)
	return array
}

func main() {
	A := []int{1, 3, 4, 2, 1}
	fmt.Println(sortedSquares(A))
}