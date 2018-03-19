def num_islands(num):
    print(num)


    islands_num = 0
    size_matrix_x = len(num[0])
    size_matrix_y = len(num)
    for idx_y in range (0,size_matrix_y):
        for idx_x  in range (0,size_matrix_x):
            if(num[idx_y][idx_x] == 1):
                islands_num = islands_num+1
                clean_island(num,idx_x,idx_y,size_matrix_x,size_matrix_y)
                print(num)
    print(islands_num)



def clean_island(num,idx_x,idx_y,size_matrix_x,size_matrix_y):
    if (idx_x != 0) and ( (idx_x%size_matrix_x == 0) or (idx_x<0) ):
        return
    if (idx_y != 0) and ((idx_y%size_matrix_y == 0) or (idx_y<0) ):
        return

    if(num[idx_y][idx_x]==0):
        return
    #num[idx_y][idx_x] is equal 1 -> clean
    num[idx_y][idx_x] = 0
    clean_island(num,idx_x+1,idx_y,size_matrix_x,size_matrix_y)
    clean_island(num, idx_x-1, idx_y,size_matrix_x,size_matrix_y)
    clean_island(num, idx_x, idx_y+1,size_matrix_x,size_matrix_y)
    clean_island(num, idx_x, idx_y -1 ,size_matrix_x,size_matrix_y)


mat = [[0,0,0,1,0],[0,1,0,0,1],[0,1,1,0,1]]
num_islands(mat)