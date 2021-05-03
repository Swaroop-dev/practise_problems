def maximun_squares(matrix=[["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]):
    row_len=len(matrix)
    col_len=len(matrix[0])
    result=[[0 for i in range(col_len)] for i in range(row_len)]
    for i in range(row_len):
        result[i][0]=int(matrix[i][0])
    for j in range(col_len):
         result[0][j]=int(matrix[0][j])
    for i in range(1,row_len):
        for j in range(1,col_len):
            if matrix[i][j]=="0":
                result[i][j]=0
            else:    
                result[i][j]=min(result[i-1][j-1],result[i-1][j],result[i][j-1])+1
    print(max(result))        
    output1=[max(result[i]) for i in range(row_len)]
    output=max(output1)
    if output<=1:
        return output
    return output**2
print(maximun_squares())