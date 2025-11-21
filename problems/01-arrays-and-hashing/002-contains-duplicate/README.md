# 2. Contains Duplicate

**Difficulty**: 🟢 Easy  
**Topic**: Arrays & Hash Tables  
**Pattern**: Set for Uniqueness Check  
**LeetCode**: #217

---

## 📋 Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

---

## 💡 Examples

### Example 1:
```
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 appears at indices 0 and 3.
```

### Example 2:
```
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.
```

### Example 3:
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Explanation: Multiple elements appear more than once.
```

---

## 🔒 Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 🎯 Key Concepts to Understand

1. **What is a Set/HashSet?**
   - How does it handle duplicates?
   - What is the time complexity for add/contains operations?

2. **Why use a Set instead of sorting?**
   - Compare time complexities: O(n) vs O(n log n)
   - When would sorting be better?

3. **Edge cases:**
   - Single element array?
   - All elements are the same?
   - Array is already sorted?

---

## 💭 Approach

### Option 1: Brute Force (Don't implement)
- Compare every element with every other element
- Time: O(n²), Space: O(1)

### Option 2: Sorting (Alternative approach)
- Sort the array and check adjacent elements
- Time: O(n log n), Space: O(1) or O(n) depending on sort

### Option 3: Hash Set (Best approach - Implement this!)
- Use a set to track seen numbers
- Time: O(n), Space: O(n)

---

## 🧪 Test Cases

- Small arrays
- Large arrays (100,000 elements)
- All duplicates
- No duplicates
- Negative numbers
- Mix of positive and negative

---

## 🎓 Learning Objectives

- Understand Set data structure
- Practice space-time tradeoff
- Learn when to use Hash Set vs sorting

---

Good luck! 🎉

