def Mat_add(a,b):
    c=[[0 for i in range(3)]for j in range(3)]
    for i in range(3):
        for j in range(3):
            c[i][j]=a[i][j]+b[i][j]
    return c

a=[[1,2,3],[3,2,1],[2,3,1]]
b=[[1,3,2],[3,1,2],[2,1,3]]
c=Mat_add(a,b)
for i in range(3):
    print(c[i])
