/*
 * Problem: Group Anagrams
 * Difficulty: Medium
 * Pattern: HashMap + String Processing
 * 
 * Time Complexity Goal: O(n × k) or O(n × k log k)
 * Space Complexity Goal: O(n × k)
 */

using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Linq;

public class GroupAnagramsSolution
{
    /// <summary>
    /// Group anagrams together from the input array
    /// </summary>
    public static List<List<string>> GroupAnagrams(string[] strs)
    {
        // TODO: Implement using Dictionary<string, List<string>>
        // Hint 1: Use sorted string as key: string.Join("", str.OrderBy(c => c))
        // Hint 2: Or use character count array as key
        Dictionary<string,List<string>> ags = new();
        foreach(string w in strs){
            string sw = string.Join("",w.OrderBy(c => c));
            if(ags.ContainsKey(sw)){
                ags[sw].Add(w);
            }
            else{
                ags[sw] = new List<string>{w};
            }

        }
        return ags.Values.ToList();
    }

    public class TestCase
    {
        public int id { get; set; }
        public string description { get; set; }
        public TestInput input { get; set; }
        public List<List<string>> expected { get; set; }
    }

    public class TestInput
    {
        public string[] strs { get; set; }
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
        Console.WriteLine("Running Group Anagrams Tests - C#");
        Console.WriteLine(new string('=', 60));

        int passed = 0, failed = 0;

        foreach (var test in data.testCases)
        {
            var strs = test.input.strs;
            var expected = test.expected;

            try
            {
                var result = GroupAnagrams(strs);

                // Sort for comparison (order doesn't matter)
                var resultSorted = result.Select(g => string.Join(",", g.OrderBy(s => s)))
                                        .OrderBy(s => s).ToList();
                var expectedSorted = expected.Select(g => string.Join(",", g.OrderBy(s => s)))
                                            .OrderBy(s => s).ToList();

                if (resultSorted.SequenceEqual(expectedSorted))
                {
                    Console.WriteLine($"✅ Test {test.id}: PASSED");
                    passed++;
                }
                else
                {
                    Console.WriteLine($"❌ Test {test.id}: FAILED");
                    Console.WriteLine($"   Input: [{string.Join(", ", strs.Select(s => $"\"{s}\""))}]");
                    Console.WriteLine($"   Expected groups: {expected.Count}");
                    Console.WriteLine($"   Got groups: {result.Count}");
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

// Quick manual test
Console.WriteLine("Quick Test: [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]");
var quickTestResult = GroupAnagramsSolution.GroupAnagrams(new[] { "eat", "tea", "tan", "ate", "nat", "bat" });
Console.WriteLine($"Your output: {quickTestResult.Count} groups");
foreach (var group in quickTestResult)
{
    Console.WriteLine($"  [{string.Join(", ", group)}]");
}
Console.WriteLine();

GroupAnagramsSolution.RunTests();



