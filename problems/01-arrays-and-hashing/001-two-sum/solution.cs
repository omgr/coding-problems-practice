/*
 * Problem: Two Sum
 * Difficulty: Easy
 * Topic: Arrays & Hash Tables
 * Pattern: HashMap Lookup
 * 
 * Problem Statement:
 * Given an array of integers nums and an integer target, return indices of the 
 * two numbers such that they add up to target.
 * 
 * Example:
 *     Input: nums = [2,7,11,15], target = 9
 *     Output: [0,1]
 *     Explanation: nums[0] + nums[1] == 9, so we return [0, 1]
 * 
 * Constraints:
 *     - 2 <= nums.length <= 10^4
 *     - -10^9 <= nums[i] <= 10^9
 *     - -10^9 <= target <= 10^9
 *     - Only one valid answer exists
 * 
 * Time Complexity Goal: O(n)
 * Space Complexity Goal: O(n)
 */

using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Linq;

namespace CodingInterviewPrep
{
    public class TwoSumSolution
    {
        /// <summary>
        /// Find two numbers in the array that add up to the target.
        /// </summary>
        /// <param name="nums">Array of integers</param>
        /// <param name="target">Target sum</param>
        /// <returns>Indices of the two numbers</returns>
        /// 
        /// Approach:
        ///     TODO: Explain your approach here before implementing
        ///     
        ///     1. What data structure will you use in C#?
        ///     2. Dictionary<int, int> - what does each part represent?
        ///     3. How will you find the complement?
        /// 
        /// Implementation Steps:
        ///     TODO: Break down your implementation into steps
        ///     
        ///     Step 1: 
        ///     Step 2: 
        ///     Step 3: 
        public static int[] TwoSum(int[] nums, int target)
        {
            // TODO: Implement your solution here
            
            // Hint: Use Dictionary<int, int> to store numbers you've seen
            // Key is the number, Value is the index
            // Key concept: For each number, check if (target - number) exists
            
            // Remove the line below and implement your solution
            return new int[] { };
        }

        // Test data classes
        public class TestCase
        {
            public int id { get; set; }
            public string description { get; set; }
            public TestInput input { get; set; }
            public int[] expected { get; set; }
            public string explanation { get; set; }
        }

        public class TestInput
        {
            public int[] nums { get; set; }
            public int target { get; set; }
        }

        public class TestData
        {
            public string problem { get; set; }
            public List<TestCase> testCases { get; set; }
        }

        /// <summary>
        /// Run all test cases from test-data.json
        /// </summary>
        public static void RunTests()
        {
            // Load test data
            string jsonString = File.ReadAllText("test-data.json");
            var data = JsonSerializer.Deserialize<TestData>(jsonString, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });

            Console.WriteLine(new string('=', 60));
            Console.WriteLine("Running Two Sum Tests - C#");
            Console.WriteLine(new string('=', 60));

            int passed = 0;
            int failed = 0;

            foreach (var test in data.testCases)
            {
                var nums = test.input.nums;
                var target = test.input.target;
                var expected = test.expected;

                try
                {
                    var result = TwoSum(nums, target);

                    // Check if result matches expected (order doesn't matter)
                    var resultSorted = result.OrderBy(x => x).ToArray();
                    var expectedSorted = expected.OrderBy(x => x).ToArray();
                    bool isCorrect = resultSorted.SequenceEqual(expectedSorted);

                    if (isCorrect)
                    {
                        Console.WriteLine($"✅ Test {test.id}: PASSED");
                        Console.WriteLine($"   Input: nums=[{string.Join(", ", nums)}], target={target}");
                        Console.WriteLine($"   Output: [{string.Join(", ", result)}]");
                        passed++;
                    }
                    else
                    {
                        Console.WriteLine($"❌ Test {test.id}: FAILED");
                        Console.WriteLine($"   Input: nums=[{string.Join(", ", nums)}], target={target}");
                        Console.WriteLine($"   Expected: [{string.Join(", ", expected)}]");
                        Console.WriteLine($"   Got: [{string.Join(", ", result)}]");
                        failed++;
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"❌ Test {test.id}: ERROR");
                    Console.WriteLine($"   Input: nums=[{string.Join(", ", nums)}], target={target}");
                    Console.WriteLine($"   Error: {ex.Message}");
                    failed++;
                }

                Console.WriteLine();
            }

            // Summary
            Console.WriteLine(new string('=', 60));
            Console.WriteLine($"Results: {passed} passed, {failed} failed out of {passed + failed} tests");
            Console.WriteLine(new string('=', 60));

            if (passed == data.testCases.Count)
            {
                Console.WriteLine("🎉 Congratulations! All tests passed!");
                Console.WriteLine("\nTime Complexity Analysis:");
                Console.WriteLine("  - What is the time complexity of your solution?");
                Console.WriteLine("  - Why is it better than brute force O(n²)?");
                Console.WriteLine("\nSpace Complexity Analysis:");
                Console.WriteLine("  - What is the space complexity of your solution?");
                Console.WriteLine("  - What are you storing in memory?");
                Console.WriteLine("\nC# Specific:");
                Console.WriteLine("  - Dictionary vs Hashtable - why use Dictionary?");
                Console.WriteLine("  - How does LINQ help in testing?");
            }
            else
            {
                Console.WriteLine("Keep trying! Debug the failing tests.");
            }
        }

        public static void Main(string[] args)
        {
            // Quick manual test
            Console.WriteLine("Quick Test:");
            Console.WriteLine("Input: [2, 7, 11, 15], target = 9");
            Console.WriteLine("Expected: [0, 1]");
            try
            {
                var result = TwoSum(new int[] { 2, 7, 11, 15 }, 9);
                Console.WriteLine($"Your output: [{string.Join(", ", result)}]");
            }
            catch
            {
                Console.WriteLine("Your output: Not implemented yet");
            }
            Console.WriteLine();

            // Uncomment the line below when you're ready to run all tests
            // RunTests();
        }
    }
}

