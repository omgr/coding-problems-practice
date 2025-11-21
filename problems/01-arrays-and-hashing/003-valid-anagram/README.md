# 3. Valid Anagram

**Difficulty**: 🟢 Easy  
**Topic**: Arrays & Hash Tables  
**Pattern**: Character Frequency Counting  
**LeetCode**: #242

---

## 📋 Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## 💡 Examples

### Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
Explanation: Both strings have the same characters with the same frequencies.
```

### Example 2:
```
Input: s = "rat", t = "car"
Output: false
Explanation: Different characters.
```

### Example 3:
```
Input: s = "listen", t = "silent"
Output: true
Explanation: Classic anagram pair.
```

---

## 🔒 Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters

---

## 🎯 Key Concepts to Understand

1. **What is character frequency counting?**
   - How to count occurrences of each character?
   - What data structure is best for this?

2. **Different approaches:**
   - Sorting vs HashMap/Dictionary
   - Which is more efficient?

3. **Edge cases:**
   - Different lengths?
   - Empty strings?
   - Single character?
   - Same string?

---

## 💭 Approach

### Option 1: Sorting
- Sort both strings and compare
- Time: O(n log n), Space: O(1) or O(n) depending on sort

### Option 2: Frequency Counter (Best approach - Implement this!)
- Count character frequencies in both strings
- Compare the frequency maps
- Time: O(n), Space: O(1) - only 26 lowercase letters

### Option 3: Alternative Frequency Counter
- Build frequency map for first string
- Decrement for second string
- Check if all counts are zero
- Time: O(n), Space: O(1)

---

## 🧪 Test Cases

- Basic anagrams
- Non-anagrams
- Different lengths
- Single character
- Empty strings
- Same string
- Case sensitivity (all lowercase in this problem)

---

## 🎓 Learning Objectives

- Master frequency counting pattern
- Understand HashMap/Dictionary usage
- Compare multiple solution approaches
- Optimize for specific constraints (only 26 letters)

---

Good luck! 🎉

