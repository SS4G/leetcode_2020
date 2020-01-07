package main
func uniqueOccurrences(arr []int) bool {
	cntMap := make(map[int]int)
	markMap := make(map[int]bool) 
    for _, val := range arr {
		if _, ok := cntMap[val]; ok {
			cntMap[val]++
		} else {
			cntMap[val] = 1
		}
	}

	for k, v := range cntMap {
		if _, ok := markMap[v]; ok {
			return false
		} else {
			markMap[v] = true
		}
	}
	return true
}