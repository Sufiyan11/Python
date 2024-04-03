def josephs(n,k):
    l=list(range(1,n+1))
    c=0
    while len(l)>1:
        
        l=l[k-1:]+l[:k-1]
    print(l[0])

        
n,k=map(int,input('Enter number of people in circle and value of order of assasination:').split())
josephs(n,k)
