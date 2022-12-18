# Hello

print("Hi, there!")

name = 'Tom'
id = 12345
print("Hi, My name is {}, and ID is {}".format(name, id))
print()

# f-string
val = 123
print(f"val is |{val:<10}|")    # left adjustment
print(f"val is |{val:>10}|")    # right adjustment
print(f"val is |{val:^10}|")    # center adjustment
print(f"val is {{{val:^10}}}")    # print brace character {{ }}
print()

# input
inStr = input("Please enter anything: ").split()
print('You entered {}'.format(inStr))
