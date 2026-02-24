import re
import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
        
    # \d находит любую отдельную цифру от 0 до 9
    digits = re.findall(r'\d', line)
    
    if digits:
        print(" ".join(digits))
    else:
        print()

if __name__ == "__main__":
    solve()