package main
import (
	"strings"
	"fmt"
)

func inRow(word, row string) bool {
	
    for _, c := range []rune(word) {
		//fmt.Println(word, c)
		if !strings.ContainsRune(row, c) {
			return false
		}
	}
	return true
} 


func findWords(words []string) []string {
	row1 := "qwertyuiop"
	row2 := "asdfghjkl"
	row3 := "zxcvbnm"

	result := make([]string, 0, 1000)
	for _, str := range words {
		lowerString := strings.ToLower(str)
		if inRow(lowerString, row1) || inRow(lowerString, row2) || inRow(lowerString, row3) {
			result = append(result, str)
		}
	}
	return result
}

func main() {
	words := []string{"Hello", "Alaska", "Dad", "Peace"}
	fmt.Println(inRow("dad", "asdfghjkl"))
	//fmt.Println(strings.ContainsRune("asdc", 'c'))
	fmt.Println(findWords(words))
}