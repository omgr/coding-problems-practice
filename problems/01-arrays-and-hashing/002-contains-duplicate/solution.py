"""
Problem: Contains Duplicate
Difficulty: Easy
Pattern: Set for Uniqueness Check

Given an integer array nums, return true if any value appears at least twice,
and return false if every element is distinct.

Time Complexity Goal: O(n)
Space Complexity Goal: O(n)
"""

from typing import List
import json


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains any duplicates.
    
    Args:
        nums: List of integers
        
    Returns:
        True if duplicates exist, False otherwise
        
    TODO: Explain your approach:
        1. What data structure will you use?
        2. How will you detect duplicates?
        3. Can you do it in one pass?
    """
    
    # TODO: Implement your solution here
    # Hint: Use a set to track numbers you've seen
    # numTrack = set()
    # for num in nums:
    #     if num in numTrack:
    #         return True
    #     numTrack.add(num)
    # return False
    
    return len(nums) != len(set(nums))

    pass


def run_tests():
    """Run all test cases"""
    with open('test-data.json', 'r') as f:
        data = json.load(f)
    
    print("=" * 60)
    print("Running Contains Duplicate Tests - Python")
    print("=" * 60)
    
    passed = failed = 0
    
    for test in data['testCases']:
        nums = test['input']['nums']
        expected = test['expected']
        
        try:
            result = contains_duplicate(nums)
            
            if result == expected:
                print(f"✅ Test {test['id']}: PASSED")
                passed += 1
            else:
                print(f"❌ Test {test['id']}: FAILED - Expected {expected}, Got {result}")
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


if __name__ == "__main__":
    print("Quick Test: [1,2,3,1] -> Expected: True")
    try:
        print(f"Your output: {contains_duplicate([1, 2, 3, 1])}")
    except:
        print("Not implemented yet")
    print()
    
    run_tests()

