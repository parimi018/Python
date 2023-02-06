def towers_of_hanoi(n,l,r,c):
    if n>0:
        towers_of_hanoi(n-1,l,c,r)
        print('Move disc',n,' from',l,'to',r)
        towers_of_hanoi(n-1,c,r,l)

n=int(input('Enter n:'))
towers_of_hanoi(n,'L','R','C')
    
    
    
