a=input()
for i in range(len(a)):
    if a[i]=='1':
        for j in range(i,len(a)):
            if a[j]=='1':
                print(a[i:j+1])