if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    x_i=[i for i in range(x+1)]
    y_j=[i for i in range(y+1)]
    z_k=[i for i in range(z+1)]
    
    all_i_j_k=[]
    for i in x_i:
        for j in y_j:
            for k in z_k:
                all_i_j_k.append(list([i,j,k]))
    result=[coordinate for coordinate in all_i_j_k if coordinate[0]+coordinate[1]+coordinate[2] !=n]
    
    print(result)