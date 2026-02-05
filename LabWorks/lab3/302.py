import sys

def isUsual(num):
    # Числа меньше или равные 0 обычно не считаются "usual"
    if num <= 0:
        return False
    
    # Пока число делится на 2, делим его на 2
    while num % 2 == 0:
        num //= 2
        
    # Пока число делится на 3, делим его на 3
    while num % 3 == 0:
        num //= 3
        
    # Пока число делится на 5, делим его на 5
    while num % 5 == 0:
        num //= 5
    
    # Если в конце осталась 1, значит других простых множителей нет
    return num == 1

def solve():
    # Читаем входное число
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
        
    n = int(input_data)
    
    # Проверяем и выводим результат
    if isUsual(n):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()