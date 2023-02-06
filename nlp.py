w=0
d=0
up=0
lc=0
a=input('Enter the sentence:')
while 1>0:
    if a==' ':
        w+=1
    elif a.isdigit():
        d+=1
    elif a.isupper():
        up+=1
    elif a.islower():
        lc=+1
    elif a=='.':
        break
print('The given sentence contains',w,'words',d,'digits',up,'uppercase letters and',lc,'lowercase letters')
