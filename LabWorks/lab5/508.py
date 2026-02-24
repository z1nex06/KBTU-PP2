import re
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return
        
    text = lines[0]
    pattern = lines[1]
    
    parts = re.split(pattern, text)
    print(",".join(parts))

if __name__ == "__main__":
    solve()