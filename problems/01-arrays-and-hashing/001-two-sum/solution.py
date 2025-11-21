"""
Problem: Two Sum
Difficulty: Easy
Topic: Arrays & Hash Tables
Pattern: HashMap Lookup

Problem Statement:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists

Time Complexity Goal: O(n)
Space Complexity Goal: O(n)
"""

from typing import List
import json


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in the array that add up to the target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers
        
    Approach:
        Explain your approach here before implementing
        Walkthrough of nums = [3, 2, 4], target = 6
        In this case:
        create empty hashmap.
        loop through i, nums array where I being the index.
        if target - nums[i] is not in Hashmap:
            add to hashmap[nums[i]] = i
            else return [i,hashmap[target - nums[i]];
            
        So we follow above pseudo code:
        first we start with 
        i = 0
        hashmap = {}
        num = 3
        compliment = 6-3 = 3
        hasmap is empty so we can't find 3 in it. so add to hashmap i.e., {[3]=0}

        next iteration
        i = 1
        hashmap = {[3]=0}
        num = 2
        compliment = 6-2 = 4
        hasmap is not empty but we can't find 4 in it. so add to hashmap i.e., {[3]=0,[2]=1}

        last iteration
        i = 2
        hashmap = {[3]=0,[2]=1}
        num = 4
        compliment = 6-4 = 2
        hasmap is not empty but we CAN find 2 in it. so return [hashmap[2],i] i.e., [1,2]
        1. What data structure will you use?
        HashMap/Dictionary


    """
    num_map = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in num_map:
            return [num_map[compliment], i]
        num_map[num] = i
    return []


    
    # TODO: Implement your solution here
    
    # Hint: You'll need a dictionary to store numbers you've seen
    # Key concept: For each number, check if (target - number) exists
    
    pass  # Remove this and implement your solution


def run_tests():
    """Run all test cases from test-data.json"""
    
    # Load test data
    with open('test-data.json', 'r') as f:
        data = json.load(f)
    
    print("=" * 60)
    print("Running Two Sum Tests - Python")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for test in data['testCases']:
        nums = test['input']['nums']
        target = test['input']['target']
        expected = test['expected']
        
        try:
            result = two_sum(nums, target)
            
            # Check if result matches expected (order doesn't matter)
            is_correct = (sorted(result) == sorted(expected))
            
            if is_correct:
                print(f"✅ Test {test['id']}: PASSED")
                print(f"   Input: nums={nums}, target={target}")
                print(f"   Output: {result}")
                passed += 1
            else:
                print(f"❌ Test {test['id']}: FAILED")
                print(f"   Input: nums={nums}, target={target}")
                print(f"   Expected: {expected}")
                print(f"   Got: {result}")
                failed += 1
                
        except Exception as e:
            print(f"❌ Test {test['id']}: ERROR")
            print(f"   Input: nums={nums}, target={target}")
            print(f"   Error: {str(e)}")
            failed += 1
        
        print()
    
    # Summary
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {passed + failed} tests")
    print("=" * 60)
    
    if passed == len(data['testCases']):
        print("🎉 Congratulations! All tests passed!")
        print("\nTime Complexity Analysis:")
        print("  - What is the time complexity of your solution?")
        print("  - Why is it better than brute force O(n²)?")
        print("\nSpace Complexity Analysis:")
        print("  - What is the space complexity of your solution?")
        print("  - What are you storing in memory?")
    else:
        print("Keep trying! Debug the failing tests.")


if __name__ == "__main__":
    # Quick manual test before running all tests
    print("Quick Test:")
    print("Input: [2, 7, 11, 15], target = 9")
    print("Expected: [0, 1]")
    try:
        result = two_sum([2, 7, 11, 15], 9)
        print(f"Your output: {result}")
    except:
        print("Your output: Not implemented yet")
    print()
    
    # Uncomment the line below when you're ready to run all tests
    run_tests()

