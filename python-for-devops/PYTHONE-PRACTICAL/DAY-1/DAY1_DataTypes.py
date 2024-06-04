# Numeric Data Types

# ==> integer
x=5
print("Integer Numeric Data Type X = " + str(x))

# ==> Float
x = 3.5466
print("Float Numeric Data Type X =",x)

# ==> Complex
x = 2 + 3j + 6 + 8j
print("Complex Numeric Data Type X = " ,x)


myset = {4,7,8,6,0,6,1,2,3}
print(myset)

my_frozenset = frozenset([8,1,8,2,4,8,7,9,3,5,6,0])
print(my_frozenset)

data = b'Hello'
print(data,"")

binary_data = b'\x48\x65\x6c\x6c\x6f'  # Hexadecimal values for "Hello"
print(binary_data,"")  # Outputs: b'Hello'

binary_data = bytes([95,96,97,98,99,100, 101, 108, 108, 111])
print(binary_data," ",binary_data[0])


binary_data = bytearray(b'Hello')
binary_data[0] = 87  # Change 'H' to 'W' (ASCII value of 'W' is 87)
print(binary_data)  # Outputs: bytearray(b'Wello')

none_type = None
print(none_type)

# Keywords, variables, Global VS Local

ec2_instance_name = "Legend_AWS_EC2_INSTANCE"

a = 10
b = 5
c = 6
def sub():
    a = 10
    b = 8
    print("LOCAL VARIABLE SUBTRACTION = ",a-b-c)

def add():
    print(a+b)
    
def subg():
    print("GLOBAL VARIABLE SUBTRACTION ",a-b-c)
    
add()
sub()
subg()


# mini calculator program

# input_1 = 20
# input_2 = 2
print ("\n ****** MIN CALCULATOR ****** \n  ")
def addition(input_1,input_2):
    
    print(" a =" + str(input_1) + " + b = " + str(input_2) + " = ",input_1+input_2)
    addition_output = input_1+input_2
    print ("return output") 
    return addition_output
def subtraction(input_1,input_2):
    print(" a =" + str(input_1) + " - b = " + str(input_2) + " = ",input_1-input_2)
    return subtraction
def multiplication(input_1,input_2):
    print(" a =" + str(input_1) + " X b = " + str(input_2) + " = ",input_1*input_2)
    return multiplication
def division_reaminder(input_1,input_2):
    print(" a =" + str(input_1) + " % " + "b = " + str(input_2) + " = ",input_1%input_2)
    return division_reaminder
def division_question(input_1,input_2):
    print(" a =" + str(input_1) + " / " + "b = " + str(input_2) + " = ",input_1/input_2)
    return division_question

print(addition(20,2))
print(subtraction(20,2))
print(multiplication(20,2))
print(division_reaminder(20,2))
print(division_question(20,2))
