n=int(input('N: '))
j=0
for i in range(1,n):
    if n%i==0:
        j+=1
        break
if j==2 or n==1:
    print('N is not prime')
else:
    print('N is prime')
