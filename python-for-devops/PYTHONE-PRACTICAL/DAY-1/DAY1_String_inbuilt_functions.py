print ("\n MODULES USED \n DAY1_DataTypes.py\n")
import DAY1_DataTypes as basic_cal
print ("\nDAY1_Regular_expression.py\n")
import DAY1_Regular_expression as basic_regx

basic_cal.addition()
basic_cal.subtraction()

basic_regx
print("Hello, World!")
x = 5
print(x)
arn = "arn:aws:iam::123456789012:user/johndoe"

#  spliting inbuilt functions
a = (arn.split("/") [0])
ab = (arn.split("/") [1])
print(a)
print(ab)

# Uppercase Inbuilt functions
name = "sai kumar gurugubelli"
print(name.upper())


# string concat
firstname = "sai kumar"
lastname = "gurugubelli"
print(firstname + " " + lastname)

# string length inbuilt function
fl=len(firstname)
ll=len(lastname)
print("Firstname = " + firstname + " \nLENGTH = "+ str(fl))
print("\nLastname = " + lastname + "\nLENGTH = " + str(ll))

# string upper to lower case
print("\n UPPER CASE LETTER TO LOWER CASE \n")
print(name.upper() + " ==> " + name.lower())

# string replace GURUGUBELLI to G
re = name.lower()
rep1 = str(re)
print("string replace gurugubelli to G")
rep = rep1.replace("gurugubelli", "G")
print("Modefied text: ",rep)

text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

# string stripped inbuilt fuction
stripped_name = "                   Gurugubelli Sai kumar"
print("BEFORE without stripped inbuilt function used\n" + stripped_name)

print("After stripped inbuilt function used  " + "\n" + stripped_name.strip())


# String substring in the text

text = "Python is saikumar awesome"
substring = "saikumar"
if substring in text:
    print(substring, "found in the text")
else:
    print("not found")
 
    
# Float variables
num1 = 157.0
num2 = 2.0

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division-questiont:", result4)

result5 = num1 % num2
print("Division-Remainder:", result5)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)

# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-6787)
print("Absolute Value:", result3)

