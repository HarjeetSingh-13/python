def btd(s):
    su=0
    l=len(s)
    for i in range(0,l):
        su+=(2**i)*int(s[-(i+1)])
    return su

a=list(int(i) for i in input().split(" "))
s=input()
m=s
for i in range(0,a[1]):
    for j in range(0,len(s)):
        k=''
        t=''
        if s[j]=='0':
            k=s[:j]+'1'+s[j+1:]
        if btd(k)>btd(m):
            m=k
    t=s+'0'
    if btd(t)>btd(m):      
        m=t
    s=m
print(m)
