lst = list(map(int, input().split()))

total = sum(lst)
avg = sum(lst) / len(lst)

print(total)
print(int(avg))
print(int(total - avg))
