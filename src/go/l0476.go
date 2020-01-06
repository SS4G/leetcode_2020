package main
import "fmt"
func findComplement(num int) int {
	var mask uint32 = 0 
	var i uint8
    for i = 0; i < 32; i++ {
		if num & (0x80000000 >> i) != 0 {
			break
		} else {
			mask += (0x80000000 >> i)
		}
	} 
	return (^num) & int(^mask)
}

func main() {
    fmt.Println(findComplement(5))
}