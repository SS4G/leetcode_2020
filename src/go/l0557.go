package main
import (
	"strings"
	"fmt"
)

func reverseWord(word string) string {
	bytesArray := []byte(word)
	bytesArrayCopy := bytesArray
	for i := 0; i < len(bytesArrayCopy) / 2; i++ {
		invIdx := len(bytesArray) - 1 - i
		bytesArrayCopy[i], bytesArrayCopy[invIdx] = bytesArrayCopy[invIdx], bytesArrayCopy[i]
	}
	return string(bytesArrayCopy)
}

func reverseWords(s string) string {
	strs := strings.Fields(s)
	reversedStrs := []string{}
	for _, str := range strs {
		reversedStrs = append(reversedStrs, reverseWord(str))
	}
	return strings.Join(reversedStrs, " ")
}

func main() {
    fmt.Println(reverseWords("Let's take LeetCode contest"))
}