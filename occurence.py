a=[int(s) for s in input().split(' ')]
s2=0
s3=0
s5=0
s7=0
for i in a:
    if i%2==0:
        s2+=1
    if i%3==0:
        s3+=1
    if i%5==0:
        s5+=1
    if i%7==0:
        s7+=1
d={'2':s2,'3':s3,'5':s5,'7':s7}
print(d)