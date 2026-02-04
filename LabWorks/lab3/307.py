import math
import sys

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = int(new_x)
        self.y = int(new_y)

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

def solve():
    # Читаем все входные данные сразу
    input_data = sys.stdin.read().split()
    if len(input_data) < 6:
        return

    # 1. Исходная точка
    p1 = Point(input_data[0], input_data[1])
    p1.show()

    # 2. Перемещение первой точки
    p1.move(input_data[2], input_data[3])
    p1.show()

    # 3. Вторая точка для расчета расстояния
    p2 = Point(input_data[4], input_data[5])
    
    # 4. Расчет и вывод расстояния
    distance = p1.dist(p2)
    print(f"{distance:.2f}")

if __name__ == "__main__":
    solve()