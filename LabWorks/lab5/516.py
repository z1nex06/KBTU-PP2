import re
import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
        
    pattern = r'Name: (.+), Age: (.+)'
    match = re.search(pattern, line)
    
    if match:
        print(f"{match.group(1)} {match.group(2)}")

if __name__ == "__main__":
    solve()