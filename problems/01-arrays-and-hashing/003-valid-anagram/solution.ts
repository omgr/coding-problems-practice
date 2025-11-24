/**
 * Problem: Valid Anagram
 * Difficulty: Easy
 * Pattern: Character Frequency Counting
 * 
 * Time Complexity Goal: O(n)
 * Space Complexity Goal: O(1)
 */

import fs = require('fs');

function isAnagram(s: string, t: string): boolean {
    // TODO: Implement using Map<string, number> for frequency
    // Hint: Early exit if lengths differ
    
    return false;
}

interface TestCase {
    id: number;
    description: string;
    input: { s: string; t: string };
    expected: boolean;
}

function runTests(): void {
    const data = JSON.parse(fs.readFileSync('test-data.json', 'utf8'));
    
    console.log("=".repeat(60));
    console.log("Running Valid Anagram Tests - TypeScript");
    console.log("=".repeat(60));
    
    let passed = 0, failed = 0;
    
    for (const test of data.testCases) {
        const { s, t } = test.input;
        const expected: boolean = test.expected;
        
        try {
            const result: boolean = isAnagram(s, t);
            
            if (result === expected) {
                console.log(`✅ Test ${test.id}: PASSED`);
                passed++;
            } else {
                console.log(`❌ Test ${test.id}: FAILED`);
                console.log(`   Input: s="${s}", t="${t}"`);
                console.log(`   Expected: ${expected}, Got: ${result}`);
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

console.log('Quick Test: s="anagram", t="nagaram" -> Expected: true');
console.log(`Your output: ${isAnagram('anagram', 'nagaram')}`);
console.log();

// runTests();

export { isAnagram, runTests };

