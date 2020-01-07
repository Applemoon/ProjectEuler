# -*- coding: utf-8 -*-

# imports ##################################################################
#!/usr/bin/env python
import math
import time
import string

# functions ##################################################################

def makeListUnique(lst):
    seen = set()
    seen_add = seen.add
    return [x for x in lst if not (x in seen or seen_add(x))]


def isPrime(number):
    if number < 2: return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def isVeryPrime(number):
    if not isPrime(number):
        return False

    for i in range(1, len(str(number))):
        if not isPrime(int(str(number)[i:])) or not isPrime(int(str(number)[:-i])):
            return False

    return True


def isNatural(number):
    return number % 1 == 0


def triangleNumber(p):
    return int(p * (p + 1) / 2)


def pentagonalNumber(p):
    return int(p * (3 * p - 1) / 2);


def hexagonalNumber(p):
    return p * (2 * p - 1)


def allDivisors(number, distinct = False, proper = True, withOne = False):
    if not number or number < 1:
        return None
    elif number == 1:
        return [1]

    if withOne:
        divisors = [1]
    else:
        divisors = []

    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            divisors.append(i)
            if distinct:
                number /= i

    if not proper: divisors.append(number)

    return divisors


def divisorsCount(number):
    if not number or number < 1:
        return 0
    elif number == 1:
        return 1

    divisors_count = 2

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if number/i == i:
                divisors_count += 1
            else:
                divisors_count += 2

    return divisors_count


def isEven(number):
    return number % 2 == 0


def isOdd(number):
    return not isEven(number)


def digitsSum(number):
    return sum([int(x) for x in str(number)])


def isPerfect(number):
    return number == sum(allDivisors(number, proper = True))


def isAbundant(number):
    return number < sum(allDivisors(number, proper = True))


def isSumOfPowersOfDigits(number, power):
    return sum([pow(int(x),power) for x in str(number)]) == number and number != 1


def isStringPandigital(string, minVal, maxVal):
    return sorted(string) == [str(digit) for digit in range(minVal, maxVal + 1)]


def isNumberPandigital(number, minVal, maxVal):
    return isStringPandigital(str(number), minVal, maxVal)


def isNumberCurious(number):
    if number < 3: return False
    return sum([math.factorial(int(digit)) for digit in str(number)]) == number


def isCircularPrime(number):
    numberString = str(number)
    digits = [int(x) for x in numberString]
    
    for i in range(len(digits)):
        numberString = numberString[1:] + numberString[0]
        if not isPrime(int(numberString)):
            return False
    return True


def stringIsPalindromic(string):
    for i in range(len(string)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True


def numIsPalindromicDecAndBin(number):
    return stringIsPalindromic(str(number)) and stringIsPalindromic(str(bin(number)[2:]))


def getAllCombinations(string):
    combinations = list()
    if len(string) == 1:
        return string

    for index in range(len(string)):
        secondStringPart = getAllCombinations(string[:index] + string[index + 1:])
        char = string[index]
        for second in secondStringPart:
            combinations.append((char + second))
    return makeListUnique(combinations)


def getWordValue(word):
    return sum([string.uppercase.index(letter) + 1 for letter in word.upper()])


def getListFromFile(filename):
    return [word[1:-1] for word in open(filename, 'r').read().split(',')]


def getLinesFromFile(filename):
    return [line for line in open(filename, 'r').read().split('\n')]


def isWordTriangle(word):
    value = getWordValue(word)
    for i in range(1, value+1):
        if value == triangleNumber(i):
            return True
    return False


def generateMasks(constDigitsNumber, starsNumber):
    preMasks = makeListUnique(["".join(sorted(str(i))).zfill(constDigitsNumber)+"".join(['*']*starsNumber) for i in range(10**constDigitsNumber)])
    masks = list()
    for preMask in preMasks:
        masks += getAllCombinations(preMask)
    return masks


def sameDigits2Numbers(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


def sameDigitsList(numbersList):
    if len(numbersList) < 2: return False
    for i in range(len(numbersList)-1):
        if not sameDigits2Numbers(numbersList[i], numbersList[i+1]):
            return False
    return True



t1 = time.monotonic()
# solving ##################################################################

# 60

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any
#  order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The 
#  sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


d2 = {}    

def goodPair(n1, n2):
    return True
    if (n1 > n2 and n2 in d2.get(n1, [])) or (n1 in d2.get(n2, [])):
        return True

    s1, s2 = str(n1), str(n2)
    return isPrime(int(s1 + s2)) and isPrime(int(s2 + s1))


primes = []
d3, d4 = {}, {}
cur = 1
index = 0
while True:
    cur += 1
    if not isPrime(cur):
        continue

    primes.append(cur)

    index += 1
    if index % 20 == 0: print(cur)

    # make d2
    for prev in primes[:-1]:
        if goodPair(prev, cur): # долго
            d2.setdefault(cur, []).append(prev)
            # a = 2

    # make d3
    for pair1 in d2.get(cur, []):
        for pair11 in d2.get(pair1, []):
            if goodPair(cur, pair11):
                d3.setdefault(cur, []).append([pair1, pair11])

    # make d4
    for pair1, pair2 in d3.get(cur, []):
        if pair1 not in d3:
            continue
        
        goodPairs = []
        for pair11, pair12 in d3.get(pair1, []):
            if goodPair(cur, pair11) and goodPair(cur, pair12):
                goodPairs = [pair11, pair12]

        if goodPairs != []:
            d4.setdefault(cur, []).append([pair1] + goodPairs)
            break

    # check d5
    for pair1, pair2, pair3 in d4.get(cur, []):
        for pair11, pair12, pair13 in d4.get(pair1, []):
            if goodPair(cur, pair11) and goodPair(cur, pair12) and goodPair(cur, pair13):
                print("WHAT???", cur, pair1, pair11, pair12, pair13)
                break


# done ######################################################### #########
print("### Done in %s seconds ###" % (time.monotonic() - t1))
