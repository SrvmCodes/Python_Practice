A = [[1,3,5],
     [3,7,9],
     [2,5,7]]
B = [[1,4,8],
     [3,9,2],
     [7,3,8]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j]+B[i][j]

for r in result:
    print(r)