try:
    a=int(input())
    b=int(input())
    c=a/b
    print('try successful')
except ZeroDivisionError:
    print('divide by zero error')