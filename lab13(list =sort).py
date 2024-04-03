list1=[]

print('Enter "$" to stop')
while 1>0:
    a=input('Enter the number:')
    if a=='$':
        break
    else:
        list1.append(a)

print(list1)

a=input('Enter the number to append :')
list1.append(a)
print(list1)

list2=[]
print('Enter the list to add :')
print('Enter "$" to stop')
while 1>0:
    a=input('Enter the number:')
    if a=='$':
        break
    else:
        list2.append(a)
list1.extend(list2)
print('list after addition = ',list1)

a=input('Enter the number to insert :')
p=int(input('Enter the position of insertion:'))
list1.insert(p,a)
print('list1 after the insertion :',list1)

print('Index of',a,'in list1 =',list1.index(a))

list1.sort()
print('list after the sorting: ',list1)
