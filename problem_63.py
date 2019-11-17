import time

start_time = time.time()

# https://projecteuler.net/problem=63
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number,
# 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

answer = 0
in_range = True
digits = 0

while in_range:
    in_range = False
    digits += 1
    for i in range(int(pow(10, digits - 1) ** (1 / digits)), int(int('9' * digits) ** (1 / digits)) + 1):
        if len(str(i ** digits)) == digits:
            answer += 1
            in_range = True

print("---- answer = %i ----" % answer)

print("---- %s seconds ----" % (time.time() - start_time))
