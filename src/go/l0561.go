package main
import (
	"sort"
	"fmt"
)

func arrayPairSum(nums []int) int {
	sort.Ints(nums)
	sumedVal := 0
	for idx, val := range nums {
		if idx % 2 == 0 {
			sumedVal += val
		}
	}
	return sumedVal
}

func main() {
	fmt.Println(arrayPairSum([]int{1, 4, 2, 3}))
} 