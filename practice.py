n=input('Enter the names into the list').split()
c=0
co=0
for i in n:
    if 'at' in i:
        c+=1
        for i in range(3):
            if int(i[2])=='t':
                co+=1
print('_at--->',c,'%at%--->',co)
    
