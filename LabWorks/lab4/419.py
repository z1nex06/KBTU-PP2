import sys
import math

def solve():
    d = sys.stdin.read().split()
    if not d: return
    r, ax, ay, bx, by = map(float, d)

    def dist(x1, y1, x2, y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    d_ab = dist(ax, ay, bx, by)
    
    # Расстояние от центра (0,0) до отрезка AB
    # Проекция центра на прямую
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        print(f"{0.0:.10f}")
        return

    t = -(ax * dx + ay * dy) / (dx*dx + dy*dy)
    if 0 < t < 1:
        px, py = ax + t*dx, ay + t*dy
        h = dist(0, 0, px, py)
    else:
        h = min(dist(0,0,ax,ay), dist(0,0,bx,by))

    # Если путь не пересекает круг (h >= r), идем по прямой
    if h >= r - 1e-9:
        print(f"{d_ab:.10f}")
        return

    # Если пересекает, считаем: касательная от A + дуга + касательная от B
    oa = dist(0, 0, ax, ay)
    ob = dist(0, 0, bx, by)
    
    # Длины касательных
    la = math.sqrt(oa*oa - r*r)
    lb = math.sqrt(ob*ob - r*r)
    
    # Углы
    alpha = math.acos(r / oa)
    beta = math.acos(r / ob)
    # Полный угол между OA и OB
    gamma = math.acos(max(-1.0, min(1.0, (ax*bx + ay*by) / (oa*ob))))
    
    # Угол дуги
    arc_angle = gamma - alpha - beta
    
    if arc_angle < 0:
        # Случай, когда прямая видимость не перекрыта телом круга
        print(f"{d_ab:.10f}")
    else:
        total = la + lb + r * arc_angle
        print(f"{total:.10f}")

if __name__ == "__main__":
    solve()