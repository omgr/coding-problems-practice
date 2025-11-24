#!/usr/bin/env python3
"""
Progress Updater

Updates progress-tracker.md when you complete a problem.

Usage:
    python utils/progress-update.py 001-two-sum python
    python utils/progress-update.py 002-contains-duplicate all
"""

import sys
from pathlib import Path
import re
from datetime import datetime

LANGUAGE_MAP = {
    'python': 'Python',
    'py': 'Python',
    'javascript': 'JS',
    'js': 'JS',
    'typescript': 'TS',
    'ts': 'TS',
    'csharp': 'C#',
    'cs': 'C#',
    'go': 'Go',
    'all': 'ALL'
}

def update_progress(problem_number, languages):
    """Update progress tracker for a completed problem"""
    
    tracker_path = Path('docs/progress-tracker.md')
    
    if not tracker_path.exists():
        print(f"Error: {tracker_path} not found")
        return False
    
    content = tracker_path.read_text(encoding='utf-8')
    
    # Find the problem row in the tracker
    # Pattern: | 1 | Two Sum | Easy | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
    
    # For each language, replace ⬜ with ✅
    lines = content.split('\n')
    modified = False
    
    for i, line in enumerate(lines):
        # Check if this line contains the problem number
        if re.match(rf'^\|\s*{problem_number}\s*\|', line):
            # Split by |
            parts = line.split('|')
            if len(parts) >= 8:
                # parts[0] = empty, [1] = #, [2] = problem, [3] = difficulty,
                # [4] = Python, [5] = C#, [6] = JS, [7] = TS, [8] = Go
                
                if 'python' in languages or 'all' in languages:
                    parts[4] = ' ✅ '
                if 'csharp' in languages or 'cs' in languages or 'all' in languages:
                    parts[5] = ' ✅ '
                if 'javascript' in languages or 'js' in languages or 'all' in languages:
                    parts[6] = ' ✅ '
                if 'typescript' in languages or 'ts' in languages or 'all' in languages:
                    parts[7] = ' ✅ '
                if 'go' in languages or 'all' in languages:
                    parts[8] = ' ✅ '
                
                lines[i] = '|'.join(parts)
                modified = True
                print(f"✅ Updated problem {problem_number} for {', '.join(languages)}")
    
    if modified:
        # Update last modified date
        for i, line in enumerate(lines):
            if line.startswith('*Last Updated*:'):
                lines[i] = f"*Last Updated*: {datetime.now().strftime('%B %d, %Y')}"
        
        # Write back to file
        tracker_path.write_text('\n'.join(lines), encoding='utf-8')
        return True
    else:
        print(f"⚠️  Could not find problem {problem_number} in tracker")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python utils/progress-update.py <problem-number> <language>")
        print("Example: python utils/progress-update.py 1 python")
        print("         python utils/progress-update.py 2 all")
        sys.exit(1)
    
    try:
        problem_number = int(sys.argv[1])
    except ValueError:
        # Try to extract number from problem-id like "001-two-sum"
        match = re.match(r'(\d+)', sys.argv[1])
        if match:
            problem_number = int(match.group(1))
        else:
            print(f"Error: Invalid problem number: {sys.argv[1]}")
            sys.exit(1)
    
    languages = [sys.argv[2].lower()]
    if 'all' in languages:
        languages = ['python', 'csharp', 'javascript', 'typescript', 'go']
    
    if update_progress(problem_number, languages):
        print(f"\n✅ Progress updated successfully!")
        print(f"   Problem: {problem_number}")
        print(f"   Languages: {', '.join(languages)}")
    else:
        print("\n❌ Failed to update progress")
        sys.exit(1)

if __name__ == '__main__':
    main()


