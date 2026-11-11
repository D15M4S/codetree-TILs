a_age, a_sex = input().split()
a_age = int(a_age)

b_age, b_sex = input().split()
b_age = int(b_age)

flag = False

flag = (True if a_age >= 19 and a_sex == 'M' else False) or (True if b_age >= 19 and b_sex == 'M' else False)

print(1 if flag else 0)