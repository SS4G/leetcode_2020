package main
import "fmt"
func transpose(A [][]int) [][]int {
	transposedMat := make([][]int, len(A[0]))
	for i := 0; i < len(A[0]); i++ {
		transposedMat[i] = make([]int, len(A))
		//transposedMat = append(transposedMat, )
	}

    for r := 0; r < len(A); r++ {
		for c := 0; c < len(A[0]); c++ {
			transposedMat[c][r] = A[r][c]
		}
	}
	return transposedMat
}

func main() {
	A := [][]int{{1,2,3},{4,5,6}}
	fmt.Println(transpose(A))
}