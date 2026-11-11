mid_term, final_term = map(int, input().split())

award = 0
if mid_term >= 90:
    award += 100_000 if final_term >= 95 else (50_000 if final_term >= 90 else 0)

print(award)