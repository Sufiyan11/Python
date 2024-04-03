def sumn(n):
    s=0
    while n>0:
        x=n%10
        s+=x
        n=n//10
    print(s)
    return s
def MyLPN(l):
    s=0
    for i in range(3):
        m=list(l[i])
        print(m)
        m=[int(x) for x in m]
        s+=sum(m)
    print(s)
    ch=sumn(s)
    print(ch)
    d={1: 'Independent'  ,2: 'Introvert'  ,3: 'Helpful' , 4: 'Practical' ,5: 'Extrovert',6:'Responsible' ,7:'Pious',  8: 'Ambitious',  9: 'Leader'}
    if ch in d:
        print(ch,d[ch])
l=input('dd/mm/yyyy :').split('/')
print(l)
MyLPN(l)
