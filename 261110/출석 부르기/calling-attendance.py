students = ["John", "Tom", "Paul"]
n = int(input())

print(students[n - 1] if 1 <= n <= len(students) else "Vacancy")