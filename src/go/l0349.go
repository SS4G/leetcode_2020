package main
func intersection(nums1 []int, nums2 []int) []int {
	digitMap := make(map[int]bool)
	for _, val := range nums1 {
		digitMap[val] = true
	}

	resultMap := make(map[int]bool)
	for _, val := range nums2 {
		if _, ok := digitMap[val]; ok {
			resultMap[val] = true
		}
	}

	result := make([]int, 0, 1024)
	for k := range(resultMap) {
		result = append(result, k)
	}
	return result
}