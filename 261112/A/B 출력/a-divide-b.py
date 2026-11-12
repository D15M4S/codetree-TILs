a, b = map(int, input().split())

print(a // b, end='.')

a %= b

i = 0
while i < 20:
    a *= 10
    print(a // b, end='')
    a %= b
    i += 1