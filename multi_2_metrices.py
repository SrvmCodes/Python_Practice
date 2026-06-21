A = [[1,2,3],
     [2,3,4],
     [3,5,4]]
B = [[3,4,5,7],
     [2,3,4,5],
     [6,7,8,6]]
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
for i in result:
    print(i) 
