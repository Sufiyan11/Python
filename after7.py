def fun(list1):
    s=1
    n=len(list1)
    for i in range(0,n):
        if list1[i]==7:
            if i==n-1:
                return -1
            s=1
        else:
            s=s*list1[i]
        i=i+1
    return s
       

list1=[]

print('Enter "-1" to stop')
while 1>0:
    a=int(input('Enter the number:'))
    if a==-1:
        break
    else:
        list1.append(a)

n=len(list1)
s=fun(list1)
print(':.',s)
