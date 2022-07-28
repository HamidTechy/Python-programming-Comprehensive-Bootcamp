def remvoe_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()


this = "      this is a good code    "
f = remvoe_and_split(this, "this")
print(f)