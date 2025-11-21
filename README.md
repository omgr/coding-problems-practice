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

My practice grounds for exploring data structures and algorithms across **five programming languages**: Python, C#, JavaScript, TypeScript, and Go. This is where I feed my curiosity about optimized code and deepen my understanding of fundamental CS concepts.

As a **Full-Stack Engineering Manager** who codes daily, I maintain sharp algorithmic thinking skills through deliberate practice. This repository serves both as my learning laboratory and as a reference library for implementing efficient algorithms in real-world projects.

---

## 🎯 Purpose & Approach

### Why This Repository Exists
- 🎓 **Continuous Learning**: Sharpening algorithmic thinking through deliberate practice
- 🔧 **Practical Reference**: Quick access to optimized implementations for real work
- 🌐 **Language Mastery**: Understanding how same concepts manifest across paradigms
- 📊 **Performance Analysis**: Exploring time/space complexity trade-offs
- 🧩 **Pattern Recognition**: Building intuition for efficient problem-solving

### Methodology
- **Multi-Language Implementation**: Every algorithm in 5 languages to understand paradigm differences and language-specific optimizations
- **Test-Driven Development**: Comprehensive test suites validate correctness and edge cases
- **Complexity Analysis**: Document time and space trade-offs for informed decisions
- **Pattern-Based Organization**: Group by algorithmic patterns (HashMap lookup, Two Pointers, DP, etc.)
- **Production-Quality Code**: Clean, well-documented implementations ready for real use

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

## 📈 Coverage & Progress

### Foundational Patterns
- **Arrays & Hashing**: HashMap lookup, frequency counting, set operations
- **Two Pointers**: Converging pointers, sliding window, partition algorithms
- **Strings**: Manipulation, pattern matching, character analysis
- **Stacks & Queues**: LIFO/FIFO operations, monotonic stacks
- **Binary Search**: Divide and conquer, boundary problems

### Data Structure Implementations
- **Linked Lists**: Traversal, reversal, cycle detection, merge operations
- **Trees**: DFS, BFS, traversal patterns, BST operations
- **Graphs**: Grid problems, connectivity, topological sort
- **Heaps**: Priority queues, k-way merge, top-k problems

### Advanced Algorithms
- **Dynamic Programming**: Memoization, tabulation, state machines
- **Backtracking**: Constraint satisfaction, combinatorial problems
- **Greedy**: Optimization problems, interval scheduling
- **Bit Manipulation**: Efficient operations, mathematical tricks

---

## 💼 Technical Background

### Current Expertise
- **Role**: Engineering Manager - Full-Stack Development
- **Daily Stack**: React, TypeScript, .NET, Azure
- **Core Strengths**: System architecture, performance optimization, algorithmic problem-solving
- **Expanding Knowledge**: Python and Go for cloud-native and data engineering use cases

### Why Multiple Languages?
1. **Real-World Flexibility**: Different projects demand different tools
2. **Deeper Understanding**: Implementing same algorithm across paradigms reveals insights
3. **Optimal Solutions**: Each language has strengths - know when to use which
4. **Team Collaboration**: Work effectively across polyglot codebases

---

## 🎓 Philosophy

> "Understanding algorithmic patterns deeply enables solving novel problems efficiently in production code."

### Core Principles
1. **Deep Understanding**: Know the 'why' behind each algorithm, not just the 'how'
2. **Pattern Recognition**: Build intuition for which patterns solve which problems
3. **Practical Application**: Every algorithm here has real-world use cases
4. **Language-Agnostic Thinking**: Separate algorithmic concepts from implementation details
5. **Rigorous Testing**: Production-quality code requires comprehensive test coverage

---

## 🛠️ How to Use This Repository

### For Learning & Reference
1. **Browse by Pattern**: Navigate `concepts/` to understand algorithmic patterns
2. **See Implementations**: Each problem solved in 5 languages with test suites
3. **Compare Approaches**: Study how same algorithm differs across languages
4. **Use in Projects**: Copy and adapt implementations for your own work
5. **Learn from Tests**: Comprehensive test cases show edge case handling

### For Collaboration & Code Review
- **Language-Specific Examples**: Find idiomatic implementations for each language
- **Performance Analysis**: Time/space complexity documented for informed decisions
- **Pattern Library**: Quick reference for common algorithmic patterns
- **Production-Ready**: Clean, tested code with proper documentation

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

