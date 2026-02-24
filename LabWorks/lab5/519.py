import re
import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
        
    pattern = re.compile(r'\b\w+\b')
    matches = pattern.findall(line)
    print(len(matches))

if __name__ == "__main__":
    solve()