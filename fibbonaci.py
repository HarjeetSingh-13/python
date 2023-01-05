x=int(input('x: '))
x-=1
a=s=i=0
b=1
if x>=0:
    print(a)
if x>=1:
    print(b)
while x>b:
        c=a+b
        print(c)
        a=b
        b=c
        if (i%2)==0:
            s=s+c
        i+=1
print('sum:',s)
    
    
    
    
