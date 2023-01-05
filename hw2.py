x=int(input('Enter any no.:'))
y=x-1
a=0
for i in range(0,x):
    for j in range(0,x):
        if j==a or j==y:
            print('k',end=' ')
        else:
            print(' ',end=' ')
    print()
    a+=1
    y-=1
    
