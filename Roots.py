import math
import cmath
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
d=b*b-4*a*c
if d>0 or d==0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print('Root one is:',r1)
    print('Root two is:',r2)

else:
     r1=(-b+cmath.sqrt(d))/(2*a)
     r2=(-b-cmath.sqrt(d))/(2*a)
     print('Root one is:',r1)
     print('Root two is:',r2)

      
