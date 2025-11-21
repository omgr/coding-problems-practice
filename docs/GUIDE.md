# 🚀 Complete Guide - Coding Problems Practice

A comprehensive guide to navigating this repository, understanding the approach, and using it for your own learning.

---

## 📖 Table of Contents
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [How to Use This Repository](#how-to-use-this-repository)
- [Running Solutions](#running-solutions)
- [Learning Path](#learning-path)
- [Philosophy & Approach](#philosophy--approach)
- [Contributing & Forking](#contributing--forking)

---

## Overview

This repository contains implementations of fundamental algorithms and data structures across **five programming languages**: Python, C#, JavaScript, TypeScript, and Go.

**Purpose:**
- Practice and deepen understanding of algorithmic patterns
- Maintain sharp problem-solving skills
- Create a practical reference library for production code
- Explore how concepts manifest across different programming paradigms

**Languages:**
- **Python**: Rapid prototyping, clear syntax
- **C#**: Type-safe, enterprise-grade implementations
- **JavaScript**: Functional programming capabilities
- **TypeScript**: Type safety with JS flexibility
- **Go**: Concurrent, efficient, modern simplicity

---

## Repository Structure

```
coding-problems-practice/
├── README.md                    # Portfolio overview
├── LICENSE                      # MIT License
├── concepts/                    # Pattern guides and explanations
│   └── 01-arrays-and-hashing.md
├── problems/                    # All coding problems
│   └── 01-arrays-and-hashing/
│       ├── 001-two-sum/
│       │   ├── README.md        # Problem statement
│       │   ├── test-data.json   # Comprehensive test cases
│       │   ├── solution.py      # Python implementation
│       │   ├── solution.js      # JavaScript implementation
│       │   ├── solution.ts      # TypeScript implementation
│       │   ├── solution.cs      # C# implementation
│       │   └── solution.go      # Go implementation
│       ├── 002-contains-duplicate/
│       └── 003-valid-anagram/
├── challenges/                  # Timed coding challenges
├── solutions/                   # Completed, production-ready solutions
└── utils/                       # Helper scripts and test runners
```

---

## Getting Started

### Prerequisites

Ensure you have the following installed:
- **Python**: 3.8+ (`python --version`)
- **Node.js**: 14+ (`node --version`)
- **TypeScript**: Latest (`npm install -g typescript ts-node`)
- **.NET SDK**: 6.0+ (`dotnet --version`)
- **Go**: 1.16+ (`go version`)

### Clone the Repository

```bash
git clone https://github.com/omgr/coding-problems-practice.git
cd coding-problems-practice
```

### Explore a Problem

```bash
cd problems/01-arrays-and-hashing/001-two-sum
cat README.md  # Read the problem
```

---

## How to Use This Repository

### For Learning

1. **Start with Concepts**: Read pattern guides in `concepts/` folder
2. **Pick a Problem**: Navigate to `problems/[topic]/[problem-name]/`
3. **Read the Problem**: Open `README.md` for full problem statement
4. **Try to Solve**: Implement in your preferred language first
5. **Test Your Solution**: Use provided test data
6. **Compare Approaches**: Study implementations across languages
7. **Understand Trade-offs**: Review time/space complexity

### For Reference

- **Quick Lookup**: Find pattern in `concepts/`, then see implementation
- **Copy & Adapt**: All code is production-ready with comprehensive tests
- **Compare Languages**: See how same algorithm differs across paradigms
- **Use in Projects**: Implementations are MIT licensed

### For Practice

- **Solve Before Looking**: Try to implement before viewing solutions
- **Implement in Multiple Languages**: Deepens understanding
- **Add Your Own Tests**: Extend test cases
- **Optimize**: Try to improve time/space complexity
- **Document**: Add comments explaining your thinking

---

## Running Solutions

### Python
```bash
cd problems/01-arrays-and-hashing/001-two-sum
python solution.py
```

### JavaScript
```bash
cd problems/01-arrays-and-hashing/001-two-sum
node solution.js
```

### TypeScript
```bash
cd problems/01-arrays-and-hashing/001-two-sum
ts-node solution.ts
```

### C#
```bash
cd problems/01-arrays-and-hashing/001-two-sum
# Option 1: Using dotnet script
dotnet script solution.cs

# Option 2: Compile and run
csc solution.cs
./solution.exe  # Windows: .\solution.exe
```

### Go
```bash
cd problems/01-arrays-and-hashing/001-two-sum
go run solution.go
```

### Running All Tests (Multi-Language)
```bash
python utils/test-all.py problems/01-arrays-and-hashing/001-two-sum
```

---

## Learning Path

The repository follows a structured progression through algorithmic patterns:

### Phase 1: Foundational Patterns
**Module 1: Arrays & Hash Tables**
- Two Sum (HashMap lookup)
- Contains Duplicate (Set operations)
- Valid Anagram (Frequency counting)
- *Pattern*: Using hash tables for O(1) lookups

**Module 2: Strings & Stacks**
- Valid Parentheses (Stack matching)
- String manipulation patterns
- *Pattern*: LIFO operations, character analysis

**Module 3: Linked Lists**
- Reverse Linked List (Pointer manipulation)
- Merge Two Sorted Lists (Two-pointer merge)
- Linked List Cycle (Floyd's algorithm)
- *Pattern*: Pointer manipulation, cycle detection

### Phase 2: Search & Optimization
**Module 4: Binary Search**
- Classic binary search
- Boundary problems
- *Pattern*: Divide and conquer, O(log n) complexity

**Module 5: Two Pointers**
- Converging pointers on sorted arrays
- Multiple pointer techniques
- *Pattern*: O(n) optimization on arrays

**Module 6: Sliding Window**
- Variable and fixed window sizes
- Subarray optimization problems
- *Pattern*: Optimal subarray/substring solutions

### Phase 3: Tree & Graph Algorithms
**Module 7-8: Binary Trees**
- Tree traversal (DFS, BFS)
- BST operations
- *Pattern*: Recursive tree problems

**Module 9: Graphs**
- Grid traversal (DFS/BFS)
- Connectivity problems
- Topological sort
- *Pattern*: Graph representations and traversal

### Phase 4: Advanced Algorithms
**Module 10-11: Dynamic Programming**
- Memoization and tabulation
- State machines
- Optimization problems
- *Pattern*: Overlapping subproblems, optimal substructure

---

## Philosophy & Approach

### Pattern-First Thinking
Instead of memorizing thousands of problems, master 15-20 core patterns that solve 80% of algorithmic challenges.

### Multi-Language Implementation
Implementing the same algorithm in 5 languages:
- Separates algorithmic thinking from syntax
- Reveals language-specific optimizations
- Shows when to use which language
- Deepens understanding of core concepts

### Production Quality
Every implementation includes:
- Comprehensive test suites
- Time/space complexity analysis
- Clean, documented code
- Edge case handling
- Ready for real-world use

### Real-World Application
Each pattern has practical uses:
- **HashMap Lookup**: Caching, deduplication, fast lookups
- **Two Pointers**: In-place manipulation, memory efficiency
- **Dynamic Programming**: Resource optimization, cost minimization
- **Tree/Graph Traversal**: File systems, dependency resolution

---

## Test Data Structure

Each problem includes `test-data.json` with:

```json
{
  "problem": "Two Sum",
  "testCases": [
    {
      "id": 1,
      "description": "Basic test case",
      "input": {"nums": [2, 7, 11, 15], "target": 9},
      "expected": [0, 1],
      "explanation": "nums[0] + nums[1] = 2 + 7 = 9"
    }
  ]
}
```

- **Small cases**: Verify correctness
- **Edge cases**: Handle boundaries
- **Large datasets**: Test performance (up to 10,000 elements)

---

## Contributing & Forking

### Fork for Your Own Practice
```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR_USERNAME/coding-problems-practice.git
cd coding-problems-practice

# Add your solutions
git add .
git commit -m "Solved Two Sum"
git push
```

### Customize the Repository
- Add your own problems
- Implement in additional languages
- Create custom test cases
- Document your learnings
- Build your portfolio

### Best Practices
1. **Solve before looking**: Try to implement before viewing solutions
2. **Test thoroughly**: Use all provided test cases
3. **Document thinking**: Add comments explaining your approach
4. **Optimize iteratively**: Start with correct, then optimize
5. **Compare implementations**: Learn from cross-language differences

---

## Problem Complexity Reference

### Time Complexity Goals
- **Arrays/Hashing**: O(n) with O(n) space
- **Two Pointers**: O(n) with O(1) space
- **Binary Search**: O(log n)
- **Trees**: O(n) for traversal, O(log n) for BST operations
- **Graphs**: O(V + E) for traversal
- **Dynamic Programming**: O(n) to O(n²) depending on problem

### Space Complexity Considerations
- Hash tables: O(n) additional space
- Two pointers: O(1) additional space
- Recursion: O(h) call stack (h = height)
- DP: O(n) to O(n²) for memoization

---

## Key Algorithmic Patterns

### 1. HashMap Lookup
**When to use**: Need fast lookups, counting frequencies, finding pairs
**Time**: O(n), **Space**: O(n)
**Example**: Two Sum, Group Anagrams

### 2. Two Pointers
**When to use**: Sorted arrays, finding pairs, partitioning
**Time**: O(n), **Space**: O(1)
**Example**: Two Sum II, Container With Most Water

### 3. Sliding Window
**When to use**: Subarrays/substrings, contiguous elements
**Time**: O(n), **Space**: O(1) to O(k)
**Example**: Longest Substring, Max Subarray

### 4. Binary Search
**When to use**: Sorted data, finding boundaries
**Time**: O(log n), **Space**: O(1)
**Example**: Search in Rotated Array, First/Last Position

### 5. DFS/BFS
**When to use**: Trees, graphs, connected components
**Time**: O(V + E), **Space**: O(V)
**Example**: Number of Islands, Course Schedule

### 6. Dynamic Programming
**When to use**: Optimization, counting ways, overlapping subproblems
**Time**: O(n) to O(n²), **Space**: O(n) to O(n²)
**Example**: Climbing Stairs, Longest Common Subsequence

---

## Tips for Success

### Understanding Over Memorization
- Grasp the "why" behind each algorithm
- Understand when to apply each pattern
- Know the trade-offs

### Test-Driven Development
- Write tests first (or use provided ones)
- Start with simple cases
- Add edge cases
- Test with large inputs

### Iterative Improvement
1. **First pass**: Make it work (correctness)
2. **Second pass**: Make it right (clean code)
3. **Third pass**: Make it fast (optimize)
4. **Fourth pass**: Make it elegant (refactor)

### Cross-Language Learning
- Implement in one language first (preferably Python or your strongest)
- Port to other languages
- Notice paradigm differences
- Appreciate language-specific features

---

## Common Pitfalls to Avoid

### Array/String Problems
- Off-by-one errors in indices
- Not handling empty inputs
- Forgetting to check array bounds

### Hash Table Problems
- Not checking if key exists before accessing
- Overwriting values unintentionally
- Not considering hash collisions

### Tree/Graph Problems
- Forgetting base cases in recursion
- Not handling null/None nodes
- Infinite loops in graphs (need visited tracking)

### Dynamic Programming
- Not identifying overlapping subproblems
- Incorrect state transitions
- Wrong initialization of DP array

---

## Resources & Learning

### Concept Guides
See `concepts/` folder for deep dives into each pattern:
- Arrays and Hashing
- Two Pointers and Sliding Window
- Binary Search
- Trees and Graphs
- Dynamic Programming

### Additional Learning
- **Time Complexity**: Big O notation guide
- **Space Complexity**: Memory usage analysis
- **Problem Patterns**: When to use which approach

---

## FAQ

**Q: Should I implement in all 5 languages?**
A: Start with 1-2 languages you're comfortable with. Add more languages as you progress to deepen understanding.

**Q: What if I can't solve a problem?**
A: Read the problem carefully, try brute force first, then optimize. Study the solution and implement it yourself with understanding.

**Q: How long should each problem take?**
A: First implementation: 15-30 minutes. Cross-language ports: 5-10 minutes each. Don't rush - understanding matters more than speed.

**Q: Can I use this code in my projects?**
A: Yes! All code is MIT licensed. Attribution appreciated but not required.

**Q: How do I track my progress?**
A: Fork the repo, add a progress section to your README, or use the provided progress tracker utility.

---

## License

MIT License - See LICENSE file for details.

Feel free to use, modify, and distribute this code. Attribution appreciated!

---

## Contact

For questions, suggestions, or collaboration:
- GitHub: [@omgr](https://github.com/omgr)
- LinkedIn: [Madan Gopal Ongole](https://www.linkedin.com/in/ongolemadangopal/)
- Email: ongolemadangopal@gmail.com

---

**Happy Coding!** 🚀

May your algorithms be efficient and your code be clean.

