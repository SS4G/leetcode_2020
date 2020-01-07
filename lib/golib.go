package lib
func maxInt2(a, b int) int {
	if a >= b {
		return a
	}
	return b
} 

func minInt2(a, b int) int {
	if a <= b {
		return a
	}
	return b
} 

func maxInts(A []int) int {
	maxVal := A[0]
    for _, val := range A {
		maxVal = maxInt2(val, maxVal)
	}
	return maxVal
}

func minInts(A []int) int {
	minVal := A[0]
    for _, val := range A {
		minVal = minInt2(val, minVal)
	}
	return minVal
}