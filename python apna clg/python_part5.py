f = open("a.txt", "r")  # filename, mode - read,write

print(f.read())
print(type(f.read()))
print(f.readline())

f.close()