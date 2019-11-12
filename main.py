import math


divisors_dict = dict()


def is_prime(n):
    assert n > 0, "is_prime: N must be > 0, but was %i" % n
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def phi(n):
    assert n > 1, "phi: N must be > 1, but was %i" % n

    res = 0
    for m in range(1, n):
        rel_prime = True

        if m != 1 and n % m == 0:
            rel_prime = False
        elif m in divisors_dict.keys():
            for divisor in divisors_dict[m]:
                if n % divisor == 0 or n % (m / divisor) == 0:
                    rel_prime = False
                    break
        else:
            divisors_dict[m] = set()
            for divisor in range(2, round(m/2) + 1):
                if m % divisor == 0:
                    divisor_2 = int(m / divisor)
                    divisors_dict[m].add(divisor)
                    divisors_dict[m].add(divisor_2)

                    if n % divisor == 0 or n % divisor_2 == 0:
                        rel_prime = False
                        break

        if rel_prime:
            res += 1
    return res
