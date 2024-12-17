#  open("file name", "Permission")
import json
name = input("Enter your name : ")
phone = int(input("Enter yoour phone number :"))
d1 = {}
d1.update({name:phone})
s = json.dumps(d1)

file = open("./LearnVern/Assignment/gyan.txt","a")

file.write(s)
file.seek(0)
print("File is created")
file.close()



