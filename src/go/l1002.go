package main

import "fmt"

func word2Map(str string) map[rune]int {
	wordMap := make(map[rune]int)
    for _, r := range str {
		if _, ok := wordMap[r]; ok {
			wordMap[r]++
		} else {
			wordMap[r] = 1
		}
	}
	return wordMap
}

func minInt2(a, b int) int {
	if a <= b {
		return a
	}
	return b
} 

func commonChars(A []string) []string {
	var markArray [26]int
	maps := make([]map[rune]int, 0, 100)
    for _, word := range A {
		charMap := word2Map(word)
		maps = append(maps, charMap)
	}
	for _, charMap := range maps {
		for k, _ := range charMap {
			markArray[k - 'a']++
		}
	}
	result := make([]string, 0, 10)
    for i, c := range markArray {
		if c == len(A) { //c is common char
			minVal := 10000000
			for _, charMap := range maps {
				minVal = minInt2(charMap['a' + rune(i)], minVal)
			}
			for j := 0; j < minVal; j++ {
				result = append(result, string([]rune{'a' + rune(i)}))
			}
		} 
	}
	return result
}

func main() {
	words := []string{"bella","label","roller"}
	fmt.Println(commonChars(words))
}