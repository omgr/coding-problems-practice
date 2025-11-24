/*
Problem: Contains Duplicate
Difficulty: Easy
Pattern: Set for Uniqueness Check

Time Complexity Goal: O(n)
Space Complexity Goal: O(n)
*/

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"strings"
)

/*
containsDuplicate checks if array contains any duplicates

TODO: Implement using map[int]bool as a set
Hint: In Go, maps can simulate sets
*/
func containsDuplicate(nums []int) bool {
	// Create a map to track seen numbers
	// In Go: map[keyType]valueType
	// We use bool as value (true means "seen")
	numTrack := make(map[int]bool)
	
	// range returns (index, value)
	// Use _ to ignore index since we don't need it
	for _, num := range nums {
		// Check if num exists in map
		// Go maps return (value, exists) when looked up
		if _, ok := numTrack[num]; ok {
			return true  // Found duplicate!
		}
		// Mark this number as seen
		numTrack[num] = true
	}
	
	return false
}

type TestCase struct {
	ID          int    `json:"id"`
	Description string `json:"description"`
	Input       struct {
		Nums []int `json:"nums"`
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
	fmt.Println("Running Contains Duplicate Tests - Go")
	fmt.Println(strings.Repeat("=", 60))

	passed, failed := 0, 0

	for _, test := range testData.TestCases {
		nums := test.Input.Nums
		expected := test.Expected

		result := containsDuplicate(nums)

		if result == expected {
			fmt.Printf("✅ Test %d: PASSED\n", test.ID)
			passed++
		} else {
			fmt.Printf("❌ Test %d: FAILED - Expected %v, Got %v\n", test.ID, expected, result)
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
	fmt.Println("Quick Test: [1,2,3,1] -> Expected: true")
	fmt.Printf("Your output: %v\n", containsDuplicate([]int{1, 2, 3, 1}))
	fmt.Println()

	runTests()
}

