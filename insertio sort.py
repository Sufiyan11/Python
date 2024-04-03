a=list(map(int,input('Enter the List : ').split()))


def Insertion_sort(a):
    for i in range(len(a)):
        k=a[i]
        j=i
        while j>0 and k<a[j-1]:
            a[j]=a[j-1]
            j-=1
        a[j]=k
    return a


def Selection_sort(a):
    for i in range(len(a)):
        m=i
        for j in range(i,len(a)):
            if a[m]>a[j]:
                m=j
        a[i],a[m]=a[m],a[i]
    return a


'''def binary_search(a,l,h,k):
    if l<=h:
        m=(l+h)//2
        if a[m]==k:
            return m
        if a[m]>k:
            return binary_search(a,l,m-1,k)
        return binary_search(a,m+1,h,k)
    return -1

a=Selection_sort(a)
c=binary_search(a,0,len(a),int(input('Enter the Key : ')))
print('The index :',c)'''
    


def Merge(a,b):
    i,j,c=0,0,[]
    while i<len(a) and j< len(b):
        if a[i]>b[j]:
            c.append(b[j])
            j+=1
        elif a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(a[i])
            i+=1
            j+=1

    while i<len(a):
        c.append(a[i])
        i+=1
    while j<len(b):
        c.append(b[j])
        j+=1
    return c


b=list(map(int,input('Enter the List : ').split()))
a=Selection_sort(a)
b=Insertion_sort(b)
print('List after Merging of given sorted lista : ',Merge(a,b))
































