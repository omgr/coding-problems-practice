/**
 * Problem: Valid Anagram
 * Difficulty: Easy
 * Pattern: Character Frequency Counting
 * 
 * Time Complexity Goal: O(n)
 * Space Complexity Goal: O(1)
 */

const fs = require('fs');

/**
 * Check if t is an anagram of s
 * @param {string} s - First string
 * @param {string} t - Second string
 * @returns {boolean} - True if t is anagram of s
 */
function isAnagram(s, t) {
    // TODO: Implement using Map or object for frequency counting
    // Hint: You can also use sorting approach
    
    return false;
}

function runTests() {
    const data = JSON.parse(fs.readFileSync('test-data.json', 'utf8'));
    
    console.log("=".repeat(60));
    console.log("Running Valid Anagram Tests - JavaScript");
    console.log("=".repeat(60));
    
    let passed = 0, failed = 0;
    
    for (const test of data.testCases) {
        const { s, t } = test.input;
        const expected = test.expected;
        
        try {
            const result = isAnagram(s, t);
            
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

console.log('Quick Test: s="anagram", t="nagaram" -> Expected: true');
console.log(`Your output: ${isAnagram('anagram', 'nagaram')}`);
console.log();

// runTests();

module.exports = { isAnagram, runTests };

