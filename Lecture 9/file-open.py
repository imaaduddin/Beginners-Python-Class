# File opening

f = open("demofile.txt", "a")


# Writing in file
f.write('\n I live in Houston.')
f.close()

f = open("demofile.txt", "r")
print(f.read())