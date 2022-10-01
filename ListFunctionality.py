li=[10,20,30,20]
print(li)
li.append(50) # will add 50 to array
print(li)
li.insert(2,70) # will add 70 after index 2
print(li)
li.insert(10,100) # will add 100 to array at last 
print(li)
li.pop() # removes last element
print(li)
li.pop(3)
print(li)# removes index 3 element from array
li.remove(50) # removes  element 50 from array
print(li)
li.remove(20) # removes  first occurenece if element is duplicate
print(li)
li.clear()# clears all elements in array and dispalys empty array
print(li)
del li
print(li) # displays error message that li is not defined
