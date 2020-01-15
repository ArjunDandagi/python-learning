def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        increase_by = len(string)-i
        if string[i] in vowels:
            kevin+=increase_by
        else:
            stuart+=increase_by
    if stuart == kevin:
        print("Draw")
        return 
    print("Stuart "+str(stuart) if stuart>kevin else "Kevin "+str(kevin))
if __name__ == '__main__':
    s = input()
    minion_game(s)
