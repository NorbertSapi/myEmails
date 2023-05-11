
x = open("Hello.txt", "r")
y = x.read()
print(y)
x.close()

with open("Hello.txt", "w") as file:
    file.write("Hey there!")
