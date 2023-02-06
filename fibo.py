a,b=0,1
def fibo(n,a=0,b=1):
    if n==0 or n==1:
        return True 
    s=a+b
    if n==s:
        return True
    if n>s:
        return fibo(n,b,s)
n=int(input('Enter n:'))
if fibo(n):
    print(n,'is a Fibonacci Number')
else:
    print(n,'is not a Fibonacci Number')
    
