package main
import "fmt"
func minDeletionSize(A []string) int {
	if len(A) == 0 {
		return 0
	}
	cnt := 0
    for i := 0; i < len(A[0]); i++ {//col
		for j := 1; j < len(A); j++ {//row
			if A[j][i] < A[j - 1][i] {
				cnt++
				break
			}
		}
	}        
	return cnt
}

func main() {
	strs := []string{"zyx","wvu","tsr"}
	fmt.Println(minDeletionSize(strs))
}