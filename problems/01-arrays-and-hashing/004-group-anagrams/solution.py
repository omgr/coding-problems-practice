"""
Problem: Group Anagrams
Difficulty: Medium
Pattern: HashMap + String Processing

Given an array of strings strs, group the anagrams together.
Return the groups in any order.

Time Complexity Goal: O(n × k) or O(n × k log k)
Space Complexity Goal: O(n × k)

where n = number of strings, k = max length of string
"""

import json
from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together from the input array.
    
    Args:
        strs: List of strings to group
        
    Returns:
        List of lists where each inner list contains anagram groups
        
    TODO: Plan your approach:
        1. How will you identify anagrams? (sorted string? frequency count?)
        2. What data structure will store the groups?
        3. How will you handle edge cases (empty strings, single chars)?
    
    HINTS (Don't look unless stuck!):
    - You solved "Valid Anagram" - how did you check if two strings were anagrams?
    - Use a HashMap where key = anagram signature, value = list of words
    - In Python, you can use tuple(sorted(str)) or tuple(count_array) as key
    """
    
    # TODO: Implement your solution here
    # Approach 1: Use sorted string as key
    # Approach 2: Use character frequency tuple as key
    
    pass


def run_tests():
    """Run all test cases"""
    with open('test-data.json', 'r') as f:
        data = json.load(f)
    
    print("=" * 60)
    print("Running Group Anagrams Tests - Python")
    print("=" * 60)
    
    passed = failed = 0
    
    for test in data['testCases']:
        strs = test['input']['strs']
        expected = test['expected']
        
        try:
            result = group_anagrams(strs)
            
            # Compare regardless of order (sort for comparison)
            result_sorted = sorted([sorted(group) for group in result])
            expected_sorted = sorted([sorted(group) for group in expected])
            
            if result_sorted == expected_sorted:
                print(f"✅ Test {test['id']}: PASSED")
                passed += 1
            else:
                print(f"❌ Test {test['id']}: FAILED")
                print(f"   Input: {strs}")
                print(f"   Expected (sorted): {expected_sorted}")
                print(f"   Got (sorted): {result_sorted}")
                failed += 1
        except Exception as e:
            print(f"❌ Test {test['id']}: ERROR - {str(e)}")
            print(f"   Input: {strs}")
            failed += 1
        
        print()
    
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if passed == len(data['testCases']):
        print("🎉 All tests passed!")
        print("\nBonus Challenges:")
        print("1. Did you use the optimal O(n × k) approach?")
        print("2. Can you implement both sorting and counting approaches?")
        print("3. What are the tradeoffs between the two?")


if __name__ == "__main__":
    print("⏱️  TIMED CHALLENGE: 25 MINUTES")
    print("=" * 60)
    print("Quick Test: strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']")
    print("Expected: Groups of anagrams")
    print()
    
    try:
        result = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        print(f"Your output: {result}")
    except:
        print("Not implemented yet")
    
    print()
    print("⏱️  Start your timer NOW!")
    print("=" * 60)
    print()
    
    run_tests()



