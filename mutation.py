#성공
first = input()
second = input().split()
location = int(second[0])
sub = second[1]

if len(first) <= location:
    print("The number you gave is too large!")
else:
    print(first[:location] + sub + first[location+1:])    