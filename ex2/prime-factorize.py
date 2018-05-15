#
#   Prime Factorizer
#
#   Written by Soo-hyuk Nam
#   Feb 26, 2017
#

def prime_factorize(num):
    """Prime number factorizer"""

    primeCount = 0      # number of prime numbers found
    numReach = 1        # multiplied values of prime numbers found
    numTarget = num     # remaining amount to break in search of prime numbers

    for i in range(2, num):
        # print('num={0} i={1} num%i={2} numReach={3}'.format(num, i, num % i, numReach))
        while num % i == 0:
            if primeCount > 0:
                print('*', end='')
            print(i, end='', flush=True)
            primeCount += 1
            num //= i
            numReach *= i

        if numReach == numTarget:
            if num > 1:
                print('*{0}'.format(num), end='')
            break
    if primeCount == 0:
        print(numTarget, end='')
    return


def run_factorizer():
    """Application Main"""
    while True:
        val = input("Enter a number(0 to exit): ").strip()
        if not val.isdigit():
            print("Please enter an integer number!\n")
            continue

        num = int(val)
        if num == 0: break

        prime_factorize(num)
        print()     # new line


#--- main ---
run_factorizer()
