# Data Type: String

print(f"Filling, Adjustment, Alignment: {10:$>5}")
for x in range(1, 20, 5):
    print(f'{x:>3} * {x:>3} = {x*x:0>5}')
print()


print("Using zfill:")
# text formatting
for x in range(1, 20, 5):
    print(f'{x:>3} * {x:0>3} = {str(x*x).zfill(3):^10}')
print()


# printing characters
print(" ".join(chr(i) for i in list(range(32, 127))))
