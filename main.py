
"""
x = open("Hello.txt", "r")
y = x.read()
print(y)
x.close()

with open("Hello.txt", "w") as file:
    file.write("Hey there!")
"""

with open("Names.txt", "r") as nameFile:
    with open("Message.txt", "r") as messageFile:
        body = messageFile.read()
        for name in nameFile:
            mail = "Hello " + name + body
            with open(name.strip() + ".txt", 'w') as messageFile:
                messageFile.write(mail)

print("All done, Message created and ready, take a look in your directory.")
print("--------------------------------------------------------------------------------------------------")
print("Here is an example of the message created\n")

print("----------------Message to Dave----------------")
with open("Dave.txt", "r") as dave:
    print(dave.read() + "\n")

print("----------------Message to Terry----------------")
with open("Terry.txt", "r") as terry:
    print(terry.read())
