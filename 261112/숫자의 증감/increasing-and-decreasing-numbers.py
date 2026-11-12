c, n = input().split()
n = int(n)

if c == 'A':
    print(*[i for i in range(1, n + 1)])
else:
    print(*[i for i in range(n, 0, -1)])