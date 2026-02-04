x = int(input())
num = list(map(int, input().split()))
maxval = num[0]
pos = 1
for i in range(x):
    if num[i] > maxval:
        maxval = num[i]
        pos = i + 1
print(pos)