/**
 * Problem: Contains Duplicate
 * Difficulty: Easy
 * Pattern: Set for Uniqueness Check
 * 
 * Time Complexity Goal: O(n)
 * Space Complexity Goal: O(n)
 */

import * as fs from 'fs';

function containsDuplicate(nums: number[]): boolean {
    // TODO: Implement using Set<number>
    // Hint: Compare Set size with array length
    
    return false;
}

interface TestCase {
    id: number;
    description: string;
    input: { nums: number[] };
    expected: boolean;
}

function runTests(): void {
    const data = JSON.parse(fs.readFileSync('test-data.json', 'utf8'));
    
    console.log("=".repeat(60));
    console.log("Running Contains Duplicate Tests - TypeScript");
    console.log("=".repeat(60));
    
    let passed = 0, failed = 0;
    
    for (const test of data.testCases) {
        const { nums } = test.input;
        const expected: boolean = test.expected;
        
        try {
            const result: boolean = containsDuplicate(nums);
            
            if (result === expected) {
                console.log(`✅ Test ${test.id}: PASSED`);
                passed++;
            } else {
                console.log(`❌ Test ${test.id}: FAILED - Expected ${expected}, Got ${result}`);
                failed++;
            }
        } catch (error) {
            console.log(`❌ Test ${test.id}: ERROR - ${(error as Error).message}`);
            failed++;
        }
        console.log();
    }
    
    console.log("=".repeat(60));
    console.log(`Results: ${passed} passed, ${failed} failed`);
    console.log("=".repeat(60));
}

console.log("Quick Test: [1,2,3,1] -> Expected: true");
console.log(`Your output: ${containsDuplicate([1, 2, 3, 1])}`);
console.log();

// runTests();

export { containsDuplicate, runTests };

