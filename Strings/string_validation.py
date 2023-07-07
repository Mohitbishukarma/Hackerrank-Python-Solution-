if __name__ == '__main__':
    s = input()
    found_status = [0, 0,0 ,0,0]
    for i in s:
        if i.isalnum()and found_status[0]==0:
            found_status[0]=1
        if i.isalpha() and found_status[1]==0:
            found_status[1]=1
        if i.isdigit() and found_status[2]==0:
            found_status[2]=1
        if i.islower() and found_status[3]==0:
            found_status[3]=1
        if i.isupper() and found_status[4]==0:
            found_status[4]=1
    if found_status[0]==0:
        print(False)
    else:
        print(True)
    if found_status[1]==0:
        print(False)
    else:
        print(True)
    if found_status[2]==0:
        print(False)
    else:
        print(True)
    if found_status[3]==0:
        print(False)
    else:
         print(True)
    if found_status[4]==0:
        print(False)
    else:
        print(True)