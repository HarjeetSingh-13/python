import re
mystr='This    is         sample  string 123'
print(re.findall('[a-z2]+',mystr))
a=re.search("\s",mystr)
print(a.start())
print(re.findall('[ ]+',mystr))