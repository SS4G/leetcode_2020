package main 

func hammingDistance(x int, y int) int {
	dist := x ^ y
	cnt := 0
    for i := 0; i < 32; i++ {
		if ((dist & (0x01 << i)) != 0 ) {
			cnt++
		}
	}
	return cnt
}

func main() {

}