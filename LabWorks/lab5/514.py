import re
import sys

def solve():
    line = sys.stdin.read().strip('\n\r')
    
    pattern = re.compile(r'^\d+$')
    
    if pattern.match(line):
        print("Match")
    else:
        print("No match")

if __name__ == "__main__":
    solve()