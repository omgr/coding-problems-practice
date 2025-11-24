# 004 - Group Anagrams

**Difficulty**: Medium  
**Category**: Arrays & Hashing  
**Pattern**: HashMap + String Processing  

---

## 📋 Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## 📥 Input / Output

### Input:
- `strs`: An array of strings (`1 <= strs.length <= 10^4`)
- Each string consists of lowercase English letters (`0 <= strs[i].length <= 100`)

### Output:
- A 2D array where each sub-array contains strings that are anagrams of each other
- The order of groups and order within groups doesn't matter

---

## 💡 Examples

### Example 1:
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
- "eat", "tea", "ate" are anagrams (same letters: e, a, t)
- "tan", "nat" are anagrams (same letters: t, a, n)
- "bat" has unique letters
```

### Example 2:
```
Input: strs = [""]
Output: [[""]]

Explanation: Single empty string forms one group
```

### Example 3:
```
Input: strs = ["a"]
Output: [["a"]]

Explanation: Single character forms one group
```

### Example 4:
```
Input: strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
Output: [["max"],["buy"],["doc"],["may"],["ill"],["duh"],["tin"],["bar"],["pew"],["cab"]]

Explanation: All strings have unique letter combinations (no anagrams)
```

---

## 🎯 Approach & Hints

### Key Questions to Ask:
1. **How do you identify if two strings are anagrams?**
   - You solved "Valid Anagram" - apply that knowledge!
   
2. **What's a unique "signature" for anagrams?**
   - Option 1: Sorted string - "eat" → "aet", "tea" → "aet"
   - Option 2: Character frequency tuple - (e:1, a:1, t:1)
   
3. **How do you group strings with the same signature?**
   - Use a HashMap: `{signature: [list of words]}`

### Approach 1: Sorting (Easier)
```
1. Create a HashMap to group words
2. For each word:
   - Sort its letters (e.g., "eat" → "aet")
   - Use sorted string as key
   - Add word to HashMap[key]
3. Return all values from HashMap
```

**Time Complexity**: O(n × k log k) where n = number of strings, k = max length  
**Space Complexity**: O(n × k)

### Approach 2: Character Frequency Counting (Optimal)
```
1. Create a HashMap with tuple keys
2. For each word:
   - Count character frequencies (array of 26 counts)
   - Convert to tuple (hashable in Python)
   - Use tuple as key
   - Add word to HashMap[tuple]
3. Return all values from HashMap
```

**Time Complexity**: O(n × k) where n = number of strings, k = max length  
**Space Complexity**: O(n × k)

---

## ⚠️ Edge Cases

- Empty string: `[""]` → `[[""]]`
- Single string: `["a"]` → `[["a"]]`
- No anagrams: All strings unique
- All same anagrams: `["a","a","a"]` → `[["a","a","a"]]`
- Mixed lengths: `["ab","ba","abc"]` → `[["ab","ba"],["abc"]]`

---

## 🔗 Related Problems

1. **Valid Anagram** (Problem 003) - You just solved this!
2. **Find All Anagrams in String** - Sliding window + anagram check
3. **Palindrome Pairs** - Similar grouping logic

---

## 🎓 What You'll Learn

- **HashMap with complex keys** (tuples, sorted strings)
- **Grouping pattern** (multiple values per key)
- **String manipulation** (sorting, counting)
- **Data structure selection** (when to use what)

---

## ⏱️ **TIMED CHALLENGE MODE**

**Time Limit**: 25 minutes  
**Language**: Python  
**Goal**: Get it working, then optimize if time permits

**Don't peek at hints unless stuck for 5+ minutes!**

Good luck! 🚀

