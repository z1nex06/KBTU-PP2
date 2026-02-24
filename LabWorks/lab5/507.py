import re
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 3:
        return
        
    text = lines[0]
    pattern = lines[1]
    replacement = lines[2]
    
    result = re.sub(re.escape(pattern), replacement, text)
    print(result)

if __name__ == "__main__":
    solve()