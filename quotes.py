f=open("fun.txt","r")
l=[]
for i in f:
    l.append(str(i))

for i in f:
    c=f.count(i)
    if i not in l:
        l.append(i)
        l.append('=')
        l.append(c)

for i in l:
    c=0
    print(i)
    if c//3==0:
        print()
        
