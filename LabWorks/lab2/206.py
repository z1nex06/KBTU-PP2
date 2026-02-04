x = int(input())
num = list(map(int, input().split()))
cnt = num[0]
for i in num:
    if i > cnt:
        cnt = i
print(cnt)