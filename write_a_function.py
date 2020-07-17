def is_leap(year):
    if year % 400 == 0:
        answer = True
    elif year % 100 == 0:
        answer = False
    elif year % 4 == 0:
        answer = True
    else:
        answer = False
    return answer

year = int(input())
print(is_leap(year))