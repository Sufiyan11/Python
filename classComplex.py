class Complex:
    from math import sqrt
    def __init__(self,r=0.0,i=0.0):
        self.real=r                                                                                                    
        self.img=i
    def __str__(self):
        if self.img<0:
            return str("%.2f"%self.real)+str("%.2f"%self.img)+'j'
        else:
            return str(self.real)+'+'+str(self.img)+'j'
    def __add__(self,c):
        return Complex(self.real+c.real,self.img+c.img)
    def __sub__(self,c):
            return Complex(self.real-c.real,self.img-c.img)
    def __mul__(self,c):
            return Complex(self.real*c.real+self.img*c.img,self.real*c.img+self.img*c.real)
    def __truediv__(self,c):
        d=c.real*c.real-c.img*c.img
        return Complex((self.real*c.real+self.img*(-1)*c.img)/d,(self.img*c.real+self.real*(-1)*c.img)/d)
    def mod(self):
        return sqrt(self.real**2+self**2)

c1=input('Enter the 1st complex number : ').split()
c1=Complex(int(c1[0]),int(c1[1]))
c2=input('Enter the 2nd complex number : ').split()
c2=Complex(int(c2[0]),int(c2[1]))
while True:
    print('''MENU
1.ADD
2.SUB
3.MUL
4.DIV
5.EXIT''')
    ch=input('Enter the choice : ')
    if ch=='1':
        print('c1+c2=',c1+c2)
    elif ch=='2':
        print('c1-c2=',c1-c2)
    elif ch=='3':
        print('c1*c2=',c1*c2)
    elif ch=='4':
        print('c1/c2=',c1/c2)
    else:
        sys.exit(0)
