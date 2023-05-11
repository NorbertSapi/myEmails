
"""
x = open("Hello.txt", "r")
y = x.read()
print(y)
x.close()

with open("Hello.txt", "w") as file:
    file.write("Hey there!")
"""

with open("Names.txt", "r") as name_file:
    with open("README.txt", "r") as message_file:
        body = message_file.read()
        for name in name_file:

            mail = "Hello " + name + body
            with open(name.strip() + ".txt", + ".txt", 'w') as message_file:
                message_file(mail)
