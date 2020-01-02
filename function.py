def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0: 
            leap = False 
        if year % 400 == 0:
            leap = True
    return leap 
    # well this can be written in one line too 
    # return year % 4 == 0 and ( year % 400 == 0 or year % 100 != 0 ) 



year = int(input())
print(is_leap(year))
