"""
Problem: Valid Anagram
Difficulty: Easy
Pattern: Character Frequency Counting

Given two strings s and t, return true if t is an anagram of s.

Time Complexity Goal: O(n)
Space Complexity Goal: O(1) - only 26 lowercase letters
"""

import json


def is_anagram(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is an anagram of s
        
    TODO: Explain your approach:
        1. How will you count character frequencies?
        2. Can you optimize knowing there are only 26 letters?
        3. What's an early exit condition?
    """
    
    """
    Approach: Character Frequency Counter (One Dictionary)
    
    Algorithm:
    1. Early exit: if lengths differ, not an anagram
    2. Build frequency map for string s
    3. For each char in t, decrement its count
       - If char not in map or count is 0, return False
    4. If we complete the loop, all counts match
    
    Time Complexity: O(n) - two passes through strings
    Space Complexity: O(1) - max 26 lowercase letters (constant)
    """
    
    # Step 1: Early exit - different lengths can't be anagrams
    if len(s) != len(t):
        return False
    
    # Step 2: Build frequency map for string s
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Step 3: Decrement counts using string t
    for char in t:
        # If char not in s, or we've used all occurrences, not an anagram
        if char_counts.get(char, 0) == 0:
            return False
        char_counts[char] -= 1
    
    # Step 4: All counts matched!
    return True
    
    # Alternative Approach (commented for reference):
    # Build two frequency maps and compare them
    # char_count_s = {}
    # char_count_t = {}
    # for char_s, char_t in zip(s, t):
    #     char_count_s[char_s] = char_count_s.get(char_s, 0) + 1
    #     char_count_t[char_t] = char_count_t.get(char_t, 0) + 1
    # return char_count_s == char_count_t


def run_tests():
    """Run all test cases"""
    with open('test-data.json', 'r') as f:
        data = json.load(f)
    
    print("=" * 60)
    print("Running Valid Anagram Tests - Python")
    print("=" * 60)
    
    passed = failed = 0
    
    for test in data['testCases']:
        s = test['input']['s']
        t = test['input']['t']
        expected = test['expected']
        
        try:
            result = is_anagram(s, t)
            
            if result == expected:
                print(f"✅ Test {test['id']}: PASSED")
                passed += 1
            else:
                print(f"❌ Test {test['id']}: FAILED")
                print(f"   Input: s=\"{s}\", t=\"{t}\"")
                print(f"   Expected: {expected}, Got: {result}")
                failed += 1
        except Exception as e:
            print(f"❌ Test {test['id']}: ERROR - {str(e)}")
            failed += 1
        
        print()
    
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if passed == len(data['testCases']):
        print("🎉 All tests passed!")
        print("\nBonus: Can you implement it using sorting?")
        print("What would be the time complexity difference?")


if __name__ == "__main__":
    print("Quick Test: s=\"anagram\", t=\"nagaram\" -> Expected: True")
    try:
        print(f"Your output: {is_anagram('anagram', 'nagaram')}")
    except:
        print("Not implemented yet")
    print()
    
    run_tests()

