a, b = map(int, input().split())

if a > b:
    a, b = b, a

print(sum([i for i in range(a, b + 1) if i % 5 == 0]))