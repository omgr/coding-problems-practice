/**
 * Problem: Contains Duplicate
 * Difficulty: Easy
 * Pattern: Set for Uniqueness Check
 * 
 * Time Complexity Goal: O(n)
 * Space Complexity Goal: O(n)
 */

const fs = require('fs');

/**
 * Check if array contains any duplicates
 * @param {number[]} nums - Array of integers
 * @returns {boolean} - True if duplicates exist
 */
function containsDuplicate(nums) {
    // TODO: Implement using Set
    // Hint: Set automatically handles uniqueness
    
    return false;
}

function runTests() {
    const data = JSON.parse(fs.readFileSync('test-data.json', 'utf8'));
    
    console.log("=".repeat(60));
    console.log("Running Contains Duplicate Tests - JavaScript");
    console.log("=".repeat(60));
    
    let passed = 0, failed = 0;
    
    for (const test of data.testCases) {
        const { nums } = test.input;
        const expected = test.expected;
        
        try {
            const result = containsDuplicate(nums);
            
            if (result === expected) {
                console.log(`✅ Test ${test.id}: PASSED`);
                passed++;
            } else {
                console.log(`❌ Test ${test.id}: FAILED - Expected ${expected}, Got ${result}`);
                failed++;
            }
        } catch (error) {
            console.log(`❌ Test ${test.id}: ERROR - ${error.message}`);
            failed++;
        }
        console.log();
    }
    
    console.log("=".repeat(60));
    console.log(`Results: ${passed} passed, ${failed} failed`);
    console.log("=".repeat(60));
    
    if (passed === data.testCases.length) {
        console.log("🎉 All tests passed!");
    }
}

console.log("Quick Test: [1,2,3,1] -> Expected: true");
console.log(`Your output: ${containsDuplicate([1, 2, 3, 1])}`);
console.log();

// runTests();

module.exports = { containsDuplicate, runTests };

