li=list()

# reading input from user and appends in list when we dont know how large our list is

print('enter elements press 0 to stop:')
while True:
    ele = int(input())
    if ele==0:
        break
    else:
        li.append(ele)
print('list is',li)
    
    
