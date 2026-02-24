import re
import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
        
    def double_digit(match):
        return match.group(0) * 2
        
    result = re.sub(r'\d', double_digit, line.rstrip('\n\r'))
    print(result)

if __name__ == "__main__":
    solve()