import sys
type1 = sys.argv[1]
if type1 == "t2.micro":
    print("ok")
else:
    pirnt("Not Ok")

adt = ("sai","mani")
adl = [20,9]
print(type(adt))
print(type(adl))
print(adt)
print(adl)
adl.append(8)
print(adl)

subset = adl[0:1]
print(subset)
newList = adl.append(6)
print(newList)
print(adl)
present = "saik" in adl
print(present)
s=adl.sort()
print(s)

