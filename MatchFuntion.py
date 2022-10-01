import re
line = "Java and Python are prg lanugages"
found=re.match(r'Java',line)
if found:
    print('matchfound',found)
else:
    print('not found')
