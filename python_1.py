'''def s(x):
    return x**2
l=[1,2,32,4,9]
print(list(map(s,l)))
print(list(filter(lambda x:x>=4,l)))
a=input()
b=input()
print(dict(zip(a.split(','),b.split(','))))
d={'1':'One','2':'Two','3':'Three','4':'Four'}
a=input('Enter key: ')
b=input('Enter Value: ')
c=0
v=0
if a in d.keys():
    print('value of a:',d[a])
else:
    print('not found')
if b in d.values():
    print('key of b:',d.keys(b))
else:
    print('not found')
a={'N':1,'O':2,'Z':3}
b={}
for i in a:
    b[a[i]]=i
print(b)'''
a={'A':100,'B':200,'C':10}
b={'A':30,'C':50,'S':450,'B':70}
c={}
for i in b:
    if i in a:
        c[i]=a[i]+b[i]
    else:
        c[i]=b[i]
print(c)
