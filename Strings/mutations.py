def mutate_string(string, position, character):
    charList=list(string)
    charList[position]=character
    modifiedStr="".join(charList)
    return modifiedStr
