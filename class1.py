a=input()
s=''
for i in range(len(a)):
    if i%2==0:
        s+=a[i].upper()
    else:
        s+=a[i].lower()
print(s)