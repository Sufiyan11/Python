def towers_of_hanoi(n,l,r,c):
    if n>0:
        towers_of_hanoi(n-1,l,c,r)
        print('Move disc ',n,'from',l,'to',r)
        towers_of_hanoi(n-1,c,r,l)

n=int(input('Enter the no.of discs :'))
towers_of_hanoi(n,'L','R','C')

def fibonacci(n,a=0,b=1):
    if n==0 or n==1:
        return 1
    c=a+b
    if n==c:
        return 1
    if n>c:
        return fibonacci(n,b,c)

n=int(input('Enter the number :'))
f=fibonacci(n)
if f==1:
    print(n,'is fibonacci number')
else:
    print(n,'is not a fibonacci number')


def fact(n):
    f=1
    if n==1:
        return 1
    else:
        f=n*fact(n-1)
        return f

n=int(input('Enter the number :'))
f=fact(n)
print('Factorial of',n,'is',f)

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(a,a%b)

a=int(input('Enter the number :'))
b=int(input('Enter the number :'))
f=gcd(a,b)
print('GCD of',a,'and',b,'=',f)
