s = str(input())
lower = list()
upper = list()
odd = list()
even = list()

for i in s:
    if(i.islower()):
        lower.append(ord(i))
    elif(i.isupper()):
        upper.append(ord(i))
    else:
        if(int(i) % 2 == 1):
            odd.append(ord(i))
        else:
            even.append(ord(i))

lower.sort()
upper.sort()
odd.sort()
even.sort()
final = lower + upper + odd + even

for i in final:
    print(chr(i), end="")