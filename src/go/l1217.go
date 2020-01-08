package main
func minInt2(a, b int) int {
	if a <= b {
		return a
	}
	return b
} 


func minCostToMoveChips(chips []int) int {
	oddCnt := 0
	evenCnt := 0
	for _, c := range chips {
		if c & 1 != 0 {
			oddCnt++
		} else {
			evenCnt++
		}
	}
	return minInt2(evenCnt, oddCnt)
}