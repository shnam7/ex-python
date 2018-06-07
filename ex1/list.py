#

# enumerate
aList = ['Apple', 'Mango', 'Pineapple']
for i,name in enumerate(aList, 100):
  print(i, '=', name)

# List comprehension
list1 = list(range(10, 20))
list2 = [i**2 for i in list1 if 15<= i <=17]
list3 = [x*y for x in list1 if x<13 for y in list2]
print(list1, list2, list3)

# filter
list4 = list(filter(lambda x: x>3000, list3))
print("filtered =", list4)

# map
list4 = list(map(lambda x,y: x+y, list2, list3))
print("mapped =", list4)

# zip: returns combined tuples
list5 = list(zip(list1, list2, list3))
print("zippd =", list5)

# print using jping
print('\n'.join(map(lambda x: str(x), list5[0])))