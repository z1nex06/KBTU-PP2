import re
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return
        
    text = lines[0]
    pattern = lines[1]
    
    escaped_pattern = re.escape(pattern)
    matches = re.findall(escaped_pattern, text)
    print(len(matches))

if __name__ == "__main__":
    solve()