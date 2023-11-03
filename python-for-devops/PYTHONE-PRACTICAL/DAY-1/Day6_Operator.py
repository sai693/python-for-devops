# Create two variables a and b with numeric values.
import sys

# Check if the correct number of command line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <a> <b>")
    sys.exit(1)

# Convert command line arguments to numbers
a = float(sys.argv[1])
b = float(sys.argv[2])

print("Calculate the sum, difference, product, remainder, Quotient, Float Quotient of a = " + str(a) + " and b = " + str(b) + ".\n")
print("\nResults")
print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Remainder =", a % b)
print("Quotient =", a / b)
print("Float Quotient =", a // b)
