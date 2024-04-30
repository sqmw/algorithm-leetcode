package main

import (
	"fmt"
	"strings"
)

func findWords(words []string) []string {
	// 定义一个目标 []string
	var desStrList []string
	// 构建不同的 set (Go语言没有set，这里使用map实现相同的结果)
	var zeroSet = make(map[int32]bool)
	for _, char := range "qwertyuiop" {
		zeroSet[char] = true
	}

	var oneSet = make(map[int32]bool)
	for _, char := range "asdfghjkl" {
		oneSet[char] = true
	}

	var twoSet = make(map[int32]bool)
	for _, char := range "zxcvbnm" {
		twoSet[char] = true
	}
	// 遍历 word，判断是否在多个集合里面
	for i, word := range words {
		// 对每一个单词进行判定
		word = strings.ToLower(word)
		var wordSet = make(map[int32]int)
		var canAdd bool = true
		for _, char := range word {
			if _, ok := zeroSet[char]; ok {
				wordSet[0]++
			} else if _, ok := oneSet[char]; ok {
				wordSet[1]++
			} else {
				wordSet[2]++
			}
			if len(wordSet) > 1 {
				canAdd = false
				break
			}
		}
		if canAdd {
			desStrList = append(desStrList, words[i])
		}
	}
	return desStrList
}

func main() {
	fmt.Println(findWords([]string{"Hello", "Alaska", "Dad", "Peace"}))
}
