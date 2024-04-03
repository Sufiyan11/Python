def change(n,a,b):
    x=int(n/a)
    y=n%a
    if a>=x and b>=y:
        return x,y
    else:
        return -1
    
a=int(input('Enter the available "5 rupee" coin:'))
b=int(input('Enter the available "1 rupee"coin:'))
n=int(input('Enter amount to be made:'))
c=change(n,a,b)
if c==-1:
    print('-1')
else:
    print('"5 rupee"coins needed:',c[0],'   "1 rupee"coins need:',c[1])
