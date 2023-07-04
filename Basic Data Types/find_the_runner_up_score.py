if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr_l=[x for x in arr]
    arr_l.sort()
    ind_list=[]
    for ind in arr_l:
        ind_arr=arr_l.index(ind)
        if ind_arr not in ind_list:
            ind_list.append(ind_arr)
    print(arr_l[ind_list[-2]])    
        