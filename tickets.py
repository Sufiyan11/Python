def ticket_price(a,b):
    pri=37550
    adult=(pri+pri*0.07)*0.9*a
    child=((pri/3)+(pri/3)*0.07)*0.9*b
    return adult+child

print('Enter the number of tickets')
a=int(input('Adults:'))
b=int(input('Children:'))
c=ticket_price(a,b)
print('Total ticket price=',c)
