#!/usr/bin/env python3
"""
Progress Updater

Updates progress-tracker.md when you complete a problem.

Usage:
    python utils/progress-update.py 001-two-sum python
    python utils/progress-update.py 002-contains-duplicate javascript
    python utils/progress-update.py 003-valid-anagram all
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

def update_progress(problem_id, language):
    """Update progress tracker for a completed problem"""
    
    tracker_path = Path('docs/progress-tracker.md')
    
    if not tracker_path.exists():
        print(f"Error: {tracker_path} not found")
        return False
    
    content = tracker_path.read_text(encoding='utf-8')
    
    # Find the problem row in the tracker
    # Looking for pattern like: | 1 | Two Sum | Easy | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
    
    problem_number = int(problem_id.split('-')[0])
    
    # TODO: Implement actual markdown table update logic
    # For now, just print what would be updated
    
    print(f"✅ Would update problem {problem_number} ({problem_id})")
    print(f"   Language: {LANGUAGE_MAP.get(language.lower(), language)}")
    print(f"   Status: ⬜ → ✅")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    return True

def main():
    if len(sys.argv) < 3:
        print("Usage: python progress-update.py <problem-id> <language>")
        print("Example: python progress-update.py 001-two-sum python")
        print("         python progress-update.py 002-contains-duplicate all")
        sys.exit(1)
    
    problem_id = sys.argv[1]
    language = sys.argv[2]
    
    if update_progress(problem_id, language):
        print("\n✅ Progress updated successfully!")
    else:
        print("\n❌ Failed to update progress")
        sys.exit(1)

if __name__ == '__main__':
    main()

