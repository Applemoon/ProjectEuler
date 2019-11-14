from main import is_prime
from math import sqrt

# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
c = int(sqrt(n))
while True:
    c -= 1
    if is_prime(c) and n % c == 0:
        print(c)
        break
