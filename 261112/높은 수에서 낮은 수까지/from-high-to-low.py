a, b = map(int, input().split())

max = a if a > b else b
min = a if a < b else b

print(*[i for i in range(max, min - 1, -1)])