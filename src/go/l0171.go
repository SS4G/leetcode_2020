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
}