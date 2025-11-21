# 🚀 Coding Problems Practice

<div align="center">

**A comprehensive, multi-language approach to mastering Data Structures & Algorithms**

![Languages](https://img.shields.io/badge/Languages-5-blue)
![Problems](https://img.shields.io/badge/Problems-42-green)
![Progress](https://img.shields.io/badge/Progress-0%25-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📚 Quick Start

**New here?** Start with these guides:
- 📖 [START HERE](docs/START-HERE.md) - Your first 5 minutes
- 📖 [Getting Started](docs/GETTING-STARTED.md) - Day 1 step-by-step guide
- 📋 [Learning Plan](docs/learning-plan.md) - Complete 14-day curriculum
- 🛠️ [How to Run](docs/HOW-TO-RUN.md) - Execute code in all 5 languages
- 📈 [Progress Tracker](docs/progress-tracker.md) - Track your journey

---

## 👨‍💻 About This Repository

This repository documents my intensive 14-day journey to master coding interview patterns and algorithms across **five programming languages**: Python, C#, JavaScript, TypeScript, and Go. 

As an **Engineering Manager transitioning back to hands-on development**, I'm building deep expertise in data structures, algorithms, and problem-solving patterns that are essential for technical interviews at top companies.

---

## 🎯 Goals & Approach

### Primary Objectives
- ✅ Master fundamental data structures and algorithms
- ✅ Build fluency across 5 programming languages
- ✅ Develop pattern recognition for common interview problems
- ✅ Improve live coding speed and confidence
- ✅ Create a portfolio demonstrating technical breadth

### Unique Methodology
- **Multi-Language Learning**: Every problem solved in 5 languages to understand paradigm differences
- **Pattern-First Approach**: Focus on recognizing and applying algorithmic patterns
- **Test-Driven Practice**: Comprehensive test suites from small to large datasets
- **Structured Progression**: Following Grind 75 - an optimized problem set for interview prep
- **Self-Assessment**: Timed challenges every 3 problems to measure progress

---

## 📊 Skills & Progress

### Language Proficiency
| Language   | Problems Solved | Proficiency Level | Primary Use Case |
|------------|-----------------|-------------------|------------------|
| Python 🐍  | 0 / 42 | ██████░░░░ 60% | Rapid prototyping, Data processing |
| C# 💎      | 0 / 42 | ██████░░░░ 60% | Backend services, Enterprise apps |
| JavaScript 📜 | 0 / 42 | █████░░░░░ 50% | Frontend, Full-stack |
| TypeScript 📘 | 0 / 42 | █████░░░░░ 50% | Type-safe frontend, Node.js |
| Go 🔵      | 0 / 42 | ███░░░░░░░ 30% | Systems programming, Microservices |

### Data Structures Mastered
<details>
<summary>Click to expand</summary>

- [x] Arrays & Dynamic Arrays
- [x] Hash Tables / Dictionaries
- [x] Sets / HashSets
- [ ] Linked Lists
- [ ] Stacks & Queues
- [ ] Binary Trees & BST
- [ ] Graphs
- [ ] Heaps / Priority Queues
- [ ] Tries

</details>

### Algorithms Mastered
<details>
<summary>Click to expand</summary>

- [x] HashMap Lookup Pattern
- [x] Frequency Counting
- [ ] Two Pointers
- [ ] Sliding Window
- [ ] Binary Search
- [ ] Depth-First Search (DFS)
- [ ] Breadth-First Search (BFS)
- [ ] Dynamic Programming
- [ ] Backtracking
- [ ] Greedy Algorithms
- [ ] Topological Sort

</details>

---

## 🗂️ Repository Structure

```
coding-problems-practice/
├── 📖 README.md                  # This file - Portfolio overview
├── 📚 docs/                      # All documentation
│   ├── START-HERE.md            # Begin your journey here!
│   ├── GETTING-STARTED.md       # Day 1 step-by-step guide
│   ├── learning-plan.md         # 14-day structured curriculum
│   ├── progress-tracker.md      # Detailed daily progress tracking
│   ├── HOW-TO-RUN.md           # Running code in all languages
│   └── PROJECT-SUMMARY.md       # What was built
├── 🧠 concepts/                  # Deep-dive guides for each pattern
│   ├── 01-arrays-and-hashing.md
│   ├── 02-two-pointers.md       # (Created as you progress)
│   └── ...
├── 💻 problems/                  # All coding problems organized by topic
│   ├── 01-arrays-and-hashing/
│   │   ├── 001-two-sum/
│   │   │   ├── README.md         # Problem statement & approach
│   │   │   ├── test-data.json    # Comprehensive test cases
│   │   │   ├── solution.py       # Python boilerplate
│   │   │   ├── solution.js       # JavaScript boilerplate
│   │   │   ├── solution.ts       # TypeScript boilerplate
│   │   │   ├── solution.cs       # C# boilerplate
│   │   │   └── solution.go       # Go boilerplate
│   │   └── ...
│   └── ...
├── 🏆 challenges/                # Your timed coding challenges (Day 4, 8, 12)
├── 💾 solutions/                 # Your completed, working solutions
└── 🛠️ utils/                     # Test runners and helper utilities
```

---

## 🌟 Featured Problem Solutions

### Problem 1: Two Sum
**Difficulty**: Easy | **Pattern**: HashMap Lookup | **Topic**: Arrays & Hashing

**Problem**: Given an array of integers and a target, find two numbers that add up to the target.

<details>
<summary>Python Solution</summary>

```python
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Optimal O(n) solution using HashMap lookup pattern.
    Trade space for time: O(n) space for O(1) lookups.
    """
    seen = {}  # num -> index mapping
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

# Time: O(n) - Single pass through array
# Space: O(n) - HashMap stores up to n elements
```

</details>

<details>
<summary>C# Solution</summary>

```csharp
public static int[] TwoSum(int[] nums, int target)
{
    // Dictionary provides O(1) lookup
    var seen = new Dictionary<int, int>();
    
    for (int i = 0; i < nums.Length; i++)
    {
        int complement = target - nums[i];
        
        if (seen.ContainsKey(complement))
        {
            return new int[] { seen[complement], i };
        }
        
        seen[nums[i]] = i;
    }
    
    return new int[] { };
}
```

</details>

**Key Insights**:
- HashMap reduces time complexity from O(n²) to O(n)
- Trade-off: Use O(n) extra space for significant time improvement
- Single-pass algorithm - we find the solution as we build the map

---

### Problem 2: Contains Duplicate
**Difficulty**: Easy | **Pattern**: Set for Uniqueness | **Topic**: Arrays & Hashing

**Problem**: Determine if an array contains any duplicates.

<details>
<summary>Python Solution (Elegant)</summary>

```python
def contains_duplicate(nums: List[int]) -> bool:
    """
    Leverage Set's automatic uniqueness property.
    If Set size < Array size, duplicates exist.
    """
    return len(nums) != len(set(nums))

# Time: O(n) - Set creation
# Space: O(n) - Set stores unique elements
```

</details>

<details>
<summary>TypeScript Solution (Efficient)</summary>

```typescript
function containsDuplicate(nums: number[]): boolean {
    const seen = new Set<number>();
    
    for (const num of nums) {
        if (seen.has(num)) {
            return true;  // Early exit on first duplicate
        }
        seen.add(num);
    }
    
    return false;
}

// Time: O(n) worst case, O(1) best case (early exit)
// Space: O(n) - Set grows with unique elements
```

</details>

**Key Insights**:
- Set provides O(1) membership testing
- Early exit optimization can improve average case performance
- Multiple valid approaches: Set comparison vs iterative checking

---

### Problem 3: Valid Anagram
**Difficulty**: Easy | **Pattern**: Frequency Counting | **Topic**: Arrays & Hashing

**Problem**: Check if two strings are anagrams of each other.

<details>
<summary>Go Solution</summary>

```go
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false  // Early exit for different lengths
    }
    
    freq := make(map[rune]int)
    
    // Count frequencies in first string
    for _, char := range s {
        freq[char]++
    }
    
    // Decrement for second string
    for _, char := range t {
        freq[char]--
        if freq[char] < 0 {
            return false  // More occurrences in t than s
        }
    }
    
    return true
}

// Time: O(n) - Two passes through strings
// Space: O(1) - Only 26 lowercase letters (constant space)
```

</details>

**Key Insights**:
- Frequency counting is optimal for character comparison
- Space complexity is O(1) when character set is limited (26 letters)
- Alternative: Sorting both strings (O(n log n) time, O(1) space if in-place)

---

## 📈 Progress Timeline

### Week 1: Foundations (In Progress)
- [x] **Day 1**: Arrays & Hash Tables - Two Sum, Contains Duplicate, Valid Anagram
- [ ] **Day 2**: Strings & Stacks - Valid Parentheses, Reverse String, First Unique Character
- [ ] **Day 3**: Linked Lists - Reverse, Merge Two Lists, Cycle Detection
- [ ] **Day 4**: 🏆 Timed Challenge #1
- [ ] **Day 5**: Binary Search - Binary Search, First Bad Version, Search Insert
- [ ] **Day 6**: Two Pointers - Two Sum II, 3Sum, Container With Most Water
- [ ] **Day 7**: Sliding Window - Best Time to Buy Stock, Longest Substring
- [ ] **Day 8**: 🏆 Timed Challenge #2

### Week 2: Advanced Patterns
- [ ] **Day 9**: Binary Trees - Traversal, Inversion, Max Depth
- [ ] **Day 10**: Binary Trees Advanced - LCA, Level Order, Validate BST
- [ ] **Day 11**: Graphs - Number of Islands, Clone Graph, Course Schedule
- [ ] **Day 12**: 🏆 Timed Challenge #3
- [ ] **Day 13**: Dynamic Programming - Climbing Stairs, House Robber, Coin Change
- [ ] **Day 14**: DP Advanced & Review - LCS, Word Break, Mixed Review

---

## 💼 Professional Context

### Background
- **Current Role**: Engineering Manager at [Company]
- **Goal**: Transition to hands-on Senior/Staff Engineer roles
- **Focus Areas**: Full-stack development (React, TypeScript, .NET, Azure)
- **Learning New**: Python and Go for broader language proficiency

### Why This Approach?
1. **Multi-language fluency** demonstrates adaptability and deep understanding
2. **Systematic practice** builds confidence for live coding interviews
3. **Pattern recognition** enables solving new problems efficiently
4. **Documentation** shows communication skills and teaching ability

---

## 🎓 Learning Philosophy

> "The goal isn't just to solve problems—it's to understand the patterns so deeply that recognizing them becomes second nature."

### Core Principles
1. **Understand Before Memorizing**: Explain concepts before coding
2. **Pattern Recognition Over Rote Learning**: Focus on why, not just what
3. **Incremental Progress**: Small consistent steps over sporadic bursts
4. **Multi-Language Thinking**: Understand paradigm differences
5. **Test Everything**: Comprehensive testing builds confidence

---

## 🛠️ How to Use This Repository

### For Learners
1. Start with the `learning-plan.md` for structured progression
2. Read concept guides in `concepts/` before solving problems
3. Try to solve each problem before looking at solutions
4. Run provided test cases to verify your solution
5. Compare your approach with solutions in different languages

### For Recruiters
- Browse `problems/` to see coding samples across 5 languages
- Check `progress-tracker.md` for learning journey and consistency
- Review concept guides to assess teaching/communication ability
- See `challenges/` for timed problem-solving demonstrations

---

## 📞 Connect With Me

- **GitHub**: [Your GitHub Profile]
- **LinkedIn**: [Your LinkedIn]
- **Email**: [Your Email]
- **Portfolio**: [Your Portfolio Site]

---

## 📜 License & Attribution

This repository is for educational and portfolio purposes. Problems are inspired by LeetCode and follow the Grind 75 curriculum created by the coding community.

---

## 🙏 Acknowledgments

- **Grind 75**: For the curated problem set
- **LeetCode**: For problem inspirations
- **Coding Community**: For shared knowledge and support

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

*Last Updated: November 21, 2025*

</div>

