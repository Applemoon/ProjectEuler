import math


def is_prime(n):
    assert n > 0, "is_prime: N must be > 0, but was %i" % n
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(max_prime):
    primes = set()
    for i in range(2, max_prime+1):
        if is_prime(i):
            primes.add(i)
    return primes
