lst = [int(input()) for _ in range(10)]
lst = [i for i in lst if 0 <= i <= 200]

print(f'{sum(lst)} {sum(lst) / len(lst):.1f}')