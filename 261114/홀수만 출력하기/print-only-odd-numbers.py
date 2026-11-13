n = int(input())

for _ in range(n):
    target = int(input())
    if target % 2 == 1 and target % 3 == 0:
        print(target)
