

def comp(num):
    if num%2 == 1: # Odd
        return num*3 + 1
    else:
        return num // 2
    

length = 0
biggest = 0
for x in range(1, 2000000):
    num = [x]
    while num[-1] != 1: #last num isn't 1
        num.append(comp(num[-1]))
        if len(num) > length:
            length = len(num)
            biggest = num
print("Longest sequence starts with {} and has a length of {}.".format(biggest[0], length))
print("Sequence : ")
print(biggest)
