import math
a=[]
def read():
    print('Enter $ to stop:')
    while 1>0:
        b=input('Enter the number:')
        if b=='$':
            break
        else:
            a.append(int(b))
                                                                                         
read()
n=len(a)

def mean():
    s=0
    for i in a:
        s+=i
    return s//n

def variance():
    m=mean()
    v=0
    for i in a:
        v+=(i-m)**2
    return v//n

def SD():
     v=variance()
     return math.sqrt(v)

m=mean()
v=variance()
sd=SD()
print('The mean,variance and Standard deviation of the given list',a,'are',m,',',v,','"%.2f"%sd,'respectively')



    
