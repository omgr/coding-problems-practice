/*
Problem: Valid Anagram
Difficulty: Easy
Pattern: Character Frequency Counting

Time Complexity Goal: O(n)
Space Complexity Goal: O(1)
*/

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"strings"
)

/*
isAnagram checks if t is an anagram of s

TODO: Implement using map[rune]int for frequency counting
Hint: rune is used for Unicode characters in Go
*/
func isAnagram(s string, t string) bool {
	// TODO: Implement your solution here
	
	return false
}

type TestCase struct {
	ID          int    `json:"id"`
	Description string `json:"description"`
	Input       struct {
		S string `json:"s"`
		T string `json:"t"`
	} `json:"input"`
	Expected bool `json:"expected"`
}

type TestData struct {
	Problem   string     `json:"problem"`
	TestCases []TestCase `json:"testCases"`
}

func runTests() {
	data, err := ioutil.ReadFile("test-data.json")
	if err != nil {
		fmt.Printf("Error reading test file: %v\n", err)
		return
	}

	var testData TestData
	json.Unmarshal(data, &testData)

	fmt.Println(strings.Repeat("=", 60))
	fmt.Println("Running Valid Anagram Tests - Go")
	fmt.Println(strings.Repeat("=", 60))

	passed, failed := 0, 0

	for _, test := range testData.TestCases {
		s := test.Input.S
		t := test.Input.T
		expected := test.Expected

		result := isAnagram(s, t)

		if result == expected {
			fmt.Printf("✅ Test %d: PASSED\n", test.ID)
			passed++
		} else {
			fmt.Printf("❌ Test %d: FAILED\n", test.ID)
			fmt.Printf("   Input: s=\"%s\", t=\"%s\"\n", s, t)
			fmt.Printf("   Expected: %v, Got: %v\n", expected, result)
			failed++
		}
		fmt.Println()
	}

	fmt.Println(strings.Repeat("=", 60))
	fmt.Printf("Results: %d passed, %d failed\n", passed, failed)
	fmt.Println(strings.Repeat("=", 60))

	if passed == len(testData.TestCases) {
		fmt.Println("🎉 All tests passed!")
	}
}

func main() {
	fmt.Println("Quick Test: s=\"anagram\", t=\"nagaram\" -> Expected: true")
	fmt.Printf("Your output: %v\n", isAnagram("anagram", "nagaram"))
	fmt.Println()

	// runTests()
}

