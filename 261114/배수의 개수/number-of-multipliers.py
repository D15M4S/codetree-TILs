cnt_3, cnt_5 = 0, 0

for _ in range(10):
    n = int(input())
    cnt_3 += 1 if n % 3 == 0 else 0
    cnt_5 += 1 if n % 5 == 0 else 0
print(cnt_3, cnt_5)