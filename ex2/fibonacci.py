# Print Fibonacci Numbers
import time

def fibonacci(n):
   """Returns n-th Fibonacci number"""
   return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def fibonacciFast(n):
  if n <= 1: return n   # handle 0-th and 1st fibonacci number
  v1 = 1  # 2nd fibonacci number
  v2 = 2  # 3rd fibonacci number
  if n == 2: return v1
  if n == 3: return v2

  # calc 4th or the next fibonacci numbers
  val = 0
  count = 4
  while count <= n:
    val = v1 + v2
    v1 = v2
    v2 = val
    count += 1
  return val


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
