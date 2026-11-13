n = int(input())

lst = [i for i in range(n, 100 + 1)]

for i in lst:
    print('A' if i >= 90 else ('B' if i >= 80 else ('C' if i >= 70 else ('D' if i >= 60 else 'F'))), end = ' ')