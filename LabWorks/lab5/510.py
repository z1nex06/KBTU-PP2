import re
import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
        
    pattern = r'cat|dog'
    if re.search(pattern, line):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()