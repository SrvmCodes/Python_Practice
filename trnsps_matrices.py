# # Solution using For loop 
# A = [[2,3,6],
#      [4,3,2]]
# T = [[0,0],
#      [0,0],
#      [0,0]]

# for i in range (len(A)):
#     for j in range(len(A[0])):
#         T[j][i] = A[i][j]

# for i in T:
#     print(i)


# Solution using List Comprehenshion

A = [[2,3,6],
      [4,3,2]]
T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
for i in T:
    print(i)
         



