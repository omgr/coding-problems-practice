/**
 * Problem: Group Anagrams
 * Difficulty: Medium
 * Pattern: HashMap + String Processing
 * 
 * Time Complexity Goal: O(n × k) or O(n × k log k)
 * Space Complexity Goal: O(n × k)
 */

const fs = require('fs');

/**
 * Group anagrams together from the input array
 * @param {string[]} strs - Array of strings
 * @returns {string[][]} - Grouped anagrams
 */
function groupAnagrams(strs) {
    // TODO: Implement using Map or object
    // Hint 1: Use sorted string as key: str.split('').sort().join('')
    // Hint 2: Map will store {signature: [words]}
    
    return [];
}

function runTests() {
    const data = JSON.parse(fs.readFileSync('test-data.json', 'utf8'));
    
    console.log("=".repeat(60));
    console.log("Running Group Anagrams Tests - JavaScript");
    console.log("=".repeat(60));
    
    let passed = 0, failed = 0;
    
    for (const test of data.testCases) {
        const { strs } = test.input;
        const expected = test.expected;
        
        try {
            const result = groupAnagrams(strs);
            
            // Sort for comparison (order doesn't matter)
            const resultSorted = result.map(g => g.sort().join(',')).sort();
            const expectedSorted = expected.map(g => g.sort().join(',')).sort();
            
            if (JSON.stringify(resultSorted) === JSON.stringify(expectedSorted)) {
                console.log(`✅ Test ${test.id}: PASSED`);
                passed++;
            } else {
                console.log(`❌ Test ${test.id}: FAILED`);
                console.log(`   Input: ${JSON.stringify(strs)}`);
                console.log(`   Expected groups: ${expected.length}`);
                console.log(`   Got groups: ${result.length}`);
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

console.log('Quick Test: ["eat","tea","tan","ate","nat","bat"]');
const quickResult = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);
console.log(`Your output: ${quickResult.length} groups`);
quickResult.forEach(group => console.log(`  [${group.join(", ")}]`));
console.log();

runTests();

module.exports = { groupAnagrams, runTests };



