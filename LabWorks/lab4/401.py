import sys

def square_generator(n):
    # Создаем генератор, который вычисляет квадраты по одному
    for i in range(1, n + 1):
        yield i * i

def main():
    # Читаем входные данные
    line = sys.stdin.readline()
    if not line:
        return
    
    try:
        n = int(line.strip())
        # Итерируемся по генератору и выводим результат
        for square in square_generator(n):
            print(square)
    except ValueError:
        pass

if __name__ == "__main__":
    main()