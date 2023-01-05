a=['the','sample','create']
a.sort()
print(a)
b=[len(i) for i in a]
b.sort()
c=[]
for i in b:
    for j in a:
        if i==len(j):
            if j not in c:
                c.append(j)
print(c)
