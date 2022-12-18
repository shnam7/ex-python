#
# Print Prime Numbers
#

import time


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if (n % i) == 0:
            return False
    return True


def print_prime_numbers(start, stop, separator=','):
    print(F"Prime numbers between {start} ~ {stop}:")

    found = 0
    for num in range(start, stop+1):
        if is_prime(num):
            print(num, end='')
            found += 1
            print() if found % 10 == 0 else print(separator, end='')

    print('')  # new line
    print('-' * min([found * 3, 60]))
    print("Total prime numbers found: {}".format(found))


tm1 = time.time()
print_prime_numbers(1, 2000000, '  ')
tm2 = time.time()

print(f"Elapsed time: {tm2 - tm1} seconds")
