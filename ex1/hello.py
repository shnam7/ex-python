print("Hi, there!")

name = 'Tom'
id = 12345
print("Hi, My name is {}, and ID is {}".format(name, id))

inStr = input("Please enter anything: ").split()
print('You entered {}'.format(inStr))

# printing characters
print("".join(chr(i) for i in list(range(32, 127))))
