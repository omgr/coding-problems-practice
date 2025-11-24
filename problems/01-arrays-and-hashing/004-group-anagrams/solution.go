/*
Problem: Group Anagrams
Difficulty: Medium
Pattern: HashMap + String Processing

Time Complexity Goal: O(n × k) or O(n × k log k)
Space Complexity Goal: O(n × k)
*/

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
)

/*
groupAnagrams groups anagrams together from the input array

TODO: Implement using map[string][]string
Hint: Sort each string and use as key
*/
func groupAnagrams(strs []string) [][]string {
	// TODO: Implement your solution here
	return [][]string{}
}

// Helper function to sort a string
func sortString(s string) string {
	runes := []rune(s)
	sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})
	return string(runes)
}

type TestCase struct {
	ID          int      `json:"id"`
	Description string   `json:"description"`
	Input       struct {
		Strs []string `json:"strs"`
	} `json:"input"`
	Expected [][]string `json:"expected"`
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
	fmt.Println("Running Group Anagrams Tests - Go")
	fmt.Println(strings.Repeat("=", 60))

	passed, failed := 0, 0

	for _, test := range testData.TestCases {
		strs := test.Input.Strs
		expected := test.Expected

		result := groupAnagrams(strs)

		// Sort for comparison (order doesn't matter)
		resultSorted := sortGroups(result)
		expectedSorted := sortGroups(expected)

		if compareGroups(resultSorted, expectedSorted) {
			fmt.Printf("✅ Test %d: PASSED\n", test.ID)
			passed++
		} else {
			fmt.Printf("❌ Test %d: FAILED\n", test.ID)
			fmt.Printf("   Input: %v\n", strs)
			fmt.Printf("   Expected groups: %d\n", len(expected))
			fmt.Printf("   Got groups: %d\n", len(result))
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

// Helper function to sort groups for comparison
func sortGroups(groups [][]string) []string {
	var sorted []string
	for _, group := range groups {
		sort.Strings(group)
		sorted = append(sorted, strings.Join(group, ","))
	}
	sort.Strings(sorted)
	return sorted
}

// Helper function to compare sorted groups
func compareGroups(a, b []string) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println("Quick Test: [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]")
	quickResult := groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"})
	fmt.Printf("Your output: %d groups\n", len(quickResult))
	for _, group := range quickResult {
		fmt.Printf("  %v\n", group)
	}
	fmt.Println()

	runTests()
}



