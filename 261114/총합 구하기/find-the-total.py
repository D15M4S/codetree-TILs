a, b = map(int, input().split())


print(sum([i for i in range(a, b + 1) if i % 6 == 0 and i % 8 != 0]))