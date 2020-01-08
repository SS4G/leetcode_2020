<<<<<<< HEAD
package main
import "fmt"

func powInt(x, n int) int {
    if n == 0 {
		return 1
	} 
	half := powInt(x, n / 2)
	if n % 2 == 0 {
		return half * half
	} 
	return  half * half * x
}

func titleToNumber(s string) int {
	ints := make([]int, 0, 10)
    for _, c := range s {
		ints = append(ints, int(c - 'A'))
	}
	lowLevelLength := len(ints) - 1  
	low_cnt := 0
	if lowLevelLength > 0 {
		low_cnt = 26 * (powInt(26, lowLevelLength) - 1) / (26 - 1)
	}  
	high_cnt := 0
	base := 1
    for i := len(ints) - 1; i >= 0; i-- {
		high_cnt += ints[i] * base
		base *= 26
	}
	return high_cnt + low_cnt + 1
}

func main() {
	fmt.Println(titleToNumber("ZY"))
=======
func titleToNumber(s string) int {
	result := 0
	base = 1
    for i := len(s) - 1; i >= 0; i-- {
		if i == len(s) - 1 {
			result += (byte(s[i]) - byte('A'))
		} else {

		}
		base *= 27
	}
>>>>>>> 98ecf2495b921c46a0ed83383755029bc7a667ad
}