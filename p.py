
def lp(y):
    if (y%4==0 and y%100!=0)or(y%400==0):
       return y
    else:
        return lp(y+1)

def nxt(ye):
    for i in range(0,15):
        ye+=4
        li.append(ye)

    
y=int(input('Enter a year:'))
ye=lp(y)
li=[ye]
nxt(ye)
print(li)


    
