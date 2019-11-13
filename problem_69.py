from main import get_primes
import time
import math


# https://projecteuler.net/problem=69
# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less
# than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
# prime to nine, φ(9)=6.

# n	 | Relatively Prime | φ(n)	| n/φ(n)
# ---|------------------|-------|-------
# 2	 | 1	            | 1     | 2
# 3	 | 1,2	            | 2	    | 1.5
# 4	 | 1,3	            | 2	    | 2
# 5	 | 1,2,3,4	        | 4 	| 1.25
# 6	 | 1,5	            | 2	    | 3
# 7	 | 1,2,3,4,5,6	    | 6	    | 1.1666...
# 8	 | 1,3,5,7	        | 4	    | 2
# 9	 | 1,2,4,5,7,8	    | 6	    | 1.5
# 10 | 1,3,7,9	        | 4	    | 2.5

# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

N_MAX = 1000000

start_time = time.time()
primes = get_primes(int(math.sqrt(N_MAX)))


def get_n_to_divisors_dict(max_n):
    result_dict = dict()
    for p in primes:
        for n in range(p, max_n+1, p):
            if n in result_dict.keys():
                result_dict[n].add(p)
            else:
                result_dict[n] = {p}
    return result_dict


def phi(n):
    assert n > 1, "phi: N must be > 1, but was %i" % n

    ms = [1] * (n - 1)
    for divisor in n_to_divisors_dict[n]:
        for pointer in range(divisor, n, divisor):
            ms[pointer-1] = 0
    return sum(ms)


print("---- 1: %s seconds ----" % (time.time() - start_time))
n_to_divisors_dict = get_n_to_divisors_dict(N_MAX)
print("---- 2: %s seconds ----" % (time.time() - start_time))


num = 1
for p in sorted(primes):
    new_num = num * p
    if new_num > N_MAX:
        break
    num = new_num

n_phi_num = num / phi(num)

print("---- answer: max_n_phi = %i for n = %i ----" % (n_phi_num, num))

print("---- 3: %s seconds ----" % (time.time() - start_time))
