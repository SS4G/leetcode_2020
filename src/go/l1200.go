import "sort"
func minimumAbsDifference(arr []int) [][]int {
	sort.Ints(arr)
	currntAbs := 10000000 
	results := make([][]int, 0, 100)
	for i := 0; i < len(arr) - 1; i++ {
		absVal := arr[i + 1] - arr[i]
		if absVal < currntAbs {
			currntAbs = absVal
			results = make([][]int, 0, 100)
			pair := make([]int, 2)
			pair[0], pair[1] = arr[i], arr[i + 1]
			results = append(results, pair)
		} else if absVal == currntAbs {
			pair := make([]int, 2)
			pair[0], pair[1] = arr[i], arr[i + 1]
			results = append(results, pair)
		} 
	}
	return results
}