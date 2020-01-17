func lemonadeChange(bills []int) bool {
	cashCnt := make(map[int]int)
	cashCnt[5] = 0
	cashCnt[10] = 0
	cashCnt[20] = 0
	for _, val := range bills {
		switch val {
		case 5: 
			cashCnt[5]++
		case 10: 
			cashCnt[10]++
			if cashCnt[5] <= 0 {
				return false
			}
			cashCnt[5]-- 
		case 20: 
			if (cashCnt[10] <= 0 && cashCnt[5] < 3) || cashCnt[5] < 1 {
				return false
			} else if cashCnt[10] > 0 {
				cashCnt[10]-- 
				cashCnt[5]--
			} else {
				cashCnt[5] -= 3
			}
		}
	}
	return true	
}