m = int(input())

print('Winter' if m == 12 or m <= 2 else ('Fall' if m >= 9 else ('Summer' if m >= 6 else 'Spring')))