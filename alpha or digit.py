i=input()
c=ord(i)
if c>=48 and c<=57:
    print('Number')
elif (c>=65 and c<=90) or (c>=97 and c<=122):
    print('Alphabet')
else:
    print('Niether Alphabet nor Number')
