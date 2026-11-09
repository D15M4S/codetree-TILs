h, w = map(int, input().split())
b = (10000 * w) / (h * h)

print(int(b))
if b > 24:
    print('Obesity')