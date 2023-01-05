n=int(input('N: '))
for i in range(1,n+1):
    if i%3==0:
        print(i,'is divisble by 3')
        continue
    print(i,'is not divisble by 3')
