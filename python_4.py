'''l=[]
a=int(input())
x,y,z=1,2,3
for i in range(0,a):  
    l.append([x,y,z])
    x+=3
    y+=3
    z+=3
print(l)


b=[]
for i in range(4):
    b.append(chr(ord('a')+i))
print(b)


n=int(input())
l=[[(1+i+j*3)  for i in range(3)] for j in range(n)]
print(l)


l1=[]
for i in range(0,2):
    a=[]
    for j in range(3):
        b=int(input())
        a.append(b)
    l1.append(a)
l2=[]
for i in range(0,2):
    a=[]
    for j in range(3):
        b=int(input())
        a.append(b)
    l2.append(a)
print(l1)
print(l2)
s=[]
for i in range(0,2):
    a=[]
    b=0
    for j in range(0,3):
        b=l1[i][j] + l2[i][j]
        a.append(b)
    s.append(a)
print(s)


a=[[int(input("")) for i in range(0,3)] for j in range(2)]
b=[[int(input("")) for i in range(0,3)] for j in range(2)]
print(a)
print(b)
c=[[(a[j][i]+b[j][i]) for i in range(0,3)] for j in range(2)]
print(c)'''


a={i:i.upper() for i in 'python'}
print(a)
print(list(a.items()))

    
