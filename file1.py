f=open("D:/INT108/file.txt")
while True:
    s=f.readline()
    if not s:
        break
    print(s)
f.close()
