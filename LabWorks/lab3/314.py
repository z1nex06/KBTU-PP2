import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())

operations = []
for _ in range(q):
    line = sys.stdin.readline().split()
    op_type = line[0]
    
    if op_type == "add":
        x = int(line[1])
        operations.append(lambda val, x=x: val + x)
    elif op_type == "multiply":
        x = int(line[1])
        operations.append(lambda val, x=x: val * x)
    elif op_type == "power":
        x = int(line[1])
        operations.append(lambda val, x=x: val ** x)
    elif op_type == "abs":
        operations.append(lambda val: abs(val))

for op in operations:
    a = [op(val) for val in a]

print(*(a))