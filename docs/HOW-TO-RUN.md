# 🚀 How to Run the Code

This guide will help you execute and test your solutions in all 5 languages.

---

## 📋 Prerequisites

Make sure you have the following installed:
- ✅ Python 3.12+
- ✅ Node.js 22+ (for JavaScript/TypeScript)
- ✅ .NET 8.0+
- ✅ Go 1.25+
- ✅ TypeScript (installed globally)

---

## 🐍 Running Python Solutions

### Option 1: Run a specific solution
```bash
cd problems/01-arrays-and-hashing/001-two-sum
python solution.py
```

### Option 2: Run with tests
```bash
cd problems/01-arrays-and-hashing/001-two-sum
python solution.py

# Uncomment run_tests() in the file or modify the file to call it
```

### Using Python's unittest (if available)
```bash
python -m pytest solution.py  # If pytest is installed
```

---

## 📜 Running JavaScript Solutions

### Execute JavaScript file
```bash
cd problems/01-arrays-and-hashing/001-two-sum
node solution.js
```

### Run with tests
The test function is already in the file. Uncomment `runTests()` at the bottom:
```javascript
// Change this line from:
// runTests();

// To:
runTests();
```

Then run:
```bash
node solution.js
```

---

## 📘 Running TypeScript Solutions

### Option 1: Using ts-node (recommended)
```bash
cd problems/01-arrays-and-hashing/001-two-sum
ts-node solution.ts
```

### Option 2: Compile then run
```bash
cd problems/01-arrays-and-hashing/001-two-sum
tsc solution.ts
node solution.js
```

### Run with tests
Uncomment `runTests()` in the solution file before running.

---

## 💎 Running C# Solutions

### Option 1: Run directly with dotnet
```bash
cd problems/01-arrays-and-hashing/001-two-sum
dotnet script solution.cs
```

### Option 2: Create a project (recommended for better IDE support)
```bash
cd problems/01-arrays-and-hashing/001-two-sum

# Create a console app
dotnet new console -n TwoSum
cd TwoSum

# Replace Program.cs with solution.cs content
# Or copy solution.cs and modify the project

dotnet run
```

### Option 3: Using .NET Interactive (if installed)
```bash
dotnet tool install -g Microsoft.dotnet-interactive
dotnet interactive jupyter install

# Then open in Jupyter or use dotnet script
```

### Quick run without project:
```bash
# Make sure you're in the problem directory
csc solution.cs
./solution.exe  # On Windows
```

---

## 🔵 Running Go Solutions

### Run Go file directly
```bash
cd problems/01-arrays-and-hashing/001-two-sum
go run solution.go
```

### Build and run (faster for multiple executions)
```bash
cd problems/01-arrays-and-hashing/001-two-sum
go build solution.go
./solution  # On Unix/Mac
solution.exe  # On Windows
```

### Run with tests
Uncomment `runTests()` in the solution file before running.

---

## 🧪 Testing Your Solutions

### Running Tests

Each solution file has a `runTests()` function that reads from `test-data.json` in the same directory.

**To enable tests:**
1. Open the solution file
2. Find the commented line (usually at the bottom):
   - Python: `# run_tests()`
   - JavaScript/TypeScript: `// runTests();`
   - C#: `// RunTests();`
   - Go: `// runTests()`
3. Uncomment it
4. Run the file

### Understanding Test Output

**✅ Test Passed:**
```
✅ Test 1: PASSED
   Input: nums=[2, 7, 11, 15], target=9
   Output: [0, 1]
```

**❌ Test Failed:**
```
❌ Test 2: FAILED
   Input: nums=[3, 2, 4], target=6
   Expected: [1, 2]
   Got: [0, 2]
```

---

## 🎯 Recommended Workflow

### Starting a New Problem

1. **Read the Problem**
   ```bash
   cd problems/01-arrays-and-hashing/001-two-sum
   cat README.md  # or open in your editor
   ```

2. **Understand Test Cases**
   ```bash
   cat test-data.json
   ```

3. **Choose Your Primary Language** (Python or C# as recommended)

4. **Implement the Solution**
   - Open solution.py or solution.cs
   - Read the TODO comments
   - Explain your approach in comments
   - Implement the function

5. **Test Your Solution**
   - Uncomment the test line
   - Run the file
   - Debug if needed

6. **Implement in Other Languages**
   - Once working in primary language
   - Port logic to other languages
   - Test each one

---

## 🐛 Debugging Tips

### Python
```python
# Add print statements
print(f"Debug: num={num}, complement={complement}")

# Use debugger
import pdb; pdb.set_trace()
```

### JavaScript/TypeScript
```javascript
// Console log
console.log('Debug:', { num, complement });

// Use Node debugger
node --inspect-brk solution.js
```

### C#
```csharp
// Console output
Console.WriteLine($"Debug: num={num}, complement={complement}");

// Use Visual Studio or VS Code debugger
```

### Go
```go
// Print statements
fmt.Printf("Debug: num=%d, complement=%d\n", num, complement)

// Use delve debugger
dlv debug solution.go
```

---

## ⚡ Pro Tips

### 1. Use an IDE with Language Support
- **VS Code**: Works great for all 5 languages
  - Extensions: Python, JavaScript, C#, Go
- **JetBrains**: PyCharm, WebStorm, Rider, GoLand
- **Visual Studio**: Best for C#

### 2. Keep Test Data Valid
The `test-data.json` file must be valid JSON and in the same directory as the solution file.

### 3. Manage Multiple Terminals
Open separate terminals for each language to quickly switch between them:
```bash
Terminal 1: Python development
Terminal 2: JavaScript/TypeScript
Terminal 3: C#
Terminal 4: Go
```

### 4. Version Control Your Work
```bash
# Initialize git if you haven't
git init
git add .
git commit -m "Solved Two Sum in all 5 languages"

# Push to GitHub
git remote add origin <your-repo-url>
git push -u origin main
```

### 5. Time Yourself
For timed challenges, use a timer:
```bash
# Unix/Mac
time go run solution.go

# Or use a stopwatch app
```

---

## 🆘 Common Issues

### Issue: "Module not found" in Python
**Solution**: Make sure you're in the correct directory with test-data.json

### Issue: "Cannot find name" in TypeScript
**Solution**: Check imports and ensure types are defined

### Issue: C# won't compile
**Solution**: Ensure you have the right using statements and Main method

### Issue: Go "undefined: package"
**Solution**: Check if test-data.json exists in the same directory

---

## 📞 Need Help?

If you encounter issues:
1. Check the error message carefully
2. Ensure all prerequisites are installed
3. Verify you're in the correct directory
4. Check that test-data.json is valid JSON

---

**Happy Coding! 🎉**

