a, b = map(int, input().split())
a = (a + 1 if a % 2 == 0 else a)
b = (b - 1 if b % 2 == 0 else b)
print(*[i for i in range(a, b + 1, 2)])