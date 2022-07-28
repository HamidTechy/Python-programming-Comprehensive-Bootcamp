f = open("10_sample.txt")
text = f.readline() #this readline method print first line of paragraph
# if we want to print next we should reuse readline method
print(text)
text = f.readline()
print(text)
text = f.readline()
print(text)
f.close() # close() IS used to close the program that other programs should work on that file
