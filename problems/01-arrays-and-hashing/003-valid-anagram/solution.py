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
    
    # TODO: Implement your solution here
    # Hint: Use dictionary/Counter to count character frequencies
    # Alternative: Use sorting (but slower)
    
    pass


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
    
    # run_tests()

