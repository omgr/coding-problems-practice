# 📚 Arrays and Hashing - Concept Guide

## Overview

Arrays and Hash Tables are the most fundamental data structures in programming. Mastering them is essential for technical interviews as they form the foundation for more complex algorithms.

---

## 🎯 Core Concepts

### 1. Arrays

**What is an Array?**
- Contiguous block of memory storing elements of the same type
- Elements accessed by index (0-based in most languages)
- Fixed or dynamic size depending on the language

**Time Complexities:**
- Access by index: O(1)
- Search (unsorted): O(n)
- Search (sorted): O(log n) with binary search
- Insert at end: O(1) amortized
- Insert at beginning: O(n)
- Delete: O(n)

**When to Use:**
- Need random access to elements
- Know the size beforehand or size doesn't change often
- Need cache-friendly sequential access

---

### 2. Hash Tables (HashMap, Dictionary, Object, Map)

**What is a Hash Table?**
- Data structure that maps keys to values
- Uses a hash function to compute an index
- Provides near O(1) lookup, insert, and delete operations

**Language-Specific Names:**
- Python: `dict` or `defaultdict`
- JavaScript: `Object` or `Map`
- TypeScript: `Map<K, V>` or `Record<K, V>`
- C#: `Dictionary<TKey, TValue>` or `Hashtable`
- Go: `map[KeyType]ValueType`

**Time Complexities (Average):**
- Insert: O(1)
- Delete: O(1)
- Search/Lookup: O(1)
- Worst case (hash collisions): O(n)

**When to Use:**
- Need fast lookups by key
- Counting frequencies
- Checking for existence
- Caching/memoization

---

### 3. Sets (HashSet)

**What is a Set?**
- Collection of unique elements
- Implemented using hash tables
- No duplicates allowed

**Language-Specific:**
- Python: `set()`
- JavaScript/TypeScript: `Set`
- C#: `HashSet<T>`
- Go: `map[T]bool` (simulate set with map)

**Time Complexities:**
- Add: O(1)
- Remove: O(1)
- Contains: O(1)

**When to Use:**
- Need to check for duplicates
- Need uniqueness guarantee
- Set operations (union, intersection, difference)

---

## 🔑 Common Patterns

### Pattern 1: HashMap Lookup
**Use Case:** Find complementary elements (like Two Sum)

```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

**Key Insight:** Trade space for time - use O(n) space to achieve O(n) time instead of O(n²)

---

### Pattern 2: Frequency Counting
**Use Case:** Count occurrences of elements

```python
def count_frequencies(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Or use Counter in Python
from collections import Counter
freq = Counter(arr)
```

**Applications:**
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements

---

### Pattern 3: Set for Uniqueness
**Use Case:** Detect duplicates

```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Or more concise:
def has_duplicate(nums):
    return len(nums) != len(set(nums))
```

---

## 💡 Problem-Solving Strategy

### Step 1: Identify the Pattern
Ask yourself:
- Do I need to find two elements that satisfy a condition? → HashMap Lookup
- Do I need to count something? → Frequency Counter
- Do I need to check for duplicates? → Set
- Is the array sorted? → Consider two pointers instead

### Step 2: Choose the Right Data Structure

| Need | Data Structure | Why |
|------|----------------|-----|
| Fast lookup by key | HashMap | O(1) access |
| Uniqueness | Set | Automatic deduplication |
| Counting | HashMap | key=item, value=count |
| Order matters | Array + HashMap | Combine both |
| Sorted access | Array (sorted) | Or use sorted keys |

### Step 3: Consider Trade-offs

**Time vs Space:**
- Using HashMap: More space (O(n)) but faster time (O(1) lookup)
- No extra space: Less space but slower time (O(n) search)

**When to Use Each:**
- Small datasets → Space is less critical, readability matters
- Large datasets → Time complexity becomes critical
- Constraints → "O(1) space" means you can't use HashMap

---

## 🎓 Interview Tips

### 1. Always Ask About Constraints
- Input size?
- Can we modify the input?
- Memory constraints?
- Are elements unique?

### 2. Start with Brute Force
- Explain the O(n²) solution first
- Then optimize using HashMap

### 3. Explain Your Thought Process
- "I'll use a HashMap to track numbers I've seen"
- "This gives us O(1) lookup instead of O(n) for each element"
- "The space trade-off is worth it for the time improvement"

### 4. Handle Edge Cases
- Empty array
- Single element
- All duplicates
- No duplicates
- Negative numbers
- Very large numbers

---

## 📊 Complexity Analysis

### Space Complexity Guidelines

**O(1)** - Constant Space:
- Only using a few variables
- No data structures that grow with input

**O(n)** - Linear Space:
- HashMap/Set that stores all elements
- Frequency counter
- Auxiliary array of same size

**O(k)** - Limited Space:
- Only 26 letters (alphabet)
- Fixed range of numbers

---

## 🚀 Practice Problems

### Easy
- ✅ Two Sum
- ✅ Contains Duplicate
- ✅ Valid Anagram
- Valid Palindrome
- Best Time to Buy and Sell Stock

### Medium
- Group Anagrams
- Top K Frequent Elements
- Product of Array Except Self
- Encode and Decode Strings
- Longest Consecutive Sequence

### Hard
- Minimum Window Substring
- Largest Rectangle in Histogram

---

## 🔗 Related Concepts

- **Two Pointers**: Often can replace HashMap when array is sorted
- **Sliding Window**: Combines array traversal with HashMap for subarray problems
- **Binary Search**: Used on sorted arrays for O(log n) search

---

## 📝 Language-Specific Tips

### Python
```python
# Dictionary methods
d.get(key, default)  # Safe access with default
d[key] = d.get(key, 0) + 1  # Increment counter

# Counter for frequency
from collections import Counter
freq = Counter(arr)

# Set operations
set1 & set2  # Intersection
set1 | set2  # Union
set1 - set2  # Difference
```

### JavaScript/TypeScript
```javascript
// Map vs Object
const map = new Map();  // Better for non-string keys
map.set(key, value);
map.get(key);
map.has(key);

// Set
const set = new Set([1, 2, 3]);
set.add(4);
set.has(2);  // true
```

### C#
```csharp
// Dictionary
var dict = new Dictionary<int, int>();
if (dict.ContainsKey(key)) { }
dict.TryGetValue(key, out value);

// HashSet
var set = new HashSet<int>();
set.Add(1);
set.Contains(1);  // true
```

### Go
```go
// Map
m := make(map[int]int)
value, exists := m[key]

// Simulate Set
set := make(map[int]bool)
set[1] = true
if set[1] { } // Check existence
```

---

## ✅ Mastery Checklist

After completing the Arrays & Hashing problems, you should be able to:

- [ ] Explain when to use HashMap vs Array vs Set
- [ ] Implement frequency counter pattern
- [ ] Use HashMap for O(n) solutions instead of O(n²)
- [ ] Analyze time and space complexity
- [ ] Handle edge cases confidently
- [ ] Code in all 5 languages with correct syntax
- [ ] Explain trade-offs between different approaches

---

**Remember**: Arrays and Hashing are the foundation. Master these patterns, and you'll recognize them in many other problems!

