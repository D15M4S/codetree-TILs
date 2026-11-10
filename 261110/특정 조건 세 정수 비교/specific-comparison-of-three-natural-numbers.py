lst = list(map(int, input().split()))

a, b, c = lst

print(f"{1 if a == min(lst) else 0} {1 if a == b == c else 0}")
