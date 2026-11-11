sex = int(input())
age = int(input())

if sex == 1:
    print("WOMAN" if age >= 19 else "GIRL")
else:
    print("MAN" if age >= 19 else "BOY")