/*
 * Problem: Valid Anagram
 * Difficulty: Easy
 * Pattern: Character Frequency Counting
 * 
 * Time Complexity Goal: O(n)
 * Space Complexity Goal: O(1)
 */

using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Linq;

public class ValidAnagramSolution
{
        /// <summary>
        /// Check if t is an anagram of s
        /// </summary>
        public static bool IsAnagram(string s, string t)
        {
            // TODO: Implement using Dictionary<char, int>
            // Hint: LINQ can help with sorting approach
            // Alternative: Count frequencies manually
            
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
            public string s { get; set; }
            public string t { get; set; }
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
            Console.WriteLine("Running Valid Anagram Tests - C#");
            Console.WriteLine(new string('=', 60));

            int passed = 0, failed = 0;

            foreach (var test in data.testCases)
            {
                var s = test.input.s;
                var t = test.input.t;
                var expected = test.expected;

                try
                {
                    var result = IsAnagram(s, t);

                    if (result == expected)
                    {
                        Console.WriteLine($"✅ Test {test.id}: PASSED");
                        passed++;
                    }
                    else
                    {
                        Console.WriteLine($"❌ Test {test.id}: FAILED");
                        Console.WriteLine($"   Input: s=\"{s}\", t=\"{t}\"");
                        Console.WriteLine($"   Expected: {expected}, Got: {result}");
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

}

// Quick manual test (global code for dotnet script)
Console.WriteLine("Quick Test: s=\"anagram\", t=\"nagaram\" -> Expected: True");
Console.WriteLine($"Your output: {ValidAnagramSolution.IsAnagram(\"anagram\", \"nagaram\")}");
Console.WriteLine();

// Uncomment to run all tests
// ValidAnagramSolution.RunTests();

