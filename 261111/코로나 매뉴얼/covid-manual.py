
cnt = 0

for _ in range(3):
    symptom, temperature = input().split()
    temperature = int(temperature)

    cnt += 1 if symptom == 'Y' and temperature >= 37 else 0

print('E' if cnt >= 2 else 'N')