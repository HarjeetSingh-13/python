def btd(s):
    sum=0
    l=len(s)
    for i in range(0,l):
        sum+=(2**i)*int(s[i])
    print(sum)
    return sum

a=list(int(i) for i in input().split(" "))
s=input()
max=s
for i in range(0,a[1]):
    for j in range(0,len(s)):
        k=''
        t=''
        if s[j]=='0':
            k=s[:j]+'0'+s[j+1:]
        if btd(k)>btd(max):
            max=t
    t=s+'0'
    if btd(t)>btd(max):
        max=t
print(max)