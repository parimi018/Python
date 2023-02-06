class Complex:
    def __init__(self,r=0,i=0):
        self.real=r
        self.img=i
    def __str__(self):
        if self.img>=0:
            return str(self.real)+'+'+str(self.img)+'j'
        else:
            return str(self.real)+'-'+str(self.img)+'j'
    def __add__(self,c):
        return Complex(self.real+c.real,self.img+c.img)
    def __sub__(self,c):
        return Complex(self.real-c.real,self.img-c.img)
    def __mul__(self,c):
        r = (self.real * c.real) - (self.img * c.img)
        i = (self.real * c.img) + (self.img * c.real)
        return Complex(r, i)
    def __truediv__(self,c):
        r= ((self.real * c.real) + (self.img * c.img))/((c.real**2)+(c.img**2))
        i=((self.real * c.img) + (self.img * c.real))/((c.real**2)+(c.img**2))
        return Complex(r,i)


c1=input('Enter 1st complex number').split()
c1=Complex(int(c1[0]),int(c1[1]))
c2=input('Enter 2nd complex number').split()
c2=Complex(int(c2[0]),int(c2[1]))
print('''MENU
1.ADD
2.SUBTRACT
3.MULTIPLICATION
4.TRUE DIVISION
5.FLOOR DIVISION
6.QUIT''')
while True:
    ch=(input('Enter your choice:'))
    if ch=='1':
        print(c1+c2)
    elif ch=='2':
        print(c1-c2)
    elif ch=='3':
        print(c1*c2)
    elif ch=='4':
        print(c1/c2)
    elif ch=='5':
        print(c1//c2)
    else:
        sys.exit(0)
