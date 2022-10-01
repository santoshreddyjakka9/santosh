li=list()

for i in range(10):
    li.append(i)

print('List :',li)

i=0
while i<len(li):
   # li.pop(i) # removes numbers 0,2,4,6,8
#li.pop() # removes whole list
    li.remove(i) # value error
i=i+1

print('Final list:',li)
    

    
