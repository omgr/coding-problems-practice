/**
 * Problem: Two Sum
 * Difficulty: Easy
 * Topic: Arrays & Hash Tables
 * Pattern: HashMap Lookup
 * 
 * Problem Statement:
 * Given an array of integers nums and an integer target, return indices of the 
 * two numbers such that they add up to target.
 * 
 * Example:
 *     Input: nums = [2,7,11,15], target = 9
 *     Output: [0,1]
 *     Explanation: nums[0] + nums[1] == 9, so we return [0, 1]
 * 
 * Constraints:
 *     - 2 <= nums.length <= 10^4
 *     - -10^9 <= nums[i] <= 10^9
 *     - -10^9 <= target <= 10^9
 *     - Only one valid answer exists
 * 
 * Time Complexity Goal: O(n)
 * Space Complexity Goal: O(n)
 */

import fs = require('fs');

/**
 * Test case interface
 */
interface TestCase {
    id: number;
    description: string;
    input: {
        nums: number[];
        target: number;
    };
    expected: number[];
    explanation: string;
}

interface TestData {
    problem: string;
    testCases: TestCase[];
}

/**
 * Find two numbers in the array that add up to the target.
 * 
 * @param nums - Array of integers
 * @param target - Target sum
 * @returns Indices of the two numbers
 * 
 * Approach:
 *     TODO: Explain your approach here before implementing
 *     
 *     1. What data structure will you use in TypeScript?
 *     2. Map<number, number> - what does each part represent?
 *     3. How does TypeScript's type system help here?
 * 
 * Implementation Steps:
 *     TODO: Break down your implementation into steps
 *     
 *     Step 1: 
 *     Step 2: 
 *     Step 3: 
 */
function twoSum(nums: number[], target: number): number[] {
    // TODO: Implement your solution here
    
    // Hint: Use Map<number, number> to store numbers you've seen
    // First number is the value, second is the index
    // Key concept: For each number, check if (target - number) exists
    
    // Remove the line below and implement your solution
    const numMap = new Map<number, number>();
    for(let i = 0; i < nums.length; i++){
        const compliment = target - nums[i];
        if(numMap.has(compliment)){
            return [numMap.get(compliment)!,i];
        }
        numMap.set(nums[i],i);
    }
    return [];
}

/**
 * Run all test cases from test-data.json
 */
function runTests(): void {
    // Load test data
    const data: TestData = JSON.parse(fs.readFileSync('test-data.json', 'utf8'));
    
    console.log("=".repeat(60));
    console.log("Running Two Sum Tests - TypeScript");
    console.log("=".repeat(60));
    
    let passed = 0;
    let failed = 0;
    
    for (const test of data.testCases) {
        const { nums, target } = test.input;
        const expected = test.expected;
        
        try {
            const result: number[] = twoSum(nums, target);
            
            // Check if result matches expected (order doesn't matter)
            const resultSorted = [...result].sort((a, b) => a - b);
            const expectedSorted = [...expected].sort((a, b) => a - b);
            const isCorrect = JSON.stringify(resultSorted) === JSON.stringify(expectedSorted);
            
            if (isCorrect) {
                console.log(`✅ Test ${test.id}: PASSED`);
                console.log(`   Input: nums=[${nums}], target=${target}`);
                console.log(`   Output: [${result}]`);
                passed++;
            } else {
                console.log(`❌ Test ${test.id}: FAILED`);
                console.log(`   Input: nums=[${nums}], target=${target}`);
                console.log(`   Expected: [${expected}]`);
                console.log(`   Got: [${result}]`);
                failed++;
            }
            
        } catch (error) {
            console.log(`❌ Test ${test.id}: ERROR`);
            console.log(`   Input: nums=[${nums}], target=${target}`);
            console.log(`   Error: ${(error as Error).message}`);
            failed++;
        }
        
        console.log();
    }
    
    // Summary
    console.log("=".repeat(60));
    console.log(`Results: ${passed} passed, ${failed} failed out of ${passed + failed} tests`);
    console.log("=".repeat(60));
    
    if (passed === data.testCases.length) {
        console.log("🎉 Congratulations! All tests passed!");
        console.log("\nTime Complexity Analysis:");
        console.log("  - What is the time complexity of your solution?");
        console.log("  - Why is it better than brute force O(n²)?");
        console.log("\nSpace Complexity Analysis:");
        console.log("  - What is the space complexity of your solution?");
        console.log("  - What are you storing in memory?");
        console.log("\nTypeScript Benefits:");
        console.log("  - How did type safety help you while coding?");
        console.log("  - What errors did the compiler catch?");
    } else {
        console.log("Keep trying! Debug the failing tests.");
    }
}

// Quick manual test
console.log("Quick Test:");
console.log("Input: [2, 7, 11, 15], target = 9");
console.log("Expected: [0, 1]");
try {
    const result = twoSum([2, 7, 11, 15], 9);
    console.log(`Your output: [${result}]`);
} catch {
    console.log("Your output: Not implemented yet");
}
console.log();

// Uncomment the line below when you're ready to run all tests
runTests();

// Export for use in other files
export { twoSum, runTests };

