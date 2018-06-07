#

# string and numbers
aStr = "String"
aNum = 123 / 2
print(aStr, aStr[::-1], aStr[1:3], aNum)

# list
aList = [1,2,3, "hello"]
aListInversed = aList[::-1]
print(aList, aListInversed)

ar = list(range(10))  # 0~9
print(ar[2:5], ar[::3], ar[::-1], 5 in ar, 10 in ar)

list2 = aList
print("id(aList)=", id(aList), "id(list2)=", id(list2)) # aList and list2 are the same object
list2 = aList[:] # copy all
print("id(aList)=", id(aList), "id(list2)=", id(list2)) # now aList and list2 are not the same

# dict
person1 = {
  "name"  : "Jun",
  "age"   : 19,
  "born"  : "Seoul"
}
person2 = dict(name="Marvin", age=60, born="US")

for key, val in person1.items():
  print("{} = {}".format(key, val))

print(person2, person2["name"])

for key in person1.keys():
  print("key=", key)

for val in person2.values():
  print("val=", val)
