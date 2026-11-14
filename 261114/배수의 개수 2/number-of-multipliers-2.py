cnt = 0
for _ in range(10):
    cnt += (1 if int(input()) % 2 == 1 else 0)

print(cnt)