class MyFraction(math):
    def __init__(self,num=0,den=1):
        self.num=num
        self.den=den
    def fun1(self):
        while(GCD(self.real,self.img)>1):
            x=GCD(self.real,self.img)
            self.real/=x
            self.img/=x
    def __str__(self):
        self.fun1()
        return str(self.num)+'/'+str(self.den)
    def __add__(self,f):
        return MyFraction(self.num*f.den+f.num*self.den,self.den*f.den)
    def __sub__(self,f):
        return MyFraction(self.num*f.den-f.num*self.den,self.den*f.den)
    def __mul__(self,f):
        return MyFraction(self.num*f.num,self.den*f.den)
    def __truediv__(self,f):
        return MyFraction(self.num*f.den,self.den*f.num)
        
f1=input('Enter the 1st fraction: ').split('/')
f1=MyFraction(int(f1[0]),int(f1[1]))
f2=input('Enter the 1st fraction : ').split('/')
f2=MyFraction(int(f2[0]),int(f2[1]))
while True:
    print('''MENU
_____
1.ADD
2.SUB
3.MUL
4.DIV
5.EXIT''')
    ch=input('Enter the choice : ')
    if ch=='1':
        print('f1+f2=',f1+f2)
    elif ch=='2':
        print('f1-f2=',f1-f2)
    elif ch=='3':
        print('f1*f2=',f1*f2)
    elif ch=='4':
        print('f1/f2=',f1/f2)
    else:
        sys.exit(0)

