def count_substring(string, sub_string):
    sbtrs=[]
    for i in range(len(string)):
        x=len(string)
        for i in range(x):
            sbtrs.append(string[0:x])
            x-=1
        string = string.replace(string[0],'',1)
    return sbtrs.count(sub_string)
