cnt = 0
for _ in range(int(input())):
    i = int(input())
    cnt += i if i % 2 == 1 and i % 3 == 0 else 0
print(cnt)