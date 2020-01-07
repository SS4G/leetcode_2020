package main
func maxInt2(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
} 

func minInt2(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
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

func smallestRangeI(A []int, K int) int {
	amax := maxInts(A)
	amin := minInts(A)
	if amax - amin > 2 * K {
		return amax - amin - 2 * K
	} 
	return 0
}