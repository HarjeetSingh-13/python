import re
a=' abc@gmail.com, xy@gmail.com,hello there how are you,hey welcome.'
print(re.findall("\s[a-z]+@[a-z]+.[a-z]+,",a))