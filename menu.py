
def isPrime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print(n,'is Prime')
    else:
        print(n,'is not prime')
        
def isArmstrong(n):
    c=0
    m=n
    while n!=0:
        n=n//10
        c=c+1
    n=m
    s=0
    while n!=0:
        r=n%10
        s=s+r**c
        n=n//10
    if s==m:
        print(m,'is Armstrong')
    else:
        print(m,'is not Armstrong')

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def isStrong(n):
     m=n
     s=0
     while n!=0:
         r=n%10
         s=s+fact(r)
         n=n//10
     if s==m:
        print(m,'is Strong')
     else:
        print(m,'is not Strong')
    
def isPerfect(n):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s=s+i
    if s==n:
        print(n,'is Perfect')
    else:
        print(n,'is not perfect')
        
n=int(input('Enter a number'))    
q=1
while q!=0:
    print('~~~MENU~~~')
    print('''1.Prime 
2.Armstrong
3.Strong
4.Perfect
5.Quit'''
          )
    c=int(input('Enter your choice'))
    if c==1:
        isPrime(n)
    elif c==2:
        isArmstrong(n)
    elif c==3:
        isStrong(n)
    elif c==4:
        isPerfect(n)
    else:
        q=0
        
    
        
    
    
    
     
    
