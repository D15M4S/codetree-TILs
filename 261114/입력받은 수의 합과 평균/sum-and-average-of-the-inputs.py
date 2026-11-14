n = int(input())

lst = [int(input()) for i in range(n)]

print(f'{sum(lst)} {sum(lst)/len(lst):.1f}')