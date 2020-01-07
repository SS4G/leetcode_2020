package main
func repeatedNTimes(A []int) int {
	markMap := make(map[int]bool)
	for _, val := range A {
		if _, ok := markMap[val]; ok {
			return val
		} else {
			markMap[val] = true
		}
	}
	return 0
}