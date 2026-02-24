import re
import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
        
    pattern = r'\d{2,}'
    matches = re.findall(pattern, line)
    
    if matches:
        print(" ".join(matches))
    else:
        print()

if __name__ == "__main__":
    solve()