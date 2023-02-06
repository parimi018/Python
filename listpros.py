import itertools
list1=[]
while 1>0:
    a=input('Enter a number(press ! to stop):')
    if a=='!':
        break
    else:
        list1.append(a)
list1.sort()
print('After sorting the values in the list are:',list1)
print()


b=input('Enter n:')
if b in list1:
    print(b,'is in the list')
else:
    print(b,'is not in the list')
