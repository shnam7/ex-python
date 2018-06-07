# inut/output

import sys

print('Welcome to', 'Python', sep='...', end='\n\n', file=sys.stderr)

# file writing
#file1 = open('test.txt', 'w')
#print('data...', file=file1)
#file1.close()

# text formatting
for x in range(1, 20, 5):
  print('{} * {} = {}'.format(str(x).rjust(3), str(x).zfill(3), str(x*x).zfill(3).center(10)))

item1 = { "name": "apple", "color": "red" }
item2 = { "name": "melon", "color": "green" }
print("{0[name]} is {0[color]}, {1[name]} is {1[color]}".format(item1, item2))
print("{name} is {color}".format(**item1))

# type conversion: !a equals ascii(), !r equals repr(), !s equals str()
print("Type conversion with '!': {1!a} {2!s} {0}".format('하나abcde', item1, item2))

# fill with $, right justment(>), width 5
print("Filling, Adjustment, Alignment: {0:$>5}".format(10))
for x in range(1,20, 5):
  print('{:>3} * {:>3} = {:0>5}'.format(x, x, x*x))

# '=' means show sign before spaces
print("Using '=': {:5} and {:5} vs. {:=5} and {:=5}".format(10, -10, 10, -10))

# '+' means show signs, '-' means show signs only for the minus numbers
print("Using '+' and '-': {:+5} and {:+5} vs {:-5} and {:-5}".format(10, -10, 10, -10))

# convert list to string, fill with $,*,~, align left,center,right
ar = list(range(3))
print('{!s:$<15} {!s:*^15} {!s:~>15}'.format(ar,ar,ar))

# number notations: number base systems
print("decimal:{} binary:{:b} octal:{:o} hexa:{:x} ascii:{:c}".format(65,65,65,65,65))

# number notations: floatig point numbers
num = 3.14159
print("floating:{:.2} exponential:{:e} percentage:{:.3%}".format(num, num, num))

print("----------")
# input
msg = input('Enter your input:')
print('You entered "{}"'.format(msg))