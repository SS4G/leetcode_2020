package main
func sortArrayByParityII(A []int) []int {
	newSlice := make([]int, len(A))
	oddIdx := 1
	evenIdx := 0
	for _, val := range A {
		if val % 2 != 0 {
			newSlice[oddIdx] = val
			oddIdx += 2
		} else {
			newSlice[evenIdx] = val
			evenIdx += 2
		}
	}
	return newSlice
}