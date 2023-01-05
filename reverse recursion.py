def reverse(n,x):
    if  n==0:
        return x
    x=(x*10)+(n%10)
    return reverse(n//10,x)
n=int(input())
x=0
print(reverse(n,x))
