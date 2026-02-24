import re
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return
        
    text = lines[0]
    pattern = lines[1]
    
    # re.findall возвращает список всех неперекрывающихся совпадений
    # re.escape гарантирует, что паттерн трактуется как обычная строка
    matches = re.findall(re.escape(pattern), text)
    print(len(matches))

if __name__ == "__main__":
    solve()