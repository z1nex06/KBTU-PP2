import math
import sys

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        # Используем формулу площади круга pi * r^2
        return math.pi * (self.radius ** 2)

def solve():
    # Считываем радиус из стандартного ввода
    line = sys.stdin.read().strip()
    if not line:
        return
    
    r = int(line)
    
    # Создаем объект круга и считаем площадь
    my_circle = Circle(r)
    result = my_circle.area()
    
    # Выводим с точностью 2 знака после запятой
    print(f"{result:.2f}")

if __name__ == "__main__":
    solve()