import re
import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
        
    pattern = r'\S+@\S+\.\S+'
    match = re.search(pattern, line)
    
    if match:
        print(match.group())
    else:
        print("No email")

if __name__ == "__main__":
    solve()