#
# Print Prime Numbers
#

import time

primes = [
  2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
  31, 37, 41, 43, 47, 53, 59, 61, 67, 71
]

def isPrime(num):
  # check if num is in primes list
  maxPrime = primes[-1]
  if num <= maxPrime: return num in primes

  # find next prime number
  for prime in primes:
    if num % prime == 0: return False
  return True

def printPrimeNumbers(start, stop, separator=','):
  print("Prime numbers between {} ~ {}:".format(start, stop))

  found = 0
  for num in range(start, stop+1):
    if isPrime(num):
      if found > 0:
        print(separator, end='')
        if found % 10 == 0: print('')
      print(num, end='')
      # if num > primes[-1]: primes.append(num)
      found += 1

  print('') # new line
  print('-' * min([found * 3, 60]))
  print("Total prime numbers found: {}".format(found))


tm1 = time.time()
printPrimeNumbers(1, 2000000, '  ')
tm2 = time.time()

print("Elapsed time: {}".format(tm2 - tm1))