#!/usr/bin/env python3
"""
Test All Solutions - Multi-Language Test Runner

This utility runs tests for a problem across all 5 languages and
provides a summary of results.

Usage:
    python utils/test-all.py problems/01-arrays-and-hashing/001-two-sum
    python utils/test-all.py problems/01-arrays-and-hashing/001-two-sum --language python
"""

import subprocess
import sys
import os
from pathlib import Path
import time

LANGUAGES = {
    'python': {'file': 'solution.py', 'command': 'python'},
    'javascript': {'file': 'solution.js', 'command': 'node'},
    'typescript': {'file': 'solution.ts', 'command': 'ts-node'},
    'csharp': {'file': 'solution.cs', 'command': 'dotnet script'},
    'go': {'file': 'solution.go', 'command': 'go run'}
}

def run_test(problem_path, language):
    """Run test for a specific language"""
    lang_config = LANGUAGES[language]
    solution_file = Path(problem_path) / lang_config['file']
    
    if not solution_file.exists():
        return {
            'language': language,
            'status': 'NOT_FOUND',
            'message': f'{lang_config["file"]} not found',
            'time': 0
        }
    
    try:
        start_time = time.time()
        result = subprocess.run(
            f'{lang_config["command"]} {solution_file}',
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=problem_path
        )
        elapsed = time.time() - start_time
        
        # Check output for test results
        output = result.stdout + result.stderr
        
        if result.returncode == 0:
            # Look for test results in output
            if 'All tests passed' in output or '🎉' in output:
                status = 'PASSED'
            elif 'passed' in output.lower():
                status = 'PARTIAL'
            else:
                status = 'UNKNOWN'
        else:
            status = 'FAILED'
        
        return {
            'language': language,
            'status': status,
            'time': elapsed,
            'output': output[:500]  # First 500 chars
        }
        
    except subprocess.TimeoutExpired:
        return {
            'language': language,
            'status': 'TIMEOUT',
            'message': 'Test took longer than 30 seconds',
            'time': 30
        }
    except Exception as e:
        return {
            'language': language,
            'status': 'ERROR',
            'message': str(e),
            'time': 0
        }

def print_results(results):
    """Print formatted test results"""
    print("\n" + "=" * 70)
    print("MULTI-LANGUAGE TEST RESULTS")
    print("=" * 70)
    
    status_emoji = {
        'PASSED': '✅',
        'PARTIAL': '⚠️',
        'FAILED': '❌',
        'ERROR': '🔥',
        'TIMEOUT': '⏱️',
        'NOT_FOUND': '🚫',
        'UNKNOWN': '❓'
    }
    
    for result in results:
        lang = result['language'].title()
        status = result['status']
        emoji = status_emoji.get(status, '❓')
        time_str = f"{result.get('time', 0):.2f}s"
        
        print(f"\n{emoji} {lang:12} {status:10} {time_str:>8}")
        
        if 'message' in result:
            print(f"   Message: {result['message']}")
        
        if result.get('output') and status == 'FAILED':
            print(f"   Output: {result['output'][:200]}...")
    
    print("\n" + "=" * 70)
    
    # Summary
    passed = sum(1 for r in results if r['status'] == 'PASSED')
    total = len(results)
    print(f"Summary: {passed}/{total} languages passed all tests")
    print("=" * 70 + "\n")
    
    return passed == total

def main():
    if len(sys.argv) < 2:
        print("Usage: python test-all.py <problem-path> [--language <lang>]")
        print("Example: python test-all.py problems/01-arrays-and-hashing/001-two-sum")
        sys.exit(1)
    
    problem_path = sys.argv[1]
    
    if not Path(problem_path).exists():
        print(f"Error: Problem path '{problem_path}' not found")
        sys.exit(1)
    
    # Check if specific language requested
    languages_to_test = list(LANGUAGES.keys())
    if '--language' in sys.argv:
        lang_index = sys.argv.index('--language')
        if lang_index + 1 < len(sys.argv):
            requested_lang = sys.argv[lang_index + 1].lower()
            if requested_lang in LANGUAGES:
                languages_to_test = [requested_lang]
            else:
                print(f"Unknown language: {requested_lang}")
                print(f"Available: {', '.join(LANGUAGES.keys())}")
                sys.exit(1)
    
    print(f"\nTesting problem: {problem_path}")
    print(f"Languages: {', '.join(lang.title() for lang in languages_to_test)}\n")
    
    results = []
    for language in languages_to_test:
        print(f"Testing {language.title()}...", end=' ', flush=True)
        result = run_test(problem_path, language)
        results.append(result)
        print(f"{result['status']}")
    
    all_passed = print_results(results)
    
    sys.exit(0 if all_passed else 1)

if __name__ == '__main__':
    main()

