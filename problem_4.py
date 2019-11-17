import time
from main import is_palindromic

start_time = time.time()

# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

max_pal = 0
for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        product = i * j
        if is_palindromic(product) and product > max_pal:
            max_pal = product

print("---- answer = %i ----" % max_pal)

print("---- %s seconds ----" % (time.time() - start_time))
