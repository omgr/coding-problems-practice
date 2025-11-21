/*
 * Problem: Contains Duplicate
 * Difficulty: Easy
 * Pattern: Set for Uniqueness Check
 * 
 * Time Complexity Goal: O(n)
 * Space Complexity Goal: O(n)
 */

using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

namespace CodingInterviewPrep
{
    public class ContainsDuplicateSolution
    {
        /// <summary>
        /// Check if array contains any duplicates
        /// </summary>
        public static bool ContainsDuplicate(int[] nums)
        {
            // TODO: Implement using HashSet<int>
            // Hint: Try to add each element to HashSet
            
            return false;
        }

        public class TestCase
        {
            public int id { get; set; }
            public string description { get; set; }
            public TestInput input { get; set; }
            public bool expected { get; set; }
        }

        public class TestInput
        {
            public int[] nums { get; set; }
        }

        public class TestData
        {
            public string problem { get; set; }
            public List<TestCase> testCases { get; set; }
        }

        public static void RunTests()
        {
            string jsonString = File.ReadAllText("test-data.json");
            var data = JsonSerializer.Deserialize<TestData>(jsonString, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });

            Console.WriteLine(new string('=', 60));
            Console.WriteLine("Running Contains Duplicate Tests - C#");
            Console.WriteLine(new string('=', 60));

            int passed = 0, failed = 0;

            foreach (var test in data.testCases)
            {
                var nums = test.input.nums;
                var expected = test.expected;

                try
                {
                    var result = ContainsDuplicate(nums);

                    if (result == expected)
                    {
                        Console.WriteLine($"✅ Test {test.id}: PASSED");
                        passed++;
                    }
                    else
                    {
                        Console.WriteLine($"❌ Test {test.id}: FAILED - Expected {expected}, Got {result}");
                        failed++;
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"❌ Test {test.id}: ERROR - {ex.Message}");
                    failed++;
                }

                Console.WriteLine();
            }

            Console.WriteLine(new string('=', 60));
            Console.WriteLine($"Results: {passed} passed, {failed} failed");
            Console.WriteLine(new string('=', 60));

            if (passed == data.testCases.Count)
            {
                Console.WriteLine("🎉 All tests passed!");
            }
        }

        public static void Main(string[] args)
        {
            Console.WriteLine("Quick Test: [1,2,3,1] -> Expected: True");
            Console.WriteLine($"Your output: {ContainsDuplicate(new int[] { 1, 2, 3, 1 })}");
            Console.WriteLine();

            // RunTests();
        }
    }
}

