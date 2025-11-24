/**
 * Problem: Group Anagrams
 * Difficulty: Medium
 * Pattern: HashMap + String Processing
 * 
 * Time Complexity Goal: O(n × k) or O(n × k log k)
 * Space Complexity Goal: O(n × k)
 */

import fs = require('fs');

function groupAnagrams(strs: string[]): string[][] {
    // TODO: Implement using Map<string, string[]>
    // Hint: Use sorted string as key
    
    return [];
}

interface TestCase {
    id: number;
    description: string;
    input: { strs: string[] };
    expected: string[][];
}

function runTests(): void {
    const data = JSON.parse(fs.readFileSync('test-data.json', 'utf8'));
    
    console.log("=".repeat(60));
    console.log("Running Group Anagrams Tests - TypeScript");
    console.log("=".repeat(60));
    
    let passed = 0, failed = 0;
    
    for (const test of data.testCases) {
        const { strs } = test.input;
        const expected: string[][] = test.expected;
        
        try {
            const result: string[][] = groupAnagrams(strs);
            
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
            console.log(`❌ Test ${test.id}: ERROR - ${(error as Error).message}`);
            failed++;
        }
        console.log();
    }
    
    console.log("=".repeat(60));
    console.log(`Results: ${passed} passed, ${failed} failed`);
    console.log("=".repeat(60));
}

console.log('Quick Test: ["eat","tea","tan","ate","nat","bat"]');
const quickResult = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);
console.log(`Your output: ${quickResult.length} groups`);
quickResult.forEach(group => console.log(`  [${group.join(", ")}]`));
console.log();

runTests();

export { groupAnagrams, runTests };



