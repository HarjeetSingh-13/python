'''def display():
    print('KOC23')
    print('1st Nov')
display()
print('End of line')
def sum():
    a=int(input())
    b=int(input())
    print(a+b)
sum()
def sum2(a,b):
    print(a+b)
recarea=56
triarea=98
sum2(recarea,triarea)
c=int(input())
d=int(input())
sum(c,d)
def chr(c,n):
    print(c*n)
c=input()
n=int(input())
chr(c,n)'''
'''def gcd(x, y):
 
    if x > y:
        a = y
    else:
        a = x
    for i in range(1, a + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    print(gcd)
             
a=int(input())
b=int(input())
gcd(a,b)'''
def area(x,y,z):
    if z==1:
        print('area of rectangle=',x*y)
    elif z==2:
        print('area of triangle=',0.5*x*y)
    else:
        print('invalid input')
x=int(input())
y=int(input())
z=int(input())
area(x,y,z)
