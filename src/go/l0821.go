package main
import "fmt"

func minInt2(a, b int) int {
	if a <= b {
		return a
	}
	return b
} 

func shortestToChar(S string, C byte) []int {
	sbytes := []byte(S)
	dist := make([]int, len(S))
	for i := 0; i < len(dist); i++ {
		dist[i] = len(dist)
	} 
   
	for i := 0; i < len(dist); i++ {
		if sbytes[i] == C {
			dist[i] = 0
			for leftOffset := 1; i - leftOffset >= 0 && sbytes[i - leftOffset] != C; leftOffset++ {
				dist[i - leftOffset] = minInt2(dist[i - leftOffset], leftOffset)
			}

			for rightOffset := 1; i + rightOffset < len(sbytes) && sbytes[i + rightOffset] != C; rightOffset++ {
				dist[i + rightOffset] = minInt2(dist[i + rightOffset], rightOffset)
			}
		} else {
			continue
		}
	}

	return dist
}

func main() {
	S := "loveleetcode"
	C := byte('e')
	fmt.Println(byte('e'))
	fmt.Println(shortestToChar(S, C))
	//[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
}