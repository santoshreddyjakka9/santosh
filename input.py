

fo = open("foo.txt", "a+",)
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)

#print ("Softspace flag : ", fo.softspace)

str=input("Enter your input")

print("string is",str)
fo.write(str)



fo.close()  


