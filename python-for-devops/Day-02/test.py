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