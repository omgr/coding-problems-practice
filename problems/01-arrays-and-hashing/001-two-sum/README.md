# 1. Two Sum

**Difficulty**: 🟢 Easy  
**Topic**: Arrays & Hash Tables  
**Pattern**: HashMap Lookup  
**LeetCode**: #1

---

## 📋 Problem Statement

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may **not** use the same element twice.

You can return the answer in any order.

---

## 💡 Examples

### Example 1:
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].
```

### Example 3:
```
Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 6, we return [0, 1].
```

---

## 🔒 Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists**

---

## 🎯 Key Concepts to Understand

Before you start coding, make sure you understand:

1. **What is a Hash Table/Dictionary/HashMap?**
   - How does it provide O(1) lookup time?
   - What are the key-value pairs in this problem?

2. **Why is this approach better than brute force?**
   - What is the time complexity of nested loops?
   - How does a hash table reduce time complexity?

3. **What should we store in the hash table?**
   - The number itself? Or its index?
   - Why?

4. **Edge cases to consider:**
   - What if the array has only 2 elements?
   - Can the same element be used twice? (No, according to the problem)
   - What if there are duplicate numbers?

---

## 💭 Approach

### Brute Force (Don't implement this, but understand why it's slow)
- Use two nested loops to check every pair
- Time Complexity: O(n²)
- Space Complexity: O(1)

### Optimized Solution (Implement this!)
- Use a hash table to store numbers we've seen
- For each number, check if `target - current_number` exists in hash table
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## 🧪 Test Cases Provided

The `test-data.json` file contains multiple test cases including:
- ✅ Small arrays (2-3 elements)
- ✅ Medium arrays (~100 elements)
- ✅ Large arrays (~10,000 elements)
- ✅ Negative numbers
- ✅ Duplicate numbers
- ✅ Edge cases

---

## 📝 Implementation Checklist

Before you start coding:
- [ ] Do you understand the problem?
- [ ] Can you explain the approach in your own words?
- [ ] Do you know what data structure to use?
- [ ] Have you identified the edge cases?

While coding:
- [ ] Add comments explaining your logic
- [ ] Handle edge cases
- [ ] Think about time and space complexity

After coding:
- [ ] Test with provided test cases
- [ ] Verify time complexity is O(n)
- [ ] Verify space complexity is O(n)
- [ ] Can you explain your code to someone else?

---

## 🎓 Learning Objectives

By completing this problem, you will:
- ✅ Master the HashMap lookup pattern
- ✅ Understand trade-offs between time and space complexity
- ✅ Practice handling edge cases
- ✅ Learn to optimize from O(n²) to O(n)

---

## 🚀 Ready to Code?

1. Open the solution file for your chosen language
2. Read through the boilerplate code
3. Implement the `twoSum` function
4. Run the tests
5. Move to the next language!

**Remember**: Focus on understanding over speed. Speed will come with practice!

---

Good luck! 🎉

