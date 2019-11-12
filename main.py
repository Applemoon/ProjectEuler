import math

prime_divisors_dict = dict()


def is_prime(n):
    assert n > 0, "is_prime: N must be > 0, but was %i" % n
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def save_prime_divisors(n):
    divisors = set()
    for divisor in range(2, round(n / 2) + 1):  # can be optimized somehow
        if n % divisor == 0 and is_prime(divisor):
            divisors.add(divisor)
    prime_divisors_dict[n] = divisors


def phi(n):
    assert n > 1, "phi: N must be > 1, but was %i" % n

    save_prime_divisors(n)
    res = 1
    for m in range(2, n):
        rel_prime = True

        for divisor in prime_divisors_dict[m]:
            if divisor in prime_divisors_dict[n]:
                rel_prime = False
                break

        if rel_prime:
            res += 1
    return res
