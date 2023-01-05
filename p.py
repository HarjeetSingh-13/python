a=input()
b=int(input())
if len(a)%b != 0:
    print('Invalid')
else:
    d=[]
    s=0
    for i in range(b,len(a)+1,b):
        e=a[s:i]
        s+=b
        d.append(e)
    x=[]
    for i in d:
        s=''
        for j in i:
            if j not in s:
                s+=j
        x.append(s)
    print(x)
