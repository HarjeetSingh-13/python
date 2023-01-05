x=int(input())
y=int(input())
a=[]
for i in range(x,y):
    s=0
    for j in str(i):
       s+=int(j)
    if s%2==0:
        a.append(i)
print(a) 