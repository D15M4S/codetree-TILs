n = int(input())

divisors = [i for i in range(1, n) if n % i == 0]

print('P' if sum(divisors) == n else 'N')