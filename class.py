f=open("D:/INT108/file.txt","r")
d=f.read()
d=d.split(' ')
for i in d:
    if i==i[::-1]:
        print(i)
print('hello')
f.close()
