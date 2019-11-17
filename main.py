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


def get_fibonacci_sequence(n):
    a = 1
    b = 2
    sequence = list((a, b))
    while True:
        c = a + b
        if c < n:
            sequence.append(c)
            a = b
            b = c
        else:
            break

    return sequence


def is_palindromic(n):
    n_str = str(n)
    digits = len(n_str)
    result = True
    for i in range(int(digits/2)):
        if n_str[i] != n_str[digits - i - 1]:
            result = False
    return result
