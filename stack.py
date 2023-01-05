id = [1,2,3]
text = [['a'], ['b'], ['c']]
b=[]
for i in zip(id,text):
    b.append({'ID':i[0],'TEXT':i[1]})
print(b)