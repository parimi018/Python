def gcd(x,y):
    if y%x==0:
        return x
    else:
        x=y%x
        y=x
        return gcd(x,y)
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
l=[a,b]
x=min(l)
y=max(l)
g=gcd(x,y)
print('The GCD of',a,'and',b,'is',g)        
            
            
