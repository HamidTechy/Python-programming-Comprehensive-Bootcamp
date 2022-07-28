def fahreheit(cel):
    return cel * (9/5) + 32


c = int(input("enter cel: "))
f = fahreheit(c)
print(f)