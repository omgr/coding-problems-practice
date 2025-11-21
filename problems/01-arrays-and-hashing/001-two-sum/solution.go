/*
Problem: Two Sum
Difficulty: Easy
Topic: Arrays & Hash Tables
Pattern: HashMap Lookup

Problem Statement:
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists

Time Complexity Goal: O(n)
Space Complexity Goal: O(n)
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
TwoSum finds two numbers in the array that add up to the target.

Parameters:
  - nums: Slice of integers
  - target: Target sum

Returns:
  - Slice containing indices of the two numbers

Approach:
    TODO: Explain your approach here before implementing

    1. What data structure will you use in Go?
    2. map[int]int - what does each part represent?
    3. How will you find the complement?

Implementation Steps:
    TODO: Break down your implementation into steps

    Step 1:
    Step 2:
    Step 3:
*/
func twoSum(nums []int, target int) []int {
	// TODO: Implement your solution here

	// Hint: Use map[int]int to store numbers you've seen
	// Key is the number, Value is the index
	// Key concept: For each number, check if (target - number) exists

	// Remove the line below and implement your solution
	return []int{}
}

// TestCase represents a single test case
type TestCase struct {
	ID          int    `json:"id"`
	Description string `json:"description"`
	Input       struct {
		Nums   []int `json:"nums"`
		Target int   `json:"target"`
	} `json:"input"`
	Expected    []int  `json:"expected"`
	Explanation string `json:"explanation"`
}

// TestData represents the entire test data structure
type TestData struct {
	Problem   string     `json:"problem"`
	TestCases []TestCase `json:"testCases"`
}

// runTests runs all test cases from test-data.json
func runTests() {
	// Load test data
	data, err := ioutil.ReadFile("test-data.json")
	if err != nil {
		fmt.Printf("Error reading test file: %v\n", err)
		return
	}

	var testData TestData
	err = json.Unmarshal(data, &testData)
	if err != nil {
		fmt.Printf("Error parsing test data: %v\n", err)
		return
	}

	fmt.Println(strings.Repeat("=", 60))
	fmt.Println("Running Two Sum Tests - Go")
	fmt.Println(strings.Repeat("=", 60))

	passed := 0
	failed := 0

	for _, test := range testData.TestCases {
		nums := test.Input.Nums
		target := test.Input.Target
		expected := test.Expected

		result := twoSum(nums, target)

		// Check if result matches expected (order doesn't matter)
		resultSorted := make([]int, len(result))
		copy(resultSorted, result)
		sort.Ints(resultSorted)

		expectedSorted := make([]int, len(expected))
		copy(expectedSorted, expected)
		sort.Ints(expectedSorted)

		isCorrect := len(resultSorted) == len(expectedSorted)
		if isCorrect {
			for i := range resultSorted {
				if resultSorted[i] != expectedSorted[i] {
					isCorrect = false
					break
				}
			}
		}

		if isCorrect {
			fmt.Printf("✅ Test %d: PASSED\n", test.ID)
			fmt.Printf("   Input: nums=%v, target=%d\n", nums, target)
			fmt.Printf("   Output: %v\n", result)
			passed++
		} else {
			fmt.Printf("❌ Test %d: FAILED\n", test.ID)
			fmt.Printf("   Input: nums=%v, target=%d\n", nums, target)
			fmt.Printf("   Expected: %v\n", expected)
			fmt.Printf("   Got: %v\n", result)
			failed++
		}

		fmt.Println()
	}

	// Summary
	fmt.Println(strings.Repeat("=", 60))
	fmt.Printf("Results: %d passed, %d failed out of %d tests\n", passed, failed, passed+failed)
	fmt.Println(strings.Repeat("=", 60))

	if passed == len(testData.TestCases) {
		fmt.Println("🎉 Congratulations! All tests passed!")
		fmt.Println("\nTime Complexity Analysis:")
		fmt.Println("  - What is the time complexity of your solution?")
		fmt.Println("  - Why is it better than brute force O(n²)?")
		fmt.Println("\nSpace Complexity Analysis:")
		fmt.Println("  - What is the space complexity of your solution?")
		fmt.Println("  - What are you storing in memory?")
		fmt.Println("\nGo Specific:")
		fmt.Println("  - How does Go's map work differently from other languages?")
		fmt.Println("  - What is the zero value for maps?")
	} else {
		fmt.Println("Keep trying! Debug the failing tests.")
	}
}

func main() {
	// Quick manual test
	fmt.Println("Quick Test:")
	fmt.Println("Input: [2, 7, 11, 15], target = 9")
	fmt.Println("Expected: [0, 1]")
	result := twoSum([]int{2, 7, 11, 15}, 9)
	fmt.Printf("Your output: %v\n", result)
	fmt.Println()

	// Uncomment the line below when you're ready to run all tests
	// runTests()
}

