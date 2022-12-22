num_1 = int(input("Number One:    "))
num_2 = int(input("Number Two:    "))

### converting numbers to binary ###
num_1 = str(bin(num_1))
num_2 = str(bin(num_2))

num_1 = num_1[2:]
num_2 = num_2[2:]


### making numbers the same size adn adding extra place value
inputs_1 = [int(digit) for digit in str(num_1)]
inputs_2 = [int(digit) for digit in str(num_2)]

while len(inputs_1)!= len(inputs_2):
    if len(inputs_1) > len(inputs_2):
        inputs_2.insert(0, 0)
    else:
        inputs_1.insert(0,0)
inputs_1.insert(0,0)
inputs_2.insert(0, 0)


###### making gates as functions ###

def AND(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def XOR (a, b):
    if a != b:
        return 1
    else:
        return 0

### main function ###
ans  = []
count = 0
carry = 0

for x in inputs_1:
    count -= 1
    a = inputs_1[count]
    b = inputs_2[count]
    result1 = XOR(a,b)
    result = XOR(carry, result1)
    ans.insert(0, result)
    carry1 = AND(a,b)
    carry2 = AND(carry, result1)
    carry = XOR(carry1, carry2)


print(inputs_1)
print(inputs_2)
print(ans)
