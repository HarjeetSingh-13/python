a={1:'one',2:'one'}
b=a.keys()
c=a.values()
z='y'
if list(c)!=list(set(c)):
    print('values are repeating')
    z=input('do you still want to print (y/n): ')
if z=='y' or z=='Y':
    print(dict(zip(c,b)))
elif z=='n' or z=='N':
    print('whatever you want...')
else:
    print('Invalid input')