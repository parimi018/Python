def fact(n):
    if n==0 or n==1:
        return n
    return n*fact(n-1)
n=int(input('Enter n:'))
f=fact(n)
print(f,'is the factorial of',n)
