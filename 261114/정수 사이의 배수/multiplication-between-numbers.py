a, b = map(int, input().split())

nums = [i for i in range(a, b + 1)
        if i % 5 == 0 or i % 7 == 0]

print(f'{sum(nums)} {sum(nums) / len(nums):.1f}')