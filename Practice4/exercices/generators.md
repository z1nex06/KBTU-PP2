# Python generators
# 1. Square generator till N
```python
def gen_squares(n):
    for i in range(n + 1):
        yield i**2
```
# 2. Even numbers between 0 and n in comma separated form
```python
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
```
# 3. Numbers divisible by 3 and 4
```python
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
```
# 4. Squares from a to b
```python
def squares(a, b):
    for i in range(a, b + 1):
        yield i**2
```
# 5. Countdown from n to 0
```python
def countdown(n):
    for i in range(n, -1, -1):
        yield i
```
# Testing Even numbers output
```python
n_val = int(input("Enter n for even numbers: "))
print(",".join(map(str, even_numbers(n_val))))
```
