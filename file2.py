f1=open("D:/INT108/file.txt","r")
f2=open("D:/INT108/file1.txt","w+")
data=f1.read()
for i in data:
    if i.isalpha():
        f2.write(i)
f2.seek(0)
print(f2.read())
f1.close()
f2.close()
