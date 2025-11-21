# 🎯 Getting Started - Your First Day

Welcome to your coding interview preparation journey! This guide will help you get started with Day 1.

---

## ✅ Before You Begin

### 1. Verify Your Environment

Open PowerShell and run these commands to verify everything is installed:

```powershell
# Check Python
python --version
# Expected: Python 3.12.6

# Check Node.js
node --version
# Expected: v22.16.0

# Check TypeScript
tsc --version
# Expected: Version 5.x.x

# Check .NET
dotnet --version
# Expected: 8.0.403

# Check Go (restart terminal first)
go version
# Expected: go version go1.25.4
```

**If Go doesn't work**: Close and reopen your terminal for PATH updates to take effect.

---

## 📁 Navigate to the Repository

```powershell
cd "C:\Users\Ongole Madan gopal R\Documents\Personal\Learn\coding-interview-prep"
```

---

## 📚 Day 1: Arrays and Hashing

### Problem 1: Two Sum

Let's start with the first problem together!

#### Step 1: Read the Problem
```powershell
cd problems\01-arrays-and-hashing\001-two-sum
code README.md  # Or open in your preferred editor
```

#### Step 2: Before You Code - Coaching Questions

I'll ask you these questions. Take your time to think:

**Q1: What is a Hash Table (HashMap/Dictionary)?**
- What does it store?
- Why is lookup O(1)?
- How is it different from an array?

**Q2: What approach should we use?**
- Brute force: Two nested loops - O(n²)
- Optimized: HashMap - O(n)
- Which one and why?

**Q3: What will we store in the HashMap?**
- The number itself as key? Or index?
- What will be the value?
- Why this choice?

**Take 5 minutes to explain these to yourself or write them down.**

---

#### Step 3: Implement in Python (Primary Language)

Open `solution.py`:
```powershell
code solution.py
```

**Your Implementation Steps:**

1. **Write your approach in comments**
   ```python
   # Approach:
   # 1. Create a dictionary to store numbers we've seen
   # 2. For each number, calculate complement = target - number
   # 3. If complement exists in dictionary, return [index_of_complement, current_index]
   # 4. Otherwise, store current number with its index
   ```

2. **Implement the function**
   - Replace the `pass` statement
   - Use the approach you described
   - Add comments explaining each step

3. **Example Implementation Structure:**
   ```python
   def two_sum(nums: List[int], target: int) -> List[int]:
       seen = {}  # num -> index
       
       for i, num in enumerate(nums):
           complement = target - num
           
           # Check if complement exists
           if complement in seen:
               return [seen[complement], i]
           
           # Store current number
           seen[num] = i
       
       return []  # No solution found
   ```

4. **Test Your Solution**
   - Uncomment the `# run_tests()` line at the bottom
   - Run: `python solution.py`
   - Debug if any tests fail

---

#### Step 4: Explain Your Solution

Before moving to the next language, answer these:

1. **Time Complexity**: What is it? Why?
2. **Space Complexity**: What is it? Why?
3. **Trade-offs**: What did we gain? What did we sacrifice?
4. **Edge Cases**: What edge cases does this handle?

Write your answers in comments in the code!

---

#### Step 5: Implement in C# (Second Primary Language)

Open `solution.cs`:
```powershell
code solution.cs
```

**Port your Python logic to C#:**
- Use `Dictionary<int, int>` instead of Python dict
- Use `ContainsKey()` instead of `in` operator
- Use for loop instead of enumerate

**Test it:**
```powershell
csc solution.cs
.\solution.exe
```

---

#### Step 6: Implement in JavaScript

Open `solution.js`:
```powershell
code solution.js
```

**Port to JavaScript:**
- Use `Map` or plain object `{}`
- Use `for...of` or traditional for loop
- Test: `node solution.js`

---

#### Step 7: Implement in TypeScript

Open `solution.ts`:
```powershell
code solution.ts
```

**Port to TypeScript:**
- Add type annotations: `Map<number, number>`
- Notice how TypeScript catches errors!
- Test: `ts-node solution.ts`

---

#### Step 8: Implement in Go

Open `solution.go`:
```powershell
code solution.go
```

**Port to Go:**
- Use `map[int]int`
- Check existence: `value, exists := m[key]`
- Test: `go run solution.go`

---

## 🎯 After Completing Two Sum

Take a 10-minute break! Then:

### Self-Assessment Questions:

1. ✅ Can you explain when to use HashMap vs array?
2. ✅ Can you implement this problem from memory in Python?
3. ✅ Can you implement it in C#?
4. ✅ Do you understand the O(1) vs O(n) lookup difference?
5. ✅ Can you identify similar problems that use this pattern?

If you answered **yes to all 5**, move to Problem 2!

If **no to any**, review the concept guide:
```powershell
cd ..\..\..
code concepts\01-arrays-and-hashing.md
```

---

## 🎯 Problem 2: Contains Duplicate

```powershell
cd problems\01-arrays-and-hashing\002-contains-duplicate
```

**Repeat the same process:**
1. Read README.md
2. Think about approach
3. Implement in Python
4. Explain your solution
5. Port to C#, JS, TS, Go
6. Test everything

**Key Questions for This Problem:**
- When to use a Set vs HashMap?
- Can you do it in one line in Python?
- What's the time vs space trade-off?

---

## 🎯 Problem 3: Valid Anagram

```powershell
cd problems\01-arrays-and-hashing\003-valid-anagram
```

**This introduces a new pattern: Frequency Counting**

**Key Questions:**
- How do you count character occurrences?
- Sorting vs HashMap - which is better?
- Why is this O(1) space even with a HashMap?

---

## 📊 Tracking Your Progress

After each problem, update your progress:

```powershell
cd ..\..\..
code progress-tracker.md
```

Change ⬜ to ✅ for completed problems in each language.

---

## 🏆 End of Day 1

After completing all 3 problems in all 5 languages, you should:

### Update Progress
- Mark Day 1 problems as complete
- Note time spent
- Write key learnings

### Reflect
Answer in progress-tracker.md under "Day 1 Reflections":
- **What went well?**
- **What was challenging?**
- **Key learnings?**
- **Ready for tomorrow?**

### Celebrate! 🎉
You just solved 3 problems × 5 languages = **15 implementations**!

---

## 📅 Tomorrow: Day 2

Day 2 focuses on:
- Strings manipulation
- Stack data structure
- New pattern: LIFO operations

**Preparation:**
- Review concept guide for stacks
- Get good rest
- 4 hours commitment (2 morning + 2 evening)

---

## 🆘 If You Get Stuck

### Problem Understanding
- Re-read the problem statement
- Draw examples on paper
- Look at the test cases

### Implementation Issues
- Add print/console.log statements
- Test with simple inputs first
- Compare with concept guide examples

### Conceptual Confusion
- Read the concept guide for that topic
- Draw diagrams
- Explain it out loud

### Need Help?
- Take a break and come back
- Try a simpler example first
- Move to the next problem and return later

**Remember**: Struggle is part of learning. Don't give up!

---

## 💡 Pro Tips for Day 1

1. **Time Management**
   - Two Sum: ~1 hour for all languages
   - Contains Duplicate: ~45 minutes
   - Valid Anagram: ~45 minutes
   - Testing & Review: ~30 minutes
   - **Total: ~3 hours**

2. **Implementation Order**
   - Always start with Python or C# (your primary)
   - Port to the other primary language
   - Then do JavaScript, TypeScript, Go

3. **Don't Rush**
   - Understanding > Speed
   - Speed will come with practice
   - Focus on explaining your approach

4. **Use Comments**
   - Document your thinking
   - Explain the algorithm
   - Note complexity analysis
   - Future you will thank you!

---

## ✅ Day 1 Checklist

Before you start Day 2, make sure you've:

- [ ] Completed Two Sum in all 5 languages
- [ ] Completed Contains Duplicate in all 5 languages
- [ ] Completed Valid Anagram in all 5 languages
- [ ] All tests passing for each solution
- [ ] Updated progress-tracker.md
- [ ] Written reflections for Day 1
- [ ] Understand HashMap lookup pattern
- [ ] Understand Set usage pattern
- [ ] Understand frequency counting pattern
- [ ] Feel confident to explain these patterns

---

**You've got this! Let's start with Two Sum. Take your time, and remember: understanding is more important than speed.** 🚀

---

## 🔗 Quick Links

- [Learning Plan](learning-plan.md) - Full 14-day curriculum
- [Progress Tracker](progress-tracker.md) - Track your progress
- [How to Run](HOW-TO-RUN.md) - Detailed running instructions
- [Arrays & Hashing Concepts](concepts/01-arrays-and-hashing.md) - Deep dive

---

**Ready? Let's begin!** 🎯

