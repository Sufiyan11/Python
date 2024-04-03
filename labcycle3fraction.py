class MyFraction():
    def __init__(self,num=0,den=1):
        self.num=num
        self.den=den

    def fun1(self):
        from math import gcd
        while(gcd(self.num,self.den)>1):
            x=gcd(self.num,self.den)
            self.num//=x
            self.den//=x
    def __str__(self):
        self.fun1()
        return str(self.num)+'/'+str(self.den)
    def __add__(self,f):
        return MyFraction(self.num*f.den+f.num*self.den,self.den*f.den)
    def __sub__(self,f):
        return MyFraction(self.num*f.den-f.num*self.den,self.den*f.den)
    def __float__(self):
        return self.num/self.den
        
f1=input('Enter the 1st fraction: ').split('/')
f1=MyFraction(int(f1[0]),int(f1[1]))
f2=input('Enter the 1st fraction : ').split('/')
f2=MyFraction(int(f2[0]),int(f2[1]))
print('f1+f2=',f1+f2)
print('f1-f2=',f1-f2)
print('f1 in decimals : ',float(f1))
print('f2 in decimals : ',float(f12))
