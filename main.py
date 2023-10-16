def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = []
    for p in range(2, n + 1):
        if primes[p]:
            prime_numbers.append(p)

    return prime_numbers

n = 100
result = sieve_of_eratosthenes(n)
print(result)