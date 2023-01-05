def cel(a,b):
    if b==0:
        return 1
    elif a==0:
        return 2*cel(a-1,(2*b)//3)
print(cel(0,0))
print(cel(1,0))
print(cel(0,1))
print(cel(2,3))
