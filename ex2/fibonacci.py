# Print Fibonacci Numbers
import time

def fibonacci(n):
   """Returns n-th Fibonacci number"""
   return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def fibonacciFast(n):
  if n <= 1: return n     # handle 0-th and 1st fibonacci number: 0, 1
  if n <= 3: return n-1   # 2nd and 3rd fibonacci number: 1, 2

  # calc 4th and the next fibonacci numbers
  index, v1, v2 = 4, 1, 2
  while index <= n:
    v1,v2 = v2, v1+v2
    index += 1
  return v2

if __name__ == "__main__":
  maxCount = 22
  print("Fibonacci sequence:")
  tm1 = time.time()
  for count in range(maxCount):
    print(fibonacci(count))
  tm2 = time.time()
  print('\nTotal time elapsed: {}'.format(tm2-tm1))

  print('')

  print("Fibonacci sequence(Fast):")
  tm1 = time.time()
  for count in range(maxCount):
    print(fibonacciFast(count))
  tm2 = time.time()
  print('\nTotal time elapsed: {}'.format(tm2-tm1))
