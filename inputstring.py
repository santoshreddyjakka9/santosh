
fo = open("foo.txt", "r+")
str=input("Enter your input")
print("string is",str)
fo.write(str)

str = fo.read(10);
print ("Read String is : ", str)


fo.close()
import os
os.rename("foo.txt","Too.txt")



