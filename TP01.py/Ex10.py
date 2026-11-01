# ---------------------------------------------------------------------------
# Problem 10 (Hard) · Prime numbers and Goldbach's conjecture
# ---------------------------------------------------------------------------
def is_prime(n):
    """True when n is a prime number. Tests divisors up to the square root."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


print("\nPrimes below 50:", end=" ")
count = 0
for n in range(50):
    if is_prime(n):
        print(n, end=" ")
for n in range(100):
    if is_prime(n):
        count += 1
print("\nNumber of primes below 100:", count)


def goldbach(n):
    """Return the first pair of primes (p, q) with p + q == n, or None."""
    for p in range(2, n // 2 + 1):
        if is_prime(p) and is_prime(n - p):
            return p, n - p
    return None


for n in range(4, 31, 2):
    p, q = goldbach(n)
    print(f"{n} = {p} + {q}")

# Check the conjecture for every even number from 4 to 10 000
all_ok = True
for n in range(4, 10001, 2):
    if goldbach(n) is None:
        all_ok = False
        print("Counter-example:", n)
        break
print("Goldbach holds for every even number from 4 to 10000:", all_ok)
