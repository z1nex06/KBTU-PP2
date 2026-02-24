import re
import sys

def solve():
    line = sys.stdin.read().strip('\n\r')
    
    # ^[a-zA-Z] - начинается с буквы
    # .* - любые символы (ноль или более)
    # [0-9]$ - заканчивается цифрой
    if re.match(r'^[a-zA-Z].*[0-9]$', line):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()