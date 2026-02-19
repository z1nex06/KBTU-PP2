import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    x1, y1 = float(data[0]), float(data[1])
    x2, y2 = float(data[2]), float(data[3])
    
    # B' = (x2, -y2)
    # Прямая через (x1, y1) и (x2, -y2):
    # (x - x1) / (x2 - x1) = (y - y1) / (-y2 - y1)
    # Ищем x при y = 0:
    # -x1 / (x2 - x1) = -y1 / (-y2 - y1) (ошибка в пропорции, считаем через подобие)
    
    # Из подобия треугольников: x = x1 + (x2 - x1) * (y1 / (y1 + y2))
    # y всегда 0 по условию задачи (отражение от оси Ox)
    
    rx = x1 + (x2 - x1) * (y1 / (y1 + y2))
    ry = 0.0
    
    print(f"{rx:.10f} {ry:.10f}")

if __name__ == "__main__":
    solve()