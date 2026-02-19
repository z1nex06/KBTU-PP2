import sys
import math

def solve():
    try:
        # Чтение данных
        input_data = sys.stdin.read().split()
        if not input_data:
            return
            
        r = float(input_data[0])
        ax, ay = float(input_data[1]), float(input_data[2])
        bx, by = float(input_data[3]), float(input_data[4])
        
        # Вектор направления D = B - A
        dx, dy = bx - ax, by - ay
        
        # Квадратное уравнение: ||A + tD||^2 <= R^2
        # (ax + t*dx)^2 + (ay + t*dy)^2 <= r^2
        # t^2 * (dx^2 + dy^2) + t * 2*(ax*dx + ay*dy) + (ax^2 + ay^2 - r^2) <= 0
        
        a = dx*dx + dy*dy
        b = 2 * (ax*dx + ay*dy)
        c = ax*ax + ay*ay - r*r
        
        # Если A и B совпадают
        if a == 0:
            if ax*ax + ay*ay <= r*r + 1e-9:
                print(f"{0.0:.10f}")
            else:
                print(f"{0.0:.10f}")
            return

        # Ищем корни t^2 * a + t * b + c = 0
        discriminant = b*b - 4*a*c
        
        if discriminant < 0:
            # Отрезок полностью вне круга
            print(f"{0.0:.10f}")
            return
            
        sqrt_d = math.sqrt(discriminant)
        t1 = (-b - sqrt_d) / (2 * a)
        t2 = (-b + sqrt_d) / (2 * a)
        
        # Находим пересечение интервала [t1, t2] с интервалом [0, 1]
        t_start = max(0.0, t1)
        t_end = min(1.0, t2)
        
        if t_start < t_end:
            # Длина части траектории = длина вектора D * разницу параметров t
            segment_len = math.sqrt(a) * (t_end - t_start)
            print(f"{segment_len:.10f}")
        else:
            print(f"{0.0:.10f}")
            
    except (ValueError, IndexError):
        pass

if __name__ == "__main__":
    solve()