m=int(input('Enter no. of columns: '))
n=int(input('Enter no. of rows: '))
a=11
for j in range(0,n):
    for i in range(0,m):
        print(a,end=' ')
        a+=10
    print()
    a=12+j
    
    
