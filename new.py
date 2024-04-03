n=int(input())
m=n
s=''
if n%2==0:
    m=n
t=n//2
for i in range(t):
    s+=' '
for i in range(n):
    for j in range((n-i)-1):
        print(' ',end='')
    for k in range(i*2+1):
        print('H',end='')
    print()
for i in range(n+1):
    print(s,end='')
    for j in range(n):
        print('H',end='')
    for k in range(n):
        print('   ',end='')
    for l in range(n):
        print('H',end='')
    print()
for i in range((n//2)+1):
    print(s,end='')
    for j in range(5):
        for k in range(n):
            print('H',end='')
    print()
for i in range(n+1):
    print(s,end='')
    for j in range(n):
        print('H',end='')
    for k in range(n):
        print('   ',end='')
    for l in range(n):
        print('H',end='')
    print()
for i in range(n):
    for j in range(n*4):
        print(' ',end='')
    for l in range(i):
        print(' ',end='')
    for k in range((n-i)*2-1):
        print('H',end='')
    print()
