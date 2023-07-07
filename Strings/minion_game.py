def minion_game(string):
    kevin=0
    stuart=0
    length = len(string)
    for i,c in enumerate(string):
        if string[i] in "AEIOU": kevin += length - i
        else: stuart += length - i
    
    if stuart != kevin:
        if stuart > kevin: print("Stuart",stuart)
        else: print("Kevin",kevin)
    else: print("Draw")

if __name__ == "__main__":
    s = input()
    minion_game(s)
    