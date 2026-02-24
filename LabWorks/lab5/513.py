import re
import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
        
    pattern = r'\w+'
    matches = re.findall(pattern, line)
    print(len(matches))

if __name__ == "__main__":
    solve()