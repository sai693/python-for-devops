import re
arn = "arn:aws:iam::12345678912:user/saikumar"
print (arn.split("/")[1])

a = (arn.split("/")[1])
print (a.upper())
b = "Gurugubelli"
print (a.upper() + " " + b.upper())
text = "its match the quick pattern"
pattern = r"its match the quick pattern"
match = re.match(pattern, text)
if match:
    print("match found", match.group())
else:
    print("Not Found")

print (text," ", len(text))
print(" ",text.upper())

text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

a = 15
b = 5

def add():
    c = a+b
    print(c)

def sub():
    d = a-b
    print(d)

add()
sub()
