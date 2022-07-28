f = open("another.text","a") # w will create new file and .write will add line in that file
text = f.write("i am appending")  # a will append that line in that file 
f.close()