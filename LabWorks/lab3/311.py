import sys

class Pair:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self, other):
        # Создаем и возвращаем новый объект Pair, 
        # складывая соответствующие атрибуты
        sum_a = self.a + other.a
        sum_b = self.b + other.b
        return Pair(sum_a, sum_b)

def solve():
    # Читаем все числа из ввода
    data = sys.stdin.read().split()
    if len(data) < 4:
        return

    # Создаем два объекта Pair
    p1 = Pair(data[0], data[1])
    p2 = Pair(data[2], data[3])

    # Складываем их через метод add
    result = p1.add(p2)

    # Выводим результат в нужном формате
    print(f"Result: {result.a} {result.b}")

if __name__ == "__main__":
    solve()