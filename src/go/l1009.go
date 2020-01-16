package main
import "fmt"
func bitwiseComplement(N int) int {
    if N == 0 {
        return 1
    }
	leadingZeroMask := 0
	for i := 31; i >= 0; i-- {
		if (N & (1 << i)) == 0 {
			//fmt.Println(i)
			leadingZeroMask += (1 << i)
		} else {
			break
		}
	}
	//fmt.Printf("%x\n", (^leadingZeroMask) & 0xffffffff)
	return (^N) & ((^leadingZeroMask) & 0xffffffff)
}

func main() {
    fmt.Println(bitwiseComplement(5))
}