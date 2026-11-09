a = int(input())

a += 3 if a % 2 == 1 else 0
a /= 3 if a % 3 == 0 else 1

print(int(a))