import re
import sys

def solve():
    # Читаем строку из стандартного ввода
    line = sys.stdin.read().strip()
    
    # re.match проверяет соответствие паттерну именно с начала строки
    # Паттерн 'Hello' ищет буквальное совпадение
    if re.match(r'Hello', line):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()