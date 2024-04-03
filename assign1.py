import itertools
def mylist(l):
    d={}
    for i in l:
        if len(i)%2==0:
            m=i[0:len(i)//2]
            n=i[len(i)//2:]
        else:
            m=i[0:len(i)//2]
            n=i[len(i)//2+1:]
        k=list(itertools.permutations(m))
        for j in range(len(k)):
            k[j]=''.join(k[j])
        if n in k:
            d[i]='isLapindrome'
        else:
            d[i]='isNotLapindrome'
    for i in l:
        print(i,d[i])
        
            
l=input().split()
mylist(l)
