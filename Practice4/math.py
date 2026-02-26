# Python Math

# 1. Convert degree to radian
```python
import math
degree = float(input("Input degree: "))
print(f"Output radian: {math.radians(degree):.6f}")
```
# 2. Area of a trapezoid
```python
import math
h = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
print(f"Expected Output: {(base1 + base2) / 2 * h}")
```
# 3. Area of regular polygon
```python
import math
n_sides = int(input("Input number of sides: "))
side_len = float(input("Input the length of a side: "))
polygon_area = (n_sides * side_len**2) / (4 * math.tan(math.pi / n_sides))
print(f"The area of the polygon is: {int(polygon_area)}")
```
# 4. Area of a parallelogram
```python
import math
p_base = float(input("Length of base: "))
p_height = float(input("Height of parallelogram: "))
print(f"Expected Output: {float(p_base * p_height)}")
```
