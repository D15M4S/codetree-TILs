n = int(input())

case2, case3, case12 = 0, 0, 0
for n in range(1, n + 1):
    if n % 12 == 0:
        case12 += 1
    elif n % 3 == 0:
        case3 += 1
    elif n % 2 == 0:
        case2 += 1

print(case2, case3, case12)