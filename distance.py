x=int(input('value in km '))
y=int(input('value in m '))
v=int(input('Another value in km '))
w=int(input('Another value in m '))
k=x+v+(y+w)//1000
m=(y+w)%1000
print(k,m)
