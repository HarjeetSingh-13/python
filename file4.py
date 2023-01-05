f=open("D:/INT108/file.txt","r")
i=0
while True:
    d=f.readline()
    if not d:
        break
    if len(d)>=i:
        print(d[i])
    i+=1
