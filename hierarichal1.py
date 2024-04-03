class grandparent():
    def __init__(self,m=0,n=0):
        self.prop=m
        self.kids=n
    def display(self):
        print('Grand Parent Property :',self.prop,'\tKids=',self.kids)
    def perKid(self):
        return float(self.prop/self.kids)
class parent(grandparent):
    def __init__(self,yp=0,yk=0,pp=0,pk=0):
        super().__init__(pp,pk)
        self.prop1=yp+self.perKid()
        self.kids1=yk
    def display(self):
        super().display()
        print('Parent property :',self.prop1,'\tKids :',self.kids1)
    def perkid(self):
        return float(self.prop1/self.kids1)
class you(parent):
    def __init__(self,kp=0,kk=0,yp=0,yk=0,pp=0,pk=0):
        super().__init__(yp,yk,pp,pk)
        self.prop2=kp+self.perkid()
        self.kids2=kk
    def display(self):
        super().display()
        print('My Property:',"%.2f"%self.prop2,'\tKids :',self.kids2)


y=you(1500000,2,200000,3,100000,4)
y.display()
