file = open("AI.txt","r")

content = file.read()

print(content)

file.close()

with open("student.txt","r") as files:
    content = files.read()

    print(content)